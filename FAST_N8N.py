#recibir mebsaje de whasat

import uvicorn as aplicacion
import logging
from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class Mensaje(BaseModel):
    texto: str

@app.post("/webhook/n8n")
async def recibir_mensaje(data: Mensaje):
    logger.info(f"📩 Texto recibido desde n8n: {data.texto}")
    return {
        "status": "ok",
        "recibido": data.texto
    }


if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True) 