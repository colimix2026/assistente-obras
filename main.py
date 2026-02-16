from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

VERIFY_TOKEN = "colimix123"

@app.get("/")
def home():
    return {"status": "Assistente ativo"}

# 🔥 ROTA QUE O META PRECISA
@app.get("/webhook")
from fastapi.responses import PlainTextResponse

VERIFY_TOKEN = "colimix123"

@app.get("/webhook")
@app.get("/webhook/")
async def verify_webhook(request: Request):
    p = request.query_params
    mode = p.get("hub.mode")
    token = (p.get("hub.verify_token") or "").strip()
    challenge = p.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Erro", status_code=403)

# RECEBER MENSAGENS
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print(data)
    return JSONResponse({"status": "ok"})
