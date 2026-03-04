import requests
import json

# Lista de casos reais para validar a evolução
TEST_CASES = [
    {"texto": "Estou com dor forte no peito e braço dormente", "esperado": "URGENTE"},
    {"texto": "Sinto um aperto no coração e falta de ar", "esperado": "URGENTE"},
    {"texto": "Meu peito está coçando e vermelho", "esperado": "LEVE"},
    {"texto": "Quero marcar um exame de rotina", "esperado": "LEVE"},
    {"texto": "Estou com muita febre e dor de garganta", "esperado": "MODERADO"},
    {"texto": "Cortei o dedo com uma faca de cozinha", "esperado": "MODERADO"},
    {"texto": "Bati a cabeça e estou tonto", "esperado": "URGENTE"},
    {"texto": "Minha perna está inchada e dói ao andar", "esperado": "MODERADO"},
    {"texto": "Estou com uma mancha estranha nas costas", "esperado": "LEVE"},
    {"texto": "Não consigo mexer um lado do rosto", "esperado": "URGENTE"}
]

URL = "http://localhost:8000/predict"

def rodar_benchmark():
    print(f"{'RELATO':<50} | {'ESPERADO':<10} | {'OBTIDO':<10} | {'STATUS'}")
    print("-" * 85)
    
    acertos = 0
    for caso in TEST_CASES:
        try:
            res = requests.post(URL, json={"texto": caso["texto"]}).json()
            obtido = res["classificacao"]
            status = "✅" if obtido == caso["esperado"] else "❌"
            if status == "✅": acertos += 1
            
            print(f"{caso['texto'][:48]:<50} | {caso['esperado']:<10} | {obtido:<10} | {status}")
        except:
            print(f"Erro ao conectar na API para o caso: {caso['texto']}")

    print("-" * 85)
    print(f"Resultado Final: {acertos}/{len(TEST_CASES)} acertos ({(acertos/len(TEST_CASES))*100:.1f}%)")

if __name__ == "__main__":
    rodar_benchmark()