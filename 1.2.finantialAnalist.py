# Agent for realize finantial researchs at finantial portals

# Importing libs
from agno.agent import Agent
# from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
# from agno.models.groq import Groq
from agno.models.openai import OpenAIChat

# Setting up dot env
from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[YFinanceTools()],
    debug_mode=True
)

agent.print_response("Me dê detalhes sobre a cotação atual da apple, qual seu valor e quais motivos daquele valor")