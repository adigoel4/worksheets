def generate_prompt(prompt):
  return"""
Questions: 
1) Question 
2) Question 
3) Question 
4) Question 

Make a Worksheet on {} with 10 Questions and answers
""".format(prompt.capitalize())