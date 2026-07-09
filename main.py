from tools.calculator import multiply,add,divide,subtract
from llm_client import LLMClient
from tool_registry import Registry
from orchestrator import Orchestrator
import json

if __name__=="__main__":
    client = LLMClient()
    registry=Registry()
    registry.register(multiply)
    registry.register(add)
    registry.register(divide)
    orc=Orchestrator(registry,client)
    messages=[]
    orc.answer("Definition of mathematics under 20 words",messages)
    orc.answer("can you multiply 43 with 54,then multiply result with 35, then add 24 to result",messages)
    print(json.dumps(messages,indent=4))