import os

# pip install openai
import openai

# -----------------------------------------------------------------
# pip install python-dotenv
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

openai.api_key = os.getenv("api_key")


# list models
models = openai.Model.list()


# create a completion
def handle_input(user_input):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])
    return completion


# print the completion
while True:
    user_input = input("You: ")
    ai_response = handle_input(user_input).choices[0].message.content
    print(ai_response)
