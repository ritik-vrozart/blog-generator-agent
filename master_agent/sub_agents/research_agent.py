"""Research Agent - Gathers comprehensive information on topics."""

from google.adk.agents.llm_agent import Agent
from google.adk.tools.function_tool import FunctionTool
from ..tools.research_tools import conduct_research
from ..config.settings import MODEL_NAME


# Create research tool
research_tool = FunctionTool(
    func=conduct_research,
    require_confirmation=False,
)

# Create Research Agent
research_agent = Agent(
    model=MODEL_NAME,
    name='research_agent',
    description='A research specialist that gathers comprehensive information on topics.',
    instruction=(
        "You are an expert research agent. Your role is to gather comprehensive information "
        "on any given topic. When asked to research:\n\n"
        "1. Use the conduct_research function with:\n"
        "   - The main topic\n"
        "   - Relevant keywords (extract from the request or suggest relevant ones)\n"
        "   - Target audience (if specified)\n\n"
        "2. Your research should cover:\n"
        "   - Key concepts and definitions\n"
        "   - Current trends and statistics\n"
        "   - Best practices and recommendations\n"
        "   - SEO considerations\n"
        "   - Content structure suggestions\n\n"
        "3. Provide comprehensive, well-organized research that will help the writer agent "
        "create high-quality content.\n\n"
        "4. Be thorough and detail-oriented. Your research quality directly impacts the final content.\n\n"
        "Always provide structured, actionable research findings."
    ),
    tools=[research_tool],
)

