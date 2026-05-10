from fastapi import FastAPI
from pydantic import BaseModel

from app.main import process

app = FastAPI()


class WebhookPayload(BaseModel):

    signal: str
    price: str
    vwma: str | None = None
    volume: str | None = None
    avg_volume: str | None = None
    symbol: str | None = None


@app.get("/")
async def root():

    return {
        "status": "running"
    }


@app.post("/webhook")
async def webhook(payload: WebhookPayload):

    data = payload.dict()

    process(data)

    return {
        "status": "success",
        "received": data
    }