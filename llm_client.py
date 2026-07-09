from groq import Groq
from config.app_config import GROQ_API_KEY

class LLMClient:
    def __init__(self):
        self.client= Groq(
            api_key=GROQ_API_KEY
        )
    
    def generate(self,model,tools,messages):
        response=self.client.chat.completions.create(
            messages=messages,
            model=model,
            tools=tools,
            tool_choice="auto"
        )
        return response
