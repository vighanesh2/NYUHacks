import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenRouter API Key - MUST be set in .env file!
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError(
        "⚠️  OPENROUTER_API_KEY not found!\n"
        "Please create a .env file in the backend/ directory with:\n"
        "OPENROUTER_API_KEY=your_key_here\n"
        "Get a key at: https://openrouter.ai/keys"
    )

# Database (defaults to SQLite for development)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sat_learning.db")

# Supabase (optional - for auth)
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY", "")

