'''DAY 2 — FastAPI + AI LLM (Basic Chat API)
Problem Statement:
Create your own ChatGPT-like chat API using FastAPI + OpenAI API.
Tasks:
 ✔ POST /chat endpoint
 ✔ User sends a message → model replies
 ✔ Add simple conversation memory (list)
'''
from fastapi import FastAPI,Path, Query
from .chains import chain, chat_chain
from .pydantic_model import Post_Question
from typing import Annotated
from dotenv import load_dotenv
import os 


Memory_list=[]
request_count=1
app=FastAPI()

@app.post('/chat')
async def chat(
    question: Post_Question
):   
    global Memory_list
    global request_count
    Question_text=question.Question
    if request_count==1:
        try:
            response=chain.invoke({"Question":Question_text})
            os.environ['Chat_memory_Flag']="True"
            Memory_list=[{"Question":Question_text,**response}]
            request_count+=1
            return response, Memory_list
        except Exception as e:
            return e
    else:
        try:
            response=chat_chain.invoke({"Question":Question_text,"Memory_list":Memory_list})
            Memory_list.append({"Question":Question_text,**response})
            request_count+=1
            return response, Memory_list
        except Exception as e:
            return e

    

