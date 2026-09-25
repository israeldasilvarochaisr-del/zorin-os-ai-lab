import json
import urllib.request

# Simulação de múltiplos logs recebidos pelo SOC N1
logs = [
    "Sep 25 10:15:30 server sshd[1234]: Failed password for invalid user admin from 192.168.1.50 port 44221 ssh2",
    "Sep 25 10:15:32 server sshd[1235]: Failed password for invalid user admin from 192.168.1.50 port 44222 ssh2",
    "Sep 25 10:15:35 server sshd[1236]: Failed password for invalid user admin from 192.168.1.50 port 44223 ssh2",
]

print(f"🚨 Alerta SOC: Detectadas {len(logs)} tentativas consecutivas de falha de login!")
print("🔍 Solicitando análise do modelo local (Qwen 1.5B)...")

prompt = (
    "Você é um analista SOC N1. Analise as tentativas abaixo e confirme se o comportamento caracteriza um ataque de Força Bruta (Brute Force).\n"
    f"Logs:\n" + "\n".join(logs)
)

url = "http://localhost:11434/api/generate"
payload = {"model": "qwen2.5:1.5b", "prompt": prompt, "stream": False}

try:
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        print("\n🛡️ Diagnóstico de Incidente:")
        print(res.get("response"))
except Exception as e:
    print(f"Erro: {e}")
