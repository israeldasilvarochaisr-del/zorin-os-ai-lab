import json
import urllib.request

# Log de exemplo para triagem SOC
log_suspeito = "Sep 25 10:15:30 server sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 44221 ssh2"

# Prompt com exemplo (Few-Shot Prompting) para formatação estrita
prompt = (
    "Você é um parser técnico de logs de segurança. Extraia os dados do log seguindo estritamente o modelo de exemplo.\n\n"
    "--- EXEMPLO ---\n"
    "Log: 'Oct 01 12:00:00 server sshd[999]: Failed password for root from 10.0.0.1 port 22 ssh2'\n"
    "Resultado:\n"
    "- IP de Origem: 10.0.0.1\n"
    "- Usuário: root\n"
    "- Porta: 22\n"
    "- Status: Falha de autenticação SSH\n"
    "---------------\n\n"
    f"Analise este Log: '{log_suspeito}'\n"
    "Resultado:"
)

# Configuração apontando para o modelo Qwen 2.5 1.5B
url = "http://localhost:11434/api/generate"
payload = {
    "model": "qwen2.5:1.5b",
    "prompt": prompt,
    "stream": False
}

print("🔍 Enviando log para a IA local (Qwen 2.5 1.5B)...")

try:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    with urllib.request.urlopen(req) as response:
        resultado = json.loads(response.read().decode('utf-8'))
        print("\n🛡️ Parecer Estruturado (Qwen 1.5B):")
        print(resultado.get("response", "Nenhuma resposta gerada."))

except Exception as erro:
    print(f"❌ Falha ao conectar com o Ollama local: {erro}")
