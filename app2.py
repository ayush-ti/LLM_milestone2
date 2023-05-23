# Bring in deps
import os 
from apikey import apikey 
os.environ['OPENAI_API_KEY'] = apikey

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

prompt = PromptTemplate(
    input_variables=["product"],
    template="correct all the math calculations in {product}?",
)

llm = OpenAI(
          model_name="text-davinci-003", 
          temperature=0.9)


problem1=prompt.format(product="There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $40")
problem2=prompt.format(product="There are 10 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $40")
problem3=prompt.format(product="There are 5 items on the menu and each cost $20 on average. Even if we get all of them, We will have to pay $40")
problem4=prompt.format(product="There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $80")


print(llm(problem1))
print(llm(problem2))
print(llm(problem3))
print(llm(problem4))


# output

# There are 5 items on the menu and each cost $10 on average. Even if we get all of them, we will have to pay $50.

# There are 10 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $100.

# There are 5 items on the menu and each cost $20 on average. Even if we get all of them, We will have to pay $100.

# There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $50.
