# Importing libs
from agno.models.groq import Groq
from agno.models.message import Message

# Setting up dot env
from dotenv import load_dotenv
load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")

user_msg = Message(
    role="user",
    content=[{"type": "text", "text": "Poderia me dizer como estão as noticias sobre a operação que ocorreu no rio de janeiro?"}]
)

assistant_msg = Message(
    role="assistant",
    content=[]
)

response = model.invoke([user_msg], assistant_msg)

print(response.content)