FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

# Copia e instala requisitos primeiro (cache eficiente)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto mantendo a estrutura
COPY . .

# Expõe a porta
EXPOSE 8000

# Comando para rodar a API (agora apontando para src.api)
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]