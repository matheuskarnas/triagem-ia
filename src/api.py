from fastapi import FastAPI
from pydantic import BaseModel
from src.classifier import TriageClassifier # Importação limpa

app = FastAPI()
# Instanciamos o classificador globalmente para carregar o modelo uma única vez
triage = TriageClassifier()

class Consulta(BaseModel):
    texto: str

@app.get("/")
def read_root():
    return {"status": "API de Triagem Online"}

@app.post("/predict")
def predict(consulta: Consulta):
    classe, score, recomendacao = triage.predict(consulta.texto)
    return {
        "paciente_relato": consulta.texto,
        "classificacao": classe,
        "confianca": score,
        "recomendacao": recomendacao
    }