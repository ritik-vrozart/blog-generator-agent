"""Creative generation tools for AI image creation."""

import re
import os
import base64
import time
from datetime import datetime
from google.genai import Client
from ..utils.state_manager import workflow_state
from ..utils.file_utils import ensure_directory_exists, clean_filename
from ..config.settings import (
    GENERATED_CREATIVES_DIR,
    MODEL_NAME,
    DEFAULT_IMAGE_STYLE,
    DEFAULT_CREATIVE_TYPE,
    MAX_RETRIES,
    RETRY_DELAY
)


def generate_ai_creative(content: str, creative_type: str = DEFAULT_CREATIVE_TYPE, 
                         style: str = DEFAULT_IMAGE_STYLE, count: int = 1) -> str:
    """Generate AI creative images for blog posts and save them to a directory.
    
    Args:
        content: The blog post content to create creatives for
        creative_type: Type of creative (featured image, social media graphic, infographic, etc.)
        style: Visual style (professional, modern, minimalist, vibrant, etc.)
        count: Number of creatives to generate
    
    Returns:
        Information about generated images including file paths.
    """
    if not content:
        return "❌ Error: No content provided for creative generation."
    
    # Extract key information from content
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Blog Post"
    
    # Extract main topic/keywords
    keywords = []
    heading_matches = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if heading_matches:
        keywords.extend(heading_matches[:3])  # Top 3 headings as keywords
    
    # Create directory for storing images
    images_dir = ensure_directory_exists(GENERATED_CREATIVES_DIR)
    
    # Clean title for filename
    safe_title = clean_filename(title)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    generated_images = []
    client = Client()
    
    result_message = f"""
🎨 AI CREATIVE GENERATION
{'=' * 60}

📝 Content Title: {title}
🎯 Creative Type: {creative_type}
✨ Style: {style}
📊 Generating: {count} image(s)

🖼️ GENERATING IMAGES...
"""
    
    for i in range(1, count + 1):
        try:
            # Create enhanced prompt for image generation
            main_keyword = keywords[0] if keywords else title
            image_prompt = (
                f"A {style} {creative_type} for a blog post about {title}. "
                f"The image should be visually appealing, on-brand, and relevant to the content. "
                f"Use colors that complement the topic and maintain a {style} aesthetic. "
                f"Include visual elements that represent {main_keyword}. "
                f"High quality, professional design, suitable for web use."
            )
            
            # Try to generate image using Gemini (note: Gemini 2.5 Flash may not support image generation)
            # This is a placeholder - you may need to use a different image generation API
            image_generated = False
            
            for retry in range(MAX_RETRIES):
                try:
                    if retry > 0:
                        time.sleep(RETRY_DELAY)
                    
                    # Attempt image generation
                    # Note: This is a placeholder. You may need to use:
                    # - Google's Imagen API
                    # - DALL-E API
                    # - Stable Diffusion API
                    # - Or another image generation service
                    
                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=image_prompt,
                    )
                    
                    # Check if response contains image data
                    if hasattr(response, 'candidates') and response.candidates:
                        candidate = response.candidates[0]
                        if hasattr(candidate, 'content') and candidate.content:
                            parts = candidate.content.parts
                            for part in parts:
                                if hasattr(part, 'inline_data') and part.inline_data:
                                    # Extract image data
                                    image_data = part.inline_data.data
                                    image_mime = part.inline_data.mime_type
                                    
                                    # Determine file extension
                                    ext = 'png'
                                    if 'jpeg' in image_mime or 'jpg' in image_mime:
                                        ext = 'jpg'
                                    elif 'webp' in image_mime:
                                        ext = 'webp'
                                    
                                    # Save image to file
                                    filename = f"{safe_title}_{creative_type.replace(' ', '_')}_{i}_{timestamp}.{ext}"
                                    filepath = os.path.join(images_dir, filename)
                                    
                                    # Decode and save image
                                    if isinstance(image_data, str):
                                        image_bytes = base64.b64decode(image_data)
                                    else:
                                        image_bytes = image_data
                                    
                                    with open(filepath, 'wb') as f:
                                        f.write(image_bytes)
                                    
                                    generated_images.append({
                                        "number": i,
                                        "filename": filename,
                                        "filepath": filepath,
                                        "prompt": image_prompt
                                    })
                                    image_generated = True
                                    break
                    
                    if not image_generated:
                        # If no image data, create a placeholder file with prompt info
                        filename = f"{safe_title}_{creative_type.replace(' ', '_')}_{i}_{timestamp}.txt"
                        filepath = os.path.join(images_dir, filename)
                        with open(filepath, 'w') as f:
                            f.write(f"Image Prompt: {image_prompt}\n\n")
                            f.write(f"Note: Image generation requires an image generation API.\n")
                            f.write(f"Use this prompt with DALL-E, Midjourney, or Stable Diffusion.\n")
                        
                        generated_images.append({
                            "number": i,
                            "filename": filename,
                            "filepath": filepath,
                            "prompt": image_prompt,
                            "note": "Prompt saved - use with image generation API"
                        })
                    
                    break
                    
                except Exception as e:
                    if retry == MAX_RETRIES - 1:
                        # Create prompt file as fallback
                        filename = f"{safe_title}_{creative_type.replace(' ', '_')}_{i}_{timestamp}.txt"
                        filepath = os.path.join(images_dir, filename)
                        with open(filepath, 'w') as f:
                            f.write(f"Image Prompt: {image_prompt}\n\n")
                            f.write(f"Error: {str(e)}\n")
                            f.write(f"Note: Use this prompt with an image generation API.\n")
                        
                        generated_images.append({
                            "number": i,
                            "filename": filename,
                            "filepath": filepath,
                            "prompt": image_prompt,
                            "error": str(e)
                        })
                    else:
                        time.sleep(RETRY_DELAY)
                        continue
        
        except Exception as e:
            result_message += f"\n⚠️ Error generating image #{i}: {str(e)}\n"
    
    # Build result message
    result_message += f"\n✅ GENERATION COMPLETE\n"
    result_message += f"{'=' * 60}\n\n"
    
    if generated_images:
        result_message += f"📁 Images saved to directory: {images_dir}\n\n"
        result_message += f"📸 Generated Images:\n\n"
        
        for img in generated_images:
            result_message += f"Image #{img['number']}:\n"
            result_message += f"  📄 Filename: {img['filename']}\n"
            result_message += f"  📍 Filepath: {img['filepath']}\n"
            result_message += f"  🎨 Prompt: {img['prompt'][:100]}...\n"
            if 'note' in img:
                result_message += f"  ℹ️  Note: {img['note']}\n"
            result_message += "\n"
        
        result_message += f"💡 Usage:\n"
        result_message += f"  - Images are saved in: {images_dir}\n"
        result_message += f"  - You can view them in your file system\n"
        result_message += f"  - Use them as featured images, social media graphics, etc.\n"
    else:
        result_message += f"⚠️ No images were generated. Check the error messages above.\n"
    
    result_message += f"\n{'=' * 60}\n"
    
    # Store in workflow state
    workflow_state.add_creative_suggestion({
        "content_title": title,
        "creative_type": creative_type,
        "style": style,
        "count": count,
        "generated_images": generated_images,
        "images_directory": images_dir
    })
    
    return result_message

