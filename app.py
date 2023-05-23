# slving the same problem using agents and pal-math
import os 
from apikey import apikey 
os.environ['OPENAI_API_KEY'] = apikey

from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import load_tools

llm = OpenAI(temperature=0)
tools = load_tools(["pal-math"], llm=llm)

agent = initialize_agent(tools,
                         llm,
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True)

agent.run("There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $40")

agent.run("There are 6 items on the menu and each cost $60 on average. Even if we get all of them, We will have to pay $100")

agent.run("There are 5 items on the menu and each cost $20 on average. Even if we get all of them, We will have to pay $80")

agent.run("There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $100")

agent.run("There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $200")


# output

# > Entering new AgentExecutor chain...
#  I need to figure out how much each item costs
# Action: PAL-MATH
# Action Input: What is the cost of each item if the total cost of all 5 items is $40?


# > Entering new AgentExecutor chain...
#  I need to figure out how much each item costs
# Action: PAL-MATH
# Action Input: What is the cost of each item if the total cost of all 5 items is $80?
# Observation: 16.0
# Thought: I now know the final answer
# Final Answer: Each item costs $16.

# > Finished chain.


# > Entering new AgentExecutor chain...
#  I need to figure out how much each item costs
# Action: PAL-MATH
# Action Input: What is the cost of each item if the total cost of all 5 items is $100?
# Observation: 20.0
# Thought: I now know the final answer
# Final Answer: Each item costs $20.

# > Finished chain.


# > Entering new AgentExecutor chain...
#  I need to figure out how much each item costs
# Action: PAL-MATH
# Action Input: How much does each item cost if the total cost of all 5 items is $200?
# Observation: 40.0
# Thought: I now know the final answer
# Final Answer: Each item costs $40.

# > Finished chain.