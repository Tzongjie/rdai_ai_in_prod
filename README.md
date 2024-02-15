# Install dependencies
- `pip install -r requirements.txt`


# Download model
- Download "TinyLlama-1.1B-Chat-v0.3-GPTQ" from https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ (main branch)
- Place it in the `backend` folder (E.g. ./backend/TinyLlama-1.1B-Chat-v0.3-GPTQ/)

# Run TinyLlama
## Run using FastAPI:
- `uvicorn main:app --reload`


## Run using Docker:
- `docker build -t chatbot-tinyllama .`
- `docker run -d --gpus all --name chatbot-tinyllama -p 8000:8000 chatbot-tinyllama`


# Test
- `Send a POST Request to localhost:8000/chat with the param: {'usr_prompt': "<insert prompt>"}` 