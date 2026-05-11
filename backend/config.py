"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter# Models for the council
COUNCIL_MODELS = [
    "gemini-flash-3",          # Primary
    "gemini-pro-3.1-low",      # Support
    "sonnet-thinking-4.6"      # Diversity
]

CHAIRMAN_MODEL = "gemini-pro-3.1-high"  # The final judge

# Fallback models
FALLBACK_MODELS = ["opus-thinking-4.6", "gpt-oss-120b-medium"]

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
