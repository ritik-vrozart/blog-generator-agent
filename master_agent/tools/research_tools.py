"""Research tools for gathering information."""

from typing import List
from ..utils.state_manager import workflow_state


def conduct_research(topic: str, keywords: List[str], target_audience: str = "general") -> str:
    """Conduct research on a given topic and gather relevant information.
    
    Args:
        topic: The main topic to research
        keywords: List of keywords related to the topic
        target_audience: Target audience for the content (default: general)
    
    Returns:
        A comprehensive research report with key findings, statistics, and insights.
    """
    if not topic:
        return "❌ Error: No topic provided for research."
    
    # Simulate research gathering (in production, this would use web search, APIs, etc.)
    keywords_str = ", ".join(keywords) if keywords else "related topics"
    
    research_report = f"""
📚 RESEARCH REPORT
{'=' * 60}

Topic: {topic}
Keywords: {keywords_str}
Target Audience: {target_audience}

🔍 KEY FINDINGS:

1. Topic Overview:
   - {topic} is a relevant and important subject in today's context
   - Current trends show growing interest in this area
   - Multiple perspectives and approaches exist

2. Key Points to Cover:
   - Introduction and background information
   - Main concepts and definitions
   - Benefits and applications
   - Best practices and recommendations
   - Common challenges and solutions
   - Future trends and outlook

3. SEO Considerations:
   - Primary keyword: {topic}
   - Secondary keywords: {keywords_str}
   - Target audience: {target_audience}
   - Recommended content length: 1500-2500 words
   - Suggested headings: H2 and H3 tags for structure

4. Content Structure Recommendations:
   - Engaging introduction with hook
   - Clear value proposition
   - Well-organized sections with subheadings
   - Actionable insights and takeaways
   - Strong conclusion with call-to-action

5. Additional Insights:
   - Include relevant examples and case studies
   - Use data and statistics where possible
   - Address common questions and concerns
   - Provide practical tips and advice

📊 Research Status: Complete
✅ Ready for content writing phase

{'=' * 60}
"""
    
    # Store research data in workflow state
    workflow_state.set_research_data({
        "topic": topic,
        "keywords": keywords,
        "target_audience": target_audience,
        "report": research_report
    })
    
    return research_report

