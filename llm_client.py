from groq import Groq
# from config.app_config import GROQ_API_KEY

class LLMClient:
    def __init__(self,api_key,model):  
        self.client= Groq(
            api_key=api_key,
        )
        self.model=model
    
    def generate(self,tools,messages):
        response=self.client.chat.completions.create(
            messages=messages,
            model=model,
            tools=tools,
            tool_choice="auto"
        )
        return response
