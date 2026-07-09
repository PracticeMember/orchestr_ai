
class LLMTool:
    
    TYPE_MAPPING={
        "int": "integer",
        "str": "string",
        "float": "number",
        "bool" : "boolean"
    }

    def __init__(self,name,description,parameters,required):
        self.type="function"
        self.name=name
        self.description=description
        self.parameters=parameters
        self.required=required
    
    @staticmethod
    def from_tool(tool):
        name=tool.name
        description=tool.description
        llm_parameters=LLMTool._map_parameters(tool.parameters)
        required=[param_name for param_name in tool.parameters]
        return LLMTool(name=name,description=description,
                        parameters=llm_parameters,
                        required=required)
    
    @classmethod
    def _map_parameters(cls,parameters):
        properties={}
        for param_name, param_type in parameters.items():
            properties[param_name] = {
            "type": cls.TYPE_MAPPING[param_type]
            }
        return properties


    def to_dict(self):
        return {
        "type": self.type,
        "function": {
            "name": self.name,
            "description": self.description,
            "parameters": 
            {
                "type": "object",
                "properties": self.parameters,
                "required": self.required
            }
          }
        }

    def __repr__(self):        
        return (f"{self.type}, "
         f"{self.name}, "
         f"{self.description},"
         f"{self.parameters},"
         f"{self.required}")

