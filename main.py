from source.agent import BaseAgent
from source.llm import BaseLLM
from langchain.messages import HumanMessage


def main():

    instance = BaseAgent(llm=BaseLLM().get_default())
    
    agent = instance.create()

    response = agent.invoke({

        "messages": HumanMessage("How many people live in Texas")

    })

    print(response["messages"][-1].content)

    



if __name__ == "__main__":
    main()
