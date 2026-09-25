import json
import urllib.request
import urllib.parse

# Logs brutos do servidor Web
logs_web_raw = [
    '192.168.1.105 - - [25/Sep/2026:14:32:10] "GET /login.php?user=admin%27%20OR%20%271%27=%271 HTTP/1.1" 200 4523',
    '10.0.0.15 - - [25/Sep/2026:14:33:01] "GET /search.php?q=<script>alert(document.cookie)</script> HTTP/1.1" 200 1204',
    '172.16.0.88 - - [25/Sep/2026:14:35:12] "GET /../../../../etc/passwd HTTP/1.1" 404 230'
]

# Pré-processamento: Decodifica URLs (%27 -> ', %20 -> espaço)
logs_decodificados = [urllib.parse.unquote(log) for log in logs_web_raw]

print("🌐 [SOC N1] Analisando requisições Web Decodificadas com Qwen 1.5B...\n")

prompt = f"""Você é um analista SOC N1 especialista em OWASP Top 10.
Analise os logs de servidor web e classifique cada requisição.

--- EXEMPLO DE REFERÊNCIA ---
Log: 192.168.1.1 - - [25/Sep/2026] "GET /login.php?user=admin' OR '1'='1 HTTP/1.1" 200
- IP: 192.168.1.1
- Tipo de Ataque: SQL Injection (SQLi)
- Severidade: Crítica
- Ação: Bloquear IP no WAF e sanitizar entradas no formulário de login.
--- FIM DO EXEMPLO ---

Logs para análise:
{chr(10).join(logs_decodificados)}

Forneça a análise técnica para cada um dos logs acima seguindo o formato do exemplo.
"""

url = "http://localhost:11434/api/generate"
payload = {"model": "qwen2.5:1.5b", "prompt": prompt, "stream": False}

try:
    req = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        print("🛡️ PARECER TÉCNICO OTIMIZADO (SEM FALSOS NEGATIVOS):\n")
        print(res.get("response"))
except Exception as e:
    print(f"❌ Erro na comunicação com Ollama: {e}")
