# Agent that learns about some especific file, in this case, uses a PDF File to learn.

# Setting up dot env
from dotenv import load_dotenv
load_dotenv()

# Import libs
import os
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.semantic import SemanticChunking
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType

db = SqliteDb(db_file="tmp/knowledge.db")

# Setting up Lance, the vector db
vector_db = LanceDb(
    table_name="pdf_agent",
    uri="tmp/lancedb",
    embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    search_type=SearchType.vector, 
)

# Setting up agent's knowledge
knowledge = Knowledge(
    name="EV Cars knowledge",
    description="Global informations about ev cars.",
    vector_db=vector_db,
    contents_db=db
)

# Adding content to knowledge
knowledge.add_content(
    name="UV Cars Informations",
    path="docs/GlobalEVOutlook2025.pdf",
    reader=PDFReader(chunk=True),
)

# Bultinding agent
agent = Agent(
    name="Agente de PDF",                # Naming the agent
    model=OpenAIChat(id="gpt-5-mini"),   # Setting up model

    db=db,                                # Setting up memory
    add_history_to_context=True,          # Setting up memory
    num_history_runs=3,                   # Setting up memory
    
    enable_user_memories=True,
    add_memories_to_context=True,
    
    knowledge=knowledge,                 # Setting up the knowledge
    add_knowledge_to_context=True,       # Setting up the knowledge
  
)

# Setting up session id
sid = "demo"

# Sync chat in terminal
if __name__ == "__main__":
    agent.cli_app(
        exit_on=["/exit","/quit","/q"],
        session_id=sid
    )