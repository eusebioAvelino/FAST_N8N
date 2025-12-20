
import uvicorn as aplicacion 

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Job(BaseModel):
    title: str
    company: str
    link: str
    date: str

class JobsPayload(BaseModel):
    items: List[Job]

@app.post("/n8n")
async def recibir_n8n(payload: JobsPayload):
    return {
        "total": len(payload.items),
        "jobs": payload.items
    }

if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True) 