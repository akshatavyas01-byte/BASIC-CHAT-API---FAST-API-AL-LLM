from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
API=os.getenv('HUGGINGFACE_API')

llm=HuggingFaceEndpoint(
    model='meta-llama/Llama-3.2-1B-Instruct',
    huggingfacehub_api_token=API,
    max_new_tokens=200,
    temperature=0.2,
    top_k=1,
    top_p=0.5
)

chat_llm=ChatHuggingFace(llm=llm)


