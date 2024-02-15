from fastapi import FastAPI
from backend.model import TinyLlamaLLM

app = FastAPI()

model = TinyLlamaLLM()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chat")
def chat(usr_prompt: str = ''):
    print(usr_prompt)
    return model.generate_output(usr_prompt) 