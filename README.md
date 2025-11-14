# Multi-Agent Workflow System

A modular multi-agent system for creating SEO-optimized blog content with AI creative generation capabilities.

## 📁 Project Structure

Following Google ADK conventions:

```
image_generation_agent/
├── __init__.py                 # Package exports (imports agent module)
├── agent.py                    # Main entry point - ADK looks for 'root_agent' here
├── README.md                   # This file
│
├── config/                     # Configuration settings
│   ├── __init__.py
│   └── settings.py            # Model, directory, and default settings
│
├── agents/                     # Master agent definition
│   ├── __init__.py
│   └── master_agent.py        # Master orchestrator agent
│
├── sub_agents/                 # Sub-agents (following ADK convention)
│   ├── __init__.py
│   ├── research_agent.py      # Research specialist agent
│   ├── writer_agent.py        # Content writer agent
│   └── reviewer_agent.py      # Content reviewer agent
│
├── tools/                      # Tool functions for agents
│   ├── __init__.py
│   ├── research_tools.py      # Research functionality
│   ├── writing_tools.py       # Content writing functionality
│   ├── review_tools.py        # Content review functionality
│   └── creative_tools.py      # AI creative generation
│
└── utils/                      # Utility modules
    ├── __init__.py
    ├── state_manager.py       # Workflow state management
    └── file_utils.py          # File handling utilities
```

## 🎯 Agents

### 1. Research Agent (`research_agent`)
- **Purpose**: Gathers comprehensive information on topics
- **Tool**: `conduct_research()`
- **Output**: Research report with key findings, SEO considerations, and content structure recommendations

### 2. Writer Agent (`writer_agent`)
- **Purpose**: Creates engaging, well-structured content
- **Tool**: `write_content()`
- **Output**: Draft content ready for review

### 3. Reviewer Agent (`reviewer_agent`)
- **Purpose**: Polishes and improves content quality
- **Tool**: `review_and_polish()`
- **Output**: Polished, publication-ready content

### 4. Master Agent (`master_agent`)
- **Purpose**: Orchestrates the entire workflow
- **Tools**: All tools from research, writing, review, and creative generation
- **Workflow**: Research → Writing → Review → AI Creative Generation (optional)

## 🔄 Workflow

```
User Request
    ↓
Master Agent (Orchestrator)
    ↓
Research Agent → Gathers info & keywords
    ↓
Writer Agent → Generates content
    ↓
Reviewer Agent → Polishes & optimizes
    ↓
AI Creative Generation → Creates images/graphics
    ↓
Final SEO-Optimized Content + Creatives
```

## 🚀 Usage

### Google ADK Usage (Standard)
```python
# ADK automatically looks for 'root_agent' in agent.py
from image_generation_agent import root_agent

# Or import directly
from image_generation_agent.agent import root_agent
```

### Direct Import
```python
from image_generation_agent.agents.master_agent import master_agent
from image_generation_agent.sub_agents import research_agent, writer_agent, reviewer_agent

# Use the master agent to coordinate the workflow
# The agent will guide users through:
# 1. Research phase
# 2. Writing phase
# 3. Review phase
# 4. AI creative generation (optional)
```

## ⚙️ Configuration

Edit `config/settings.py` to customize:
- Model name
- Directory paths
- Default values (word count, tone, style, etc.)
- Retry settings

## 📝 Features

- ✅ Modular architecture for easy maintenance
- ✅ Separated concerns (agents, tools, utils, config)
- ✅ State management across workflow
- ✅ File utilities for image storage
- ✅ SEO optimization built-in
- ✅ AI creative generation support
- ✅ Backward compatibility maintained

## 🔧 Adding New Features

1. **New Tool**: Add to `tools/` directory
2. **New Agent**: Add to `agents/` directory
3. **New Utility**: Add to `utils/` directory
4. **Configuration**: Update `config/settings.py`

## 📦 Dependencies

- `google-adk`: Agent framework
- `google-genai`: GenAI client
- Standard library: `os`, `re`, `json`, `datetime`, `time`, `base64`

