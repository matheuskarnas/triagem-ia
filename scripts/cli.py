import requests

def main():
    print("=== Sistema de Triagem IA - Terminal Mode ===")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        texto = input("Relato do Paciente: ")
        if texto.lower() == 'sair':
            break
            
        try:
            response = requests.post("http://localhost:8000/predict", json={"texto": texto})
            data = response.json()
            
            print(f"\n--- Resultado ---")
            print(f"Classificação: {data['classificacao']}")
            print(f"Confiança: {data['confianca']:.2f}")
            print(f"Recomendação: {data['recomendacao']}")
            print("-" * 20 + "\n")
        except Exception as e:
            print(f"Erro: Verifique se o Docker está rodando a API na porta 8000.")

if __name__ == "__main__":
    main()