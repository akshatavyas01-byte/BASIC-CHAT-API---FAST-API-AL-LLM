from pydantic import BaseModel, Field

class Post_Question(BaseModel):
  Question:str=Field(title='Question',description='Question for the llm')