



from typing import Callable, List
from langchain_openai import ChatOpenAI 
from langchain.agents import create_agent
from pydantic import BaseModel, PrivateAttr, Field

class BaseAgent(BaseModel):

    llm: ChatOpenAI = Field(..., validate_default=False)
    _system_prompt: str = PrivateAttr(default="")
    _tools: List[Callable] = PrivateAttr(default_factory=list)

    def add_system_prompt(self, prompt: str):
        self._system_prompt = prompt
        
    def add_tool(self, tool):

        if isinstance(tool, List):
            self._tools.extend(tool)

        else:
            self._tools.append(tool)


    def create(self):
        return create_agent(
            model=self.llm,
            tools=self._tools,
            system_prompt=self._system_prompt
        )
    








