import os
from textbase import bot, Message
from textbase.models import HuggingFace
from typing import List

# Load your OpenAI API key
# HuggingFace.api_key = ""
# or from environment variable:
HuggingFace.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with a Medical Assistant. I can provide information on medical topics and answer health-related questions. Please remember that I'm not a substitute for professional medical advice. If you have a medical emergency, please call emergency services immediately.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate HuggingFace response. Uses the DialoGPT-large model from Microsoft by default.
    bot_response = HuggingFace.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
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