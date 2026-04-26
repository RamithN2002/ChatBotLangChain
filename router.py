from fastapi import APIRouter
from pydantic import BaseModel
from chatbot import chatbotfunction

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

router = APIRouter()

# Here response_model=ChatResponse validates the returned payload.
@router.post("/chat", response_model=ChatResponse)
def chatendpoint(request: ChatRequest):
    response = chatbotfunction(request.message)
    return ChatResponse(reply=response)
