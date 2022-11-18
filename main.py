import openai
import os
from dotenv import load_dotenv

from generate_prompt import generate_prompt
from formatter import formatter

load_dotenv()

openai.api_key = os.getenv('API_KEY')
topic = input("What should the quiz be about?\n")
length = input("How many questions should the quiz be?\n")
prompt = f"""Generate a quiz with {length} questions and {length} answers about {topic}. {length} Questions, {length} answers. 
Here are a few examples: 

Fractions Quiz: 

Question 1: What is 1/2 + 1/4? 
Question 2: If it takes Bob 10 minutes to run 1 mile, how long does it take for him to run 2/5 of 1 mile? 
Question 3: What is 7/2 * 10/23? 

Answer key: 

Question 1: 3/4 
Question 2: 4 minutes 
Question 3: 70/46

Multiplication Quiz: 

Question 1: What is 7 * 8? 
Question 2: There are 10 girls and 5 guys in the class. If each girl gets 2 apples and each guy gets 1 apple, how many apples are there? 
Question 3: What is 8 * 1.5? 

Answer key: 

Question 1: 56
Question 2: 25 apples
Question 3: 12 

"""
response = openai.Completion.create(
    engine="text-davinci-001", 
    prompt= prompt, 
    presence_penalty=.4,
    temperature=.9,
    max_tokens= 500

    
)
gentext = response.choices[0].text
print(gentext)
