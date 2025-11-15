"""Writing tools for content generation."""

import re
from google.genai import Client
from ..utils.state_manager import workflow_state
from ..config.settings import DEFAULT_WORD_COUNT, DEFAULT_TONE, MODEL_NAME


def write_content(topic: str, research_data: str, content_type: str = "blog post", 
                  word_count: int = DEFAULT_WORD_COUNT, tone: str = DEFAULT_TONE) -> str:
    """Generate content based on research data using AI.
    
    Args:
        topic: The main topic for the content
        research_data: Research findings from the research agent
        content_type: Type of content (blog post, article, guide, etc.)
        word_count: Target word count for the content
        tone: Writing tone (professional, casual, friendly, etc.)
    
    Returns:
        A draft of the generated content that integrates all research findings.
    """
    if not topic:
        return "❌ Error: No topic provided for content writing."
    
    if not research_data:
        return "❌ Error: No research data provided. Please conduct research first."
    
    # Extract key information from research
    keywords_match = re.search(r'Keywords: (.+)', research_data)
    keywords = keywords_match.group(1) if keywords_match else "related topics"
    
    target_audience_match = re.search(r'Target Audience: (.+)', research_data)
    target_audience = target_audience_match.group(1).strip() if target_audience_match else "general"
    
    # Create a comprehensive prompt that uses ALL research data
    writing_prompt = f"""You are an expert content writer. Write a comprehensive {content_type} about "{topic}" based on the following detailed research findings.

RESEARCH DATA:
{research_data}

REQUIREMENTS:
- Topic: {topic}
- Content Type: {content_type}
- Target Word Count: {word_count} words
- Writing Tone: {tone}
- Target Audience: {target_audience}
- Keywords to include: {keywords}

CRITICAL INSTRUCTIONS:
1. **MUST USE ALL RESEARCH DATA**: Integrate ALL findings, insights, statistics, and recommendations from the research data above. Do NOT create generic content.

2. **Specific Content Requirements**:
   - Use the exact keywords and topics mentioned in the research
   - Include all key findings from the research report
   - Address all points mentioned in the research structure recommendations
   - Incorporate SEO considerations from the research
   - Use the specific insights and recommendations provided

3. **Content Structure** (based on research):
   - Create an engaging introduction that hooks the reader
   - Use clear H2 and H3 headings as recommended in the research
   - Include all sections mentioned in the research (key concepts, benefits, best practices, challenges, etc.)
   - Add specific examples, data, and statistics from the research where applicable
   - Include actionable insights and practical tips
   - End with a strong conclusion that summarizes key points

4. **Writing Quality**:
   - Write in a {tone} tone
   - Make it engaging and valuable for the {target_audience} audience
   - Ensure the content is well-structured with proper markdown formatting
   - Use the keywords naturally throughout the content
   - Include specific details, not generic statements

5. **Format**:
   - Use markdown format with # for main title, ## for main headings, ### for subheadings
   - Include bullet points and numbered lists where appropriate
   - Make it scannable and easy to read

6. **DO NOT**:
   - Create generic or templated content
   - Ignore the research data
   - Use placeholder text
   - Write vague or generic statements
   - Skip important points from the research

Write a comprehensive, detailed, and well-researched {content_type} that fully integrates all the research findings above. The content should be approximately {word_count} words and should feel like it was written specifically for this topic using the research provided.

Start writing now:"""
    
    try:
        # Generate content using Gemini API
        client = Client()
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=writing_prompt,
        )
        
        # Extract the generated content
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'content') and candidate.content:
                parts = candidate.content.parts
                generated_text = ""
                for part in parts:
                    if hasattr(part, 'text'):
                        generated_text += part.text
                
                if generated_text:
                    # Ensure proper formatting
                    draft_content = generated_text.strip()
                    
                    # Add metadata at the end
                    draft_content += f"""

---

**Topic**: {topic}
**Keywords**: {keywords}
**Content Type**: {content_type}
**Tone**: {tone}
**Target Audience**: {target_audience}
**Target Word Count**: {word_count} words
**Status**: Draft - Ready for Review
"""
                    
                    # Store draft content in workflow state
                    workflow_state.set_draft_content({
                        "topic": topic,
                        "content": draft_content,
                        "content_type": content_type,
                        "word_count": word_count,
                        "tone": tone,
                        "research_used": True
                    })
                    
                    return draft_content
        
        # Fallback if no content generated
        return f"⚠️ Warning: Content generation completed but no text was returned. Please try again.\n\nResearch data provided:\n{research_data[:500]}..."
        
    except Exception as e:
        error_message = f"❌ Error generating content: {str(e)}\n\n"
        error_message += f"Research data that was provided:\n{research_data[:500]}...\n\n"
        error_message += "Please try again or check the research data."
        return error_message

