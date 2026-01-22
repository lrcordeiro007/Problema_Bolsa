from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import time
import os

app = FastAPI(title="Mini Text Service", version="1.0.0")

# Caminho para o modelo
MODEL_PATH = "modelos/modelo_v1.joblib"

# Carregar o modelo se ele existir
if os.path.exists(MODEL_PATH):
    modelo = joblib.load(MODEL_PATH)
else:
    modelo = None

class ClassifyRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)

@app.post("/classify")
def classify(req: ClassifyRequest):
    if not modelo:
        raise HTTPException(status_code=500, detail="Modelo não encontrado. Execute o treino primeiro.")
    
    start = time.time()
    
    prediction = modelo.predict([req.text])[0]
    probs = modelo.predict_proba([req.text])[0]
    
    elapsed_ms = int((time.time() - start) * 1000)
    
    return {
        "category": str(prediction),
        "confidence": float(max(probs)),
        "elapsed_ms": elapsed_ms
    }

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": modelo is not None}