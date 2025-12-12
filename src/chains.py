from langchain_core.output_parsers import JsonOutputParser
from .chat_llm import chat_llm
from .chat_prompts import prompt1, chat_prompt

chain=(
    prompt1
    | chat_llm
    | JsonOutputParser()
)

chat_chain=(
    chat_prompt
    | chat_llm
    | JsonOutputParser()
)

