from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

VERIFY_TOKEN = "colimix123"

@app.get("/")
def home():
    return {"status": "Assistente ativo"}

# 🔥 ROTA QUE O META PRECISA
@app.get("/webhook")
async def verify_webhook(request: Request):
    params = dict(request.query_params)
    
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return PlainTextResponse(params.get("hub.challenge"))

    return PlainTextResponse("Erro de verificação", status_code=403)

# RECEBER MENSAGENS
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print(data)
    return JSONResponse({"status": "ok"})
