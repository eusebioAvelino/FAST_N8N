#recibir mebsaje de whasat

import uvicorn as aplicacion
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageIn(BaseModel):
    message: str

@app.post("/from-n8n")
async def from_n8n(data: MessageIn):
    print("Mensaje recibido desde n8n:", data.message)
    return {"status": "ok", "respuesta": f"Recibido: {data.message}"}



if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True) 