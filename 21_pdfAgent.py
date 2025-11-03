# Agent that open and listen PDFs content (they aren't connected to other tools)

# Import libs
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.openai import OpenAIEmbedder

from agno.vectordb.lancedb import LanceDb, SearchType

# Setting up vector db
vector_db = LanceDb(
    uri="tmp/lancedb",
    table_name="pdf_agent",
    search_type=SearchType.vector,
    embedder=OpenAIEmbedder(id="text-embedding-3-small")
)

# Setting up agent's knowledge
knowledge = Knowledge(
    name="My LanceDB Vector Database Knowledge Base",
    description="This is th knowledge that uses LanceDB as vector DB.",
    vector_db=vector_db,
)

knowledge.add_content(
    name="UV Cars Informations",
    path="./GlobalEVOutlook2025.pdf",
    metadata={"source":"IEA"}
)

# Setting up dot env
from dotenv import load_dotenv
load_dotenv()

# Bultinding agent
agent = Agent(
    name="Agente de PDF",
    model=OpenAIChat(id="gpt-5-mini"),
    db=SqliteDb(db_file="tmp/agent.db"),
    knowledge=knowledge,
    search_knowledge=True,
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
    
)

# Setting up session id
sid = "demo"

# Sync chat in terminal
if __name__ == "__main__":
    agent.cli_app(
        strem=True,
        markdown=True,
        exit_on=["/exit","/quit","/q"],
        session_id=sid
    )