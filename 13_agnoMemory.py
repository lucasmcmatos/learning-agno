# Agent that uses custom tools and memory.

# Importing libs
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

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
    name="Agente do tempo",
    model=OpenAIChat(id="gpt-5-mini"),
    db=SqliteDb(db_file="tmp/agent.db"),
    tools=[
        TavilyTools(),
        celsius_to_fh,
        ],
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True
)

sid = "demo"

# Sync chat in terminal
if __name__ == "__main__":
    agent.cli_app(
        stream=False,
        markdown=True,
        exit_on=["/exit","/quit","/q"],
        session_id=sid
    )