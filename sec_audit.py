import sys
import os
import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5:1.5b"

SYSTEM_PROMPT = """Você é um especialista em cibersegurança e auditoria de código (Aegis Security Auditor).
Sua tarefa é analisar o arquivo fornecido e identificar:
1. Vulnerabilidades de segurança (ex: Injeção de código, senhas/chaves expostas, falhas de permissão).
2. Nível de severidade (BAIXO, MÉDIO, ALTO, CRÍTICO).
3. Sugestão prática de correção do código ou configuração.

Seja direto, técnico e estruture a resposta em Markdown."""

def auditar_arquivo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"[ERRO] Arquivo '{caminho_arquivo}' não encontrado.")
        sys.exit(1)

    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
        conteudo = f.read()

    print(f"==================================================")
    print(f"   AUDITANDO: {os.path.basename(caminho_arquivo)}")
    print(f"==================================================")
    print("Analisando com Qwen 2.5 (Aguarde...)...\n")

    prompt_final = f"{SYSTEM_PROMPT}\n\nConteúdo do Arquivo a ser Auditado:\n```\n{conteudo}\n```"

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_final,
        "stream": True
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=90)
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    dados = json.loads(line.decode('utf-8'))
                    print(dados.get("response", ""), end="", flush=True)
            print("\n\n==================================================")
            print("   AUDITORIA CONCLUÍDA")
            print("==================================================")
        else:
            print(f"[ERRO] Servidor Ollama respondeu com status: {response.status_code}")
    except Exception as e:
        print(f"[FALHA] Não foi possível comunicar com o Ollama: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python sec_audit.py <caminho_do_arquivo>")
        sys.exit(1)

    auditar_arquivo(sys.argv[1])
