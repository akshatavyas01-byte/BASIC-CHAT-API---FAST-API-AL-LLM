# BASIC CHAT API - FAST API + AL LLM

A Basic Chat Bot API Built using FastAPI and HuggingFace model as  the second project in this learning series.

Added basic memory list to preserve the conversation.

---

## FEATURES
1. App Features:
    - Send query to POST 
    - Recieve response & the memory list

2. Langchain concepts:
    - Prompt Template
    - OutputParsers
    - LCEL
    
3. Langchain HuggingFace:
    - HuggingFaceEndpoint
    - ChatHuggingFace

4. FAST API
    - POST
    - Pydantic model
    - Auto docs (Swagger UI)

4.  Testing
    - POSTMAN
    - Swagger UI

---
## TECHNOLOGIES USED
    Python 3.x  
    Uvicorn  
    Pydantic  
    Langchain
    Langchain-core
    Langchain-community
    Langchain-HuggingFace

---
## FOLDER STRUCTURE

    project/
            |── src/
            |   |── main.py
            |   |── chains.py
            |   |── chat_llm.py
            |   |── chat_prompt.py
            |   └── pydantic_model.py
            |
            |── images/
            |
            |── requirements.txt
            |
            └── ReadMe.md


---

## Installation & Setup for the project

```python
git clone <your repo>
cd project-name

pip install -r requirements.txt

uvicorn src.main:app --reload

```
---
## Environment Setup
```python

python -m venv venv

venv/Scripts/Activate.ps1

```
## Install Dependencies
```python

pip install -r requirements.txt

```
---

## API Endpoints

| Method | Endpoint | Parameters| Description |
|---|---|---|---|
|POST|/chat| Body(JSON) | Sends a query & recieves answer as well as the pervious conversation list.

---
## Request Example
```json
{
"Question":"What is the capital of France?"
}
```

---

## Demo Images
### 1. Uvicorn:
![alt text](/images/uvi.png)

### 2. FAST API(SWAGGER DOCS):
![alt text](/images/fast1.png)
![alt text](/images/fast2.png)

### 3. Swagger UI Post Tryout:
![alt text](/images/swagger1.png)
![alt text](/images/swagger2.png)
![alt text](/images/swagger3.png)
![alt text](/images/swagger4.png)

### 4. PostMan post request:
![alt text](/images/postman.png)


---

## License
This project is licensed under the MIT License.

## Author
**Akshata Vyas**  
GitHub: [akshatavyas01-byte](https://github.com/akshatavyas01-byte)







