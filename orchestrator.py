from groq import Groq
from config.app_config import LLM_MODEL
import json
import config.logging_config
import logging

logger=logging.getLogger(__name__)

class Orchestrator:
    
    def __init__(self,registry,llm_client):
        self.registry=registry
        self.llm_client=llm_client
    
    def answer(self,question,messages):
        messages.append({
            "role": "user",
            "content": f"{question}"
        })
        return self._call_llm_multiple_tools(messages)

    def _call_llm(self,messages):
        llm_tools=self.registry.get_llm_tools()
        response=self.llm_client.generate(LLM_MODEL,llm_tools,messages)
        message=response.choices[0].message
        logger.info("Tool Calls : %s",message.tool_calls)
        if message.tool_calls:
            tool_call=message.tool_calls[0]
            tool_name=tool_call.function.name
            arguments=tool_call.function.arguments
            arguments=json.loads(arguments)
            tool_result=self._execute_tool(tool_name,**arguments)
            self._append_tool_call(tool_call,messages)
            self._append_tool_call_result(tool_call,tool_result,messages)
            self._call_llm(messages)
        elif message.content:
            content_message={
                "role": "assistant",
                "content": f"{message.content}"
            }
            messages.append(content_message)
        
    def _call_llm_multiple_tools(self,messages):
        llm_tools=self.registry.get_llm_tools()
        response=self.llm_client.generate(LLM_MODEL,llm_tools,messages)
        message=response.choices[0].message
        logger.info("Tool Calls : %s",message.tool_calls)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name=tool_call.function.name
                arguments=tool_call.function.arguments
                arguments=json.loads(arguments)
                tool_result=self._execute_tool(tool_name,**arguments)
                self._append_tool_call(tool_call,messages)
                self._append_tool_call_result(tool_call,tool_result,messages)
            self._call_llm_multiple_tools(messages)
        if message.content:
            content_message={
                "role": "assistant",
                "content": f"{message.content}"
            }
            messages.append(content_message)

    def _append_tool_call_result(self,tool_call,tool_result,messages):
        messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(tool_result)
                })
        
    def _append_tool_call(self,tool_call,messages):
        messages.append({
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": f"{tool_call.id}",
                        "type": "function",
                        "function": {
                            "name": f"{tool_call.function.name}",
                            "arguments": f"{tool_call.function.arguments}"
                        }
                    }
                ]
            }
            )
        
    def _execute_tool(self,tool_name,**kwargs):
        return self.registry.execute(tool_name,**kwargs)




