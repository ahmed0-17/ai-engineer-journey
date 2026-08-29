from typing import TypeVar



class AgentTools:
    def execute(self)->str:
        pass

T=TypeVar("T",bound=AgentTools)


class SearchTool(AgentTools):
    pass


class CalculatorTool(AgentTools):
    pass



def register_tool(tool:T)->T:
    return tool


searchtool=SearchTool()
print(register_tool(searchtool))
calculator=CalculatorTool()
print(register_tool(calculator))

