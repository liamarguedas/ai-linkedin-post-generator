from source.agent import BaseAgent
from source.llm import BaseLLM
from source.system import load_system_prompt 
from source.tool import read_image, create_linkeding_post
from langchain.messages import HumanMessage


def main():

    instance = BaseAgent(llm=BaseLLM().get_default())

    instance.add_system_prompt(load_system_prompt())
    
    instance.add_tool([read_image, create_linkeding_post])

    orchestrator = instance.create()


    url = "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/61/6e/6c/img-20190915-110222-largejpg.jpg?w=500&h=-1&s=1"

    prompt = f"""

        read the image from this url and provide a description. Once the description has been provided, then create a linkeding post.

        URL = {url}
        
        """

    response = orchestrator.invoke({
        "messages": HumanMessage(prompt)
    })

    print(response["messages"][-1].content)



if __name__ == "__main__":
    main()
