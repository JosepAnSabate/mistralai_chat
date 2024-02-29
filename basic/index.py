from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-medium"

client = MistralClient(api_key=api_key)

messages = [
    ChatMessage(role="user", content="")
]

# No streaming
chat_response = client.chat(
    model=model,
    messages=messages,
)

print('chat_response: ', chat_response)

