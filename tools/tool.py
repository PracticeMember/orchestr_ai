import inspect
class Tool:
    def __init__(self, name, description, parameters, return_type, function):
        self.name=name
        self.description=description
        self.parameters=parameters
        self.return_type=return_type
        self.function=function
    
    @staticmethod
    def from_function(func):
        signature=inspect.signature(func)
        name=func.__name__
        description=inspect.getdoc(func)
        parameters={}
        for param_name,param_type in signature.parameters.items():
            parameters[param_name]=param_type.annotation.__name__
        return_type=signature.return_annotation.__name__
        return Tool(name=name,
                    description=description,
                    parameters=parameters,
                    return_type=return_type,
                    function=func)


    def __repr__(self):
        return (
            f"name={self.name}, "
            f"description={self.description}, "
            f"parameters={self.parameters}, "
            f"return_type={self.return_type}"
        )
