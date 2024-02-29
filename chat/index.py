import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-medium"

def main():

    client = MistralClient(api_key=api_key)

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content="city now")],
    )
    print(chat_response.choices[0].message.content)


if __name__ == "__main__":
    main()