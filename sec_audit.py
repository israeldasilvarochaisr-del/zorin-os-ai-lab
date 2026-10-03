import sys
import os
import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5:1.5b"

SYSTEM_PROMPT = """Você é um especialista em Cibersegurança e Auditoria de TI (Aegis Security System).
Sua função é analisar o arquivo fornecido e adaptar sua análise conforme a natureza do conteúdo:

1. SE O CONTEÚDO FOR UM SCAN DE REDE OU LOG (ex: Nmap, lista de portas, IPs, serviços):
   - Liste os IPs e portas identificadas como ABERTAS.
   - Analise os riscos associados aos serviços expostos (ex: HTTP, SSH, FTP, etc.).
   - Recomende ações práticas de fortalecimento de rede (Hardening / Regras de Firewall).

2. SE O CONTEÚDO FOR CÓDIGO-FONTE OU CONFIGURAÇÃO (ex: Python, Bash, C, XML, JSON):
   - Identifique vulnerabilidades de código (Injeção SQL, Chaves/Senhas expostas, falhas de permissão).
   - Classifique o Nível de Severidade (BAIXO, MÉDIO, ALTO, CRÍTICO).
   - Forneça o trecho de código corrigido.

Seja direto, altamente técnico e estruture sua resposta usando Markdown limpo."""

def auditar_arquivo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"[ERRO] O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)

    tamanho = os.path.getsize(caminho_arquivo)
    if tamanho == 0:
        print(f"[AVISO] O arquivo '{caminho_arquivo}' está VAZIO (0 bytes).")
        print("Gere a captura novamente garantindo que haja dados salvos.")
        sys.exit(1)

    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
        conteudo = f.read()

    print(f"==================================================")
    print(f"   AUDITANDO: {os.path.basename(caminho_arquivo)} ({tamanho} bytes)")
    print(f"==================================================")
    print("Analisando com Qwen 2.5 (Aguarde...)\n")

    prompt_final = f"{SYSTEM_PROMPT}\n\n[CONTEÚDO DO ARQUIVO PARA ANÁLISE]:\n```\n{conteudo}\n```"

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
