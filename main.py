# main.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Webhook Receiver is working!"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    payload = await request.json()
    print("🔔 Webhook Event Received:")
    print(payload)  # logs webhook payload
    return {"status": "received"}
