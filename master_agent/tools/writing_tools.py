"""Writing tools for content generation."""

import re
from ..utils.state_manager import workflow_state
from ..config.settings import DEFAULT_WORD_COUNT, DEFAULT_TONE


def write_content(topic: str, research_data: str, content_type: str = "blog post", 
                  word_count: int = DEFAULT_WORD_COUNT, tone: str = DEFAULT_TONE) -> str:
    """Generate content based on research data.
    
    Args:
        topic: The main topic for the content
        research_data: Research findings from the research agent
        content_type: Type of content (blog post, article, guide, etc.)
        word_count: Target word count for the content
        tone: Writing tone (professional, casual, friendly, etc.)
    
    Returns:
        A draft of the generated content.
    """
    if not topic:
        return "❌ Error: No topic provided for content writing."
    
    if not research_data:
        return "❌ Error: No research data provided. Please conduct research first."
    
    # Extract key information from research
    keywords_match = re.search(r'Keywords: (.+)', research_data)
    keywords = keywords_match.group(1) if keywords_match else "related topics"
    
    # Generate content structure
    draft_content = f"""
# {topic}

## Introduction

Welcome to this comprehensive guide on {topic}. In this {content_type}, we'll explore everything you need to know about this important subject, providing you with valuable insights and practical information.

{topic} has become increasingly relevant in today's world, and understanding its key aspects can help you make informed decisions and achieve better results.

## Understanding {topic}

{topic} encompasses various important concepts and principles. Let's dive into the fundamental aspects that make this topic significant.

### Key Concepts

The core concepts of {topic} include several essential elements that work together to create a comprehensive understanding. These concepts form the foundation for deeper exploration and application.

### Benefits and Applications

Understanding {topic} offers numerous benefits, including:

- Enhanced knowledge and awareness
- Better decision-making capabilities
- Improved outcomes and results
- Practical applications in various contexts

## Best Practices

When working with {topic}, following best practices can significantly improve your results:

1. **Start with the Basics**: Build a solid foundation before advancing
2. **Stay Updated**: Keep abreast of the latest developments and trends
3. **Apply Consistently**: Regular application leads to better outcomes
4. **Learn from Experience**: Reflect on what works and what doesn't

## Common Challenges and Solutions

Many people encounter challenges when dealing with {topic}. Here are some common issues and their solutions:

### Challenge 1: Getting Started
**Solution**: Begin with clear goals and a structured approach. Break down complex tasks into manageable steps.

### Challenge 2: Maintaining Consistency
**Solution**: Develop a routine and stick to it. Track your progress and adjust as needed.

### Challenge 3: Staying Motivated
**Solution**: Set milestones and celebrate achievements. Connect with others who share similar interests.

## Advanced Strategies

For those looking to take their understanding of {topic} to the next level, consider these advanced strategies:

- Deep dive into specialized areas
- Connect with experts and communities
- Experiment with different approaches
- Continuously refine your methods

## Future Trends

The landscape of {topic} is constantly evolving. Here are some trends to watch:

- Emerging technologies and methodologies
- Changing perspectives and approaches
- New opportunities and applications
- Evolving best practices

## Conclusion

In conclusion, {topic} is a multifaceted subject that offers significant value when properly understood and applied. By following the insights and recommendations outlined in this guide, you can navigate this topic more effectively and achieve your desired outcomes.

Remember, success with {topic} comes from consistent effort, continuous learning, and practical application. Start implementing these strategies today and see the positive impact on your journey.

---

**Keywords**: {keywords}
**Content Type**: {content_type}
**Tone**: {tone}
**Target Word Count**: {word_count} words
**Status**: Draft - Ready for Review

"""
    
    # Store draft content in workflow state
    workflow_state.set_draft_content({
        "topic": topic,
        "content": draft_content,
        "content_type": content_type,
        "word_count": word_count,
        "tone": tone
    })
    
    return draft_content

