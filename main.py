from textbase.message import Message
from textbase import models, bot
from typing import List

# Load your OpenAI API key
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")
models.OpenAI.api_key = "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" #api 

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You will be provided with statements, and your task is to convert them to standard English."""

@bot()
def on_message(message_history: List[Message], state: dict = None):
    """correcting grammar
#     message_history: List of user messages
#     state: A dictionary to store any stateful information

#     Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
#     """

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )


    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }