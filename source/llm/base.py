





from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

class BaseLLM(BaseModel):
    
    model: str = "gpt-4.1"
    temperature: float = 0.90

    def get_default(self):
        load_dotenv()
        return ChatOpenAI(
            model=self.model,
            temperature=self.temperature
        ) 


