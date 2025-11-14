"""Writer Agent - Creates engaging, well-structured content based on research."""

from google.adk.agents.llm_agent import Agent
from google.adk.tools.function_tool import FunctionTool
from ..tools.writing_tools import write_content
from ..config.settings import MODEL_NAME


# Create writing tool
writing_tool = FunctionTool(
    func=write_content,
    require_confirmation=False,
)

# Create Writer Agent
writer_agent = Agent(
    model=MODEL_NAME,
    name='writer_agent',
    description='A content writer that creates engaging, well-structured content based on research.',
    instruction=(
        "You are an expert content writer. Your role is to create engaging, well-structured content "
        "based on research findings. When asked to write content:\n\n"
        "1. First, check if research has been conducted. If not, inform the user that research is needed first.\n\n"
        "2. Use the write_content function with:\n"
        "   - The topic\n"
        "   - Research data from the research agent\n"
        "   - Content type (blog post, article, guide, etc.)\n"
        "   - Target word count\n"
        "   - Desired tone\n\n"
        "3. Your writing should:\n"
        "   - Be engaging and well-structured\n"
        "   - Follow SEO best practices\n"
        "   - Include clear headings and subheadings\n"
        "   - Be informative and valuable\n"
        "   - Have a strong introduction and conclusion\n"
        "   - Include actionable insights\n\n"
        "4. Create content that is ready for review but may need polishing.\n\n"
        "5. Write in a clear, professional tone that matches the target audience.\n\n"
        "Always create high-quality, comprehensive content based on the research provided."
    ),
    tools=[writing_tool],
)

