from fastapi import FastAPI
from fastapi import Request

from app.main import process

app = FastAPI()


@app.get("/")
async def root():

    return {
        "status": "running"
    }


@app.post("/webhook")
async def webhook(request: Request):

    payload = await request.json()

    process(payload)

    return {
        "status": "success",
        "received": payload
    }