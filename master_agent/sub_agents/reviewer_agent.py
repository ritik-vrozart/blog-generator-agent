"""Reviewer Agent - Polishes and improves content quality, SEO, and readability."""

from google.adk.agents.llm_agent import Agent
from google.adk.tools.function_tool import FunctionTool
from ..tools.review_tools import review_and_polish
from ..config.settings import MODEL_NAME


# Create review tool
review_tool = FunctionTool(
    func=review_and_polish,
    require_confirmation=False,
)

# Create Reviewer Agent
reviewer_agent = Agent(
    model=MODEL_NAME,
    name='reviewer_agent',
    description='A content reviewer that polishes and improves content quality, SEO, and readability.',
    instruction=(
        "You are an expert content reviewer and editor. Your role is to review, polish, and improve "
        "content for quality, SEO, and readability. When asked to review content:\n\n"
        "1. Use the review_and_polish function with:\n"
        "   - The draft content from the writer agent\n"
        "   - Focus areas (clarity, SEO, engagement, readability, etc.)\n"
        "   - SEO optimization flag\n"
        "   - Grammar check flag\n\n"
        "2. Your review should:\n"
        "   - Check grammar, spelling, and punctuation\n"
        "   - Improve clarity and readability\n"
        "   - Optimize for SEO (keywords, meta descriptions, headings)\n"
        "   - Enhance engagement and flow\n"
        "   - Ensure consistency in tone and style\n"
        "   - Verify factual accuracy (where possible)\n\n"
        "3. Provide detailed review notes explaining:\n"
        "   - What was improved\n"
        "   - Why changes were made\n"
        "   - Additional recommendations\n\n"
        "4. Return polished, publication-ready content.\n\n"
        "5. Be thorough but constructive. Your goal is to make the content the best it can be.\n\n"
        "Always provide comprehensive reviews that significantly improve content quality."
    ),
    tools=[review_tool],
)

