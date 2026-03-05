#!/bin/bash

CONTAINER_NAME="triagem-app"

echo "--- 🧹 Limpando Ambiente Docker ---"

# Para o container
echo "🛑 Parando container..."
docker stop $CONTAINER_NAME

# Remove o container
echo "🗑️  Removendo container..."
docker rm $CONTAINER_NAME

# Limpeza profunda (opcional, mas bom para liberar espaço)
# Remove imagens sem nome (dangling) que ficam sobrando após o build
echo "♻️  Limpando cache de imagens desnecessárias..."
docker image prune -f

echo "--- ✨ Tudo limpo! Até amanhã. ---"