#!/bin/bash
echo "🚀 Configurando o ambiente do AI Lab..."

sudo apt update && sudo apt install -y python3 git curl

if ! command -v ollama &> /dev/null; then
    echo "📦 Instalando Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

echo "🧠 Garantindo o modelo Qwen 2.5:1.5B..."
ollama pull qwen2.5:1.5b

echo "✅ Configuração concluída com sucesso!"
