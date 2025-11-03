# Agent that uses custom tools

# Importing libs
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq

# Setting up dot env
from dotenv import load_dotenv
load_dotenv()

# Building functions
def celsius_to_fh(temp_celsius: float):
    """
    Converte uma temperatura em graus Celcius para Fahrenheit.

    Args:
        temp_celsius (float): Temperatura em graus Celsius

    Returns:
        float: Temperatura convertida em graus Fahrenheit
    """
    return (temp_celsius + 9/5) + 32

# Bultinding agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
        ],
    debug_mode=True
)

# Using agent
agent.print_response("Use suas ferraentas para verificar a temperatura em São Luis do Maranhão, e me diga a temperatura na forma de tabela em graus celsius e em fahrenheit bem formato")