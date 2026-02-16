from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Assistente Financeiro Obras online"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data)

    # Aqui depois vamos colocar a lógica financeira
    return {"status": "ok"}
