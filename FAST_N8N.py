from fastapi import FastAPI, Request
import uvicorn as aplicacion 

app = FastAPI()

@app.post("/n8n")
async def recibir_n8n(request: Request):
    data = await request.json()
    print("RECIBIDO:", data)
    return {
        "status": "ok",
        "total": len(data.get("items", []))
    }


if __name__ == "__main__":
    aplicacion.run("FAST_N8N:app", host="0.0.0.0", port=8000, reload=True) 