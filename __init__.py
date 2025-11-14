"""Multi-Agent Workflow System for Content Creation.

This package provides a modular multi-agent system for creating SEO-optimized blog content
with AI creative generation capabilities.

Main Components:
- Research Agent: Gathers comprehensive information on topics
- Writer Agent: Creates engaging, well-structured content
- Reviewer Agent: Polishes and improves content quality
- Master Agent: Orchestrates the entire workflow and communicates with sub-agents

Usage:
    from image_generation_agent import root_agent  # ADK looks for root_agent
    # or
    from image_generation_agent.master_agent.agent import master_agent
    from image_generation_agent.master_agent.sub_agents import research_agent, writer_agent, reviewer_agent
"""

# Import agent module to make root_agent available (ADK convention)
from . import agent

# Also export agents for convenience
from .master_agent.agent import master_agent, root_agent
from .master_agent.sub_agents.research_agent import research_agent
from .master_agent.sub_agents.writer_agent import writer_agent
from .master_agent.sub_agents.reviewer_agent import reviewer_agent

__all__ = [
    'agent',  # Make agent module available for ADK web discovery
    'master_agent',
    'root_agent',
    'research_agent',
    'writer_agent',
    'reviewer_agent'
]
