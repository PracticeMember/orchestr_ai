import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
LLM_MODEL=os.getenv("LLM_MODEL")