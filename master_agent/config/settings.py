"""Configuration settings for the multi-agent workflow system."""

# Model configuration
MODEL_NAME = 'gemini-2.5-flash'
IMAGE_GENERATION_MODEL = 'gemini-2.5-flash-image-preview'  # Model for AI creative generation

# Directory configuration
GENERATED_CREATIVES_DIR = "generated_creatives"
WORKFLOW_STATE_FILE = "workflow_state.json"

# Image generation settings
DEFAULT_IMAGE_STYLE = "professional"
DEFAULT_CREATIVE_TYPE = "featured image"
DEFAULT_IMAGE_COUNT = 1

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Content settings
DEFAULT_WORD_COUNT = 1500
DEFAULT_TONE = "professional"
DEFAULT_TARGET_AUDIENCE = "general"

