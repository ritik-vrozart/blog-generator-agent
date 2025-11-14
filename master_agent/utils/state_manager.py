"""Workflow state management utilities."""

from typing import Dict, Any, Optional
import json
import os
from ..config.settings import WORKFLOW_STATE_FILE


class WorkflowState:
    """Manages workflow state across agents."""
    
    def __init__(self):
        self.state = {
            "research_data": None,
            "draft_content": None,
            "final_content": None,
            "creative_suggestions": []
        }
    
    def set_research_data(self, data: Dict[str, Any]) -> None:
        """Store research data."""
        self.state["research_data"] = data
    
    def get_research_data(self) -> Optional[Dict[str, Any]]:
        """Retrieve research data."""
        return self.state.get("research_data")
    
    def set_draft_content(self, content: Dict[str, Any]) -> None:
        """Store draft content."""
        self.state["draft_content"] = content
    
    def get_draft_content(self) -> Optional[Dict[str, Any]]:
        """Retrieve draft content."""
        return self.state.get("draft_content")
    
    def set_final_content(self, content: Dict[str, Any]) -> None:
        """Store final content."""
        self.state["final_content"] = content
    
    def get_final_content(self) -> Optional[Dict[str, Any]]:
        """Retrieve final content."""
        return self.state.get("final_content")
    
    def add_creative_suggestion(self, suggestion: Dict[str, Any]) -> None:
        """Add creative suggestion."""
        if "creative_suggestions" not in self.state:
            self.state["creative_suggestions"] = []
        self.state["creative_suggestions"].append(suggestion)
    
    def get_creative_suggestions(self) -> list:
        """Retrieve all creative suggestions."""
        return self.state.get("creative_suggestions", [])
    
    def save_to_file(self) -> None:
        """Save state to file."""
        try:
            with open(WORKFLOW_STATE_FILE, 'w') as f:
                json.dump(self.state, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save state to file: {e}")
    
    def load_from_file(self) -> None:
        """Load state from file."""
        if os.path.exists(WORKFLOW_STATE_FILE):
            try:
                with open(WORKFLOW_STATE_FILE, 'r') as f:
                    self.state = json.load(f)
            except Exception as e:
                print(f"Warning: Could not load state from file: {e}")
    
    def clear(self) -> None:
        """Clear all state."""
        self.state = {
            "research_data": None,
            "draft_content": None,
            "final_content": None,
            "creative_suggestions": []
        }


# Global workflow state instance
workflow_state = WorkflowState()

