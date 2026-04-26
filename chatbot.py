from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


#------------------------------------------------------- STEP 2 ---------------------------------------------------------------------------------------------
model = ChatOllama(
    model = "qwen2.5-coder:14b",
    temperature = 0.5
)

#------------------------------------------------------- STEP 3 -----------------------------------------------------------------------------------------------

#It is basically used to store the chat conversation in the field "history"
#Here memory is a normal Python list and it stores the messages as LangChain message objects.
#It is used to pass the old conversation into the prompt again and again.
#Example memory list 
# {
#     "history": [
#         HumanMessage(content="Hello"),
#         AIMessage(content="Hi there!")
#     ]
# }
memory = []






#---------------------------------------------------------  STEP 4 ----------------------------------------------------------------------------------------------
#Here ChatPromptTemplate is used so that we can reuse the prompt
#Here the MessagesPlaceholder is used because It tells that place/put the conversation into the key "history" and memory variable actually stores it. 
prompt = ChatPromptTemplate.from_messages([
    ("system","Consider yourself a expert and friendly assisstent.Your task is to Guid the user accordingly and in polite manner"),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}")
])





#-------------------------------------------------------------  STEP 5  ------------------------------------------------------------------------------------------
#Without this conversation chain we should connect the system prompt and model manually every time.
#Here prompt | model means the prompt output is directly passed into the model.
conversation = prompt | model






#-----------------------------------------------------------------  STEP 6  ---------------------------------------------------------------------------------------
def chatbotfunction(message):
    response = conversation.invoke({"history": memory, "input": message})
    memory.append(HumanMessage(content=message))
    memory.append(AIMessage(content=response.content))
    return response.content
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
