from fastapi import FastAPI
from pydantic import BaseModel
from src.classifier import TriageClassifier # Importação limpa

app = FastAPI()
# Instanciamos o classificador globalmente para carregar o modelo uma única vez
triage = None # Começa vazio

@app.on_event("startup")
async def startup_event():
    global triage
    print("\n" + "="*50)
    print("🤖 CARREGANDO MODELO IA (BERTimbau)...")
    print("="*50)
    
    # A carga pesada acontece aqui dentro
    triage = TriageClassifier() 
    
    print("\n✅ IA CARREGADA COM SUCESSO!")
    print("🚀 API pronta para receber requisições na porta 8000.")
    print("="*50 + "\n")
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