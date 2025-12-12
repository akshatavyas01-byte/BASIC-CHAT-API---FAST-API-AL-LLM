from langchain_core.prompts import PromptTemplate
prompt_template='''
You are a helpful assiatance.
Task: Answer the following Question in JSON fromat.
Output Example:
{{
"Answer":"Delhi is the capital of India."
}}

Question:
{Question}
'''

prompt1=PromptTemplate(template=prompt_template,input_variables=['Question'])

chat_prompt_template='''
You are a helpful assiatance.
Task: Answer the following Question in JSON fromat.
Note:While taking the perivous conversation into consideration don't let it affect the original answer.The output returned should only answer the question sent now.
Output Example:
{{
"Answer":"Delhi is the capital of India."
}}

Question:
{Question}

Consider Information:
{Memory_list}
'''

chat_prompt=PromptTemplate(template=chat_prompt_template,input_variables=['Question','Memory_list'])