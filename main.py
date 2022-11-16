import openai
import os
from dotenv import load_dotenv

from generate_prompt import generate_prompt
from formatter import formatter

load_dotenv()

openai.api_key = os.getenv('API_KEY')

prompt = input("prompt?\n")

response = openai.Completion.create(
    engine="text-davinci-001", 
    prompt=generate_prompt(prompt),
    max_tokens= 500
)
gentext = response.choices[0].text
