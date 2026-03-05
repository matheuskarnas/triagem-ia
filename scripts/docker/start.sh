#!/bin/bash

# Nome das variáveis para facilitar manutenção
IMAGE_NAME="triagem-ia"
CONTAINER_NAME="triagem-app"

echo "--- 🛠️  Iniciando Setup do Docker ---"

# Para e remove container se ele já estiver rodando
docker stop $CONTAINER_NAME 2>/dev/null
docker rm $CONTAINER_NAME 2>/dev/null

# Build da imagem
echo "📦 Construindo imagem..."
docker build -t $IMAGE_NAME .

# Sobbe o container
echo "🚀 Subindo container na porta 8000..."
docker run -d -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME

echo "--- ✅ API Pronta! ---"
echo "Acompanhe o carregamento do BERT com: docker logs -f $CONTAINER_NAME"