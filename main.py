from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

# 🔑 TOKEN DE VERIFICAÇÃO (tem que ser igual no META)
VERIFY_TOKEN = "colimix123"

# ✅ TESTE SE SERVIDOR ESTÁ ONLINE
@app.get("/")
def home():
    return {"status": "Assistente ativo"}

# ✅ ROTA QUE O META USA PARA VALIDAR WEBHOOK
@app.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Erro", status_code=403)

# ✅ RECEBER MENSAGENS DO WHATSAPP
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data)
    return JSONResponse({"status": "ok"})
