from fastapi import FastAPI
from router import router as chatbotrouter
import uvicorn

app = FastAPI(title="LangChain Chatbot API")

#It will include all the router included in the router folder
app.include_router(chatbotrouter)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
