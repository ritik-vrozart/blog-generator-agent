"""Main entry point for Google ADK.

ADK automatically looks for 'root_agent' variable in this file.
"""

from .master_agent.agent import root_agent

# ADK looks for 'root_agent' - it's imported from master_agent.agent
__all__ = ['root_agent']

