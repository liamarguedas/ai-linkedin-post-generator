





from os import waitpid
from langchain.tools import tool
from pathlib import Path
from ..agent import BaseAgent
from ..llm import BaseLLM
from ..system import load_system_prompt
from langchain.messages import HumanMessage


CURRENT_DESCRIPTION = None


@tool
def read_image(url: str):
    """
    Recieves an image url, reads it and returns a description of the image.

    Arguments:
        url: str, url of the image.

    Returns:
        str, description of the image.
    """
    global CURRENT_DESCRIPTION

    read_image_agent = BaseAgent(llm=BaseLLM().get_default()).create()

    result = read_image_agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=[
                        {"type": "text", "text": "Describe this image in detail."},
                        {
                            "type": "image_url",
                            "image_url": {"url": url},
                        },
                    ]
                )
            ]
        }
    )
    content = result["messages"][-1].content
    CURRENT_DESCRIPTION = content
    return content

@tool
def create_linkeding_post():
    """
    Can only be executed if read_image was executed before. Creates a linkedin post based on the description of the image.

    Returns:
        str, the linkedin post.
    """
    if CURRENT_DESCRIPTION is not None: 
        linkedin_post_creation_agent = BaseAgent(llm=BaseLLM().get_default()).create()

        result = linkedin_post_creation_agent.invoke(
            {
                "messages": [
                    HumanMessage(
                        content=[
                            {"type": "text", "text": 
                             f"""Based on DESCRIPTION, Compose a sarcastic LinkedIn post mocking typical motivational content. 
                             The post should follow the common structure
                             of a motivational post, including phrases like  'I remember when...'
                             and detailing a seemingly difficult situation that ultimately led to a profound, 
                             often clichéd, lesson. The tone should be obviously sarcastic.

                             DESCRIPTION = {CURRENT_DESCRIPTION}
                             """
                            }

                            ]
                    )
                ]
            }
        )
        content = result["messages"][-1].content
        return content



    






















