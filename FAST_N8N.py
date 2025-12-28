#recibir mebsaje de whasat

import uvicorn as aplicacion
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 🔴 variable global (simple y válida para pruebas)
ultimo_mensaje = None

class MessageIn(BaseModel):
    output: str

# RECIBIR desde n8n / WhatsApp
@app.post("/from-n8n")
async def from_n8n(data: MessageIn):
    global ultimo_mensaje
    ultimo_mensaje = data.output
    print("Mensaje recibido:", ultimo_mensaje)
    return {"status": "ok"}

# LEER desde otra app
@app.get("/from-n8n")
async def obtener():
    return {
        "ultimo_mensaje": ultimo_mensaje
    }

if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True)




if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True) 