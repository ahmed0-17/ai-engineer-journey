from typing import TypeVar

class AgentTool:
    def execute(self) -> str:
        pass

T=TypeVar("T",bound=AgentTool)    


class SearchTool(AgentTool):
    pass


class CalculatorTool(AgentTool):
    pass



def register_tool(tool:T)->T:
    return tool





calculator_tool=CalculatorTool()
print(register_tool(calculator_tool))