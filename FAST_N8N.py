#recibir mebsaje de whasat

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn as aplicacion
app = FastAPI()

class Mensaje(BaseModel):
    texto: str

@app.post("/webhook/n8n")
async def recibir_mensaje(data: Mensaje):
    print("Texto recibido:", data.texto)
    return {
        "status": "ok",
        "recibido": data.texto
    }


if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True) 