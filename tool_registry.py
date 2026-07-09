import inspect
from tools.tool import Tool
from tools.llm_tool import LLMTool
class Registry:

    def __init__(self):
        self.tools={}

    def register(self,func):
        tool_details=Tool.from_function(func)
        self.tools[tool_details.name]=tool_details

    def execute(self,tool_name,**kwargs):
        tool=self.tools[tool_name]
        func=tool.function
        result=func(**kwargs)
        return result
    
    def get_tools(self):
        return self.tools

    def get_llm_tools(self):
        llm_tools=[]
        for tool_name,tool_details in self.tools.items():
            llm_tools.append(
                LLMTool.from_tool(tool_details).to_dict()
            )
        return llm_tools

    
    # def _build_tool(self,func):
    #     tool={}
    #     signature=inspect.signature(func)
    #     tool["type"]="function"
    #     tool["name"]=func.__name__
    #     tool["description"]=inspect.getdoc(func)
    #     properties={}
    #     tool["parameters"]={}
    #     tool["required"]=[name for name in signature.parameters.keys()]
    #     tool["parameters"]["properties"]=self._map(signature.parameters.items())
    #     tool["parameters"]["type"]="object"
    #     tool["return_type"]=signature.return_annotation.__name__
    #     tool["function"]=func
    #     return tool

    # def _map(self, parameters):
    #     properties={}
    #     for name, var_type in parameters:
    #         properties[name] = {
    #         "type": self.TYPE_MAPPING[var_type.annotation.__name__]
    #         }
    #     return properties