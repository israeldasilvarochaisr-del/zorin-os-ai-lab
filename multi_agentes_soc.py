import json
import urllib.request
import urllib.parse
import time

# Função base para chamar a API REST local do Ollama
def chamar_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:1.5b",
        "prompt": prompt,
        "stream": False
    }
    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(payload).encode('utf-8'), 
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            return res.get("response", "").strip()
    except Exception as e:
        return f"Erro na conexão com Ollama: {e}"

# --- AGENTE 1: PARSER & TRIADOR ---
def agente_parser(log_bruto):
    log_decodificado = urllib.parse.unquote(log_bruto)
    prompt = f"""Você é o AGENTE 1 (Parser SOC). 
Sua única função é extrair e estruturar os dados do log abaixo.
Responda APENAS neste formato curto:
- IP: [IP extraído]
- Método: [GET/POST]
- Requisição: [Caminho e parâmetros]

Log: {log_decodificado}"""
    return chamar_ollama(prompt)

# --- AGENTE 2: ANALISTA DE AMEAÇAS (SOC N2) ---
def agente_analista(dados_estruturados):
    prompt = f"""Você é o AGENTE 2 (Analista de Cibersegurança SOC N2 especialista em OWASP Top 10).
Analise os dados estruturados abaixo fornecidos pelo Agente 1 e identifique a ameaça.

Responda APENAS neste formato:
- Status: [ATAQUE DETECTADO ou TRÁFEGO LEGÍTIMO]
- Categoria: [SQL Injection / XSS / Path Traversal / Nenhuma]
- Severidade: [Baixa / Média / Alta / Crítica]
- Justificativa: [1 frase explicando o vetor]

Dados do Agente 1:
{dados_estruturados}"""
    return chamar_ollama(prompt)

# --- AGENTE 3: ENGENHEIRO SOAR (RESPOSTA AUTOMÁTICA) ---
def agente_soar(analise_seguranca, ip_extraido):
    prompt = f"""Você é o AGENTE 3 (Engenheiro de Resposta a Incidentes SOAR).
Com base na análise de segurança fornecida pelo Agente 2, gere a ação de mitigação em Linux.

Se for um ataque de severidade Alta ou Crítica, forneça o comando 'sudo ufw deny from <IP>' para bloquear o ofensor.
Se for tráfego legítimo, responda "Nenhuma ação necessária".

Análise do Agente 2:
{analise_seguranca}
IP Ofensor: {ip_extraido}"""
    return chamar_ollama(prompt)

# --- ORQUESTRADOR MULTI-AGENTE ---
def executar_pipeline_multi_agente(log):
    print("="*60)
    print(f"📥 LOG RECEBIDO: {log}")
    print("="*60)
    
    # 1. Executa Agente 1
    print("\n🔍 [AGENTE 1: PARSER] Extraindo e estruturando dados...")
    dados_parsed = agente_parser(log)
    print(dados_parsed)
    
    # 2. Executa Agente 2
    print("\n🛡️ [AGENTE 2: ANALISTA SOC] Analisando vetores de ataque...")
    analise_ameaca = agente_analista(dados_parsed)
    print(analise_ameaca)
    
    # Extrai o IP de forma simples para o Agente 3
    ip = log.split()[0]
    
    # 3. Executa Agente 3
    print("\n⚡ [AGENTE 3: ENGENHEIRO SOAR] Gerando resposta a incidentes...")
    resposta_soar = agente_soar(analise_ameaca, ip)
    print(resposta_soar)
    print("="*60 + "\n")

# --- TESTE PRÁTICO ---
if __name__ == "__main__":
    logs_teste = [
        '192.168.15.10 - - [27/Sep/2026:10:00:01] "GET /login.php?user=admin%27%20OR%20%271%27=%271 HTTP/1.1" 200 4523',
        '10.0.0.55 - - [27/Sep/2026:10:01:15] "GET /produtos.php?cat=3 HTTP/1.1" 200 1200'
    ]
    
    print("🤖 SISTEMA MULTI-AGENTE LOCAL INICIADO (3 AGENTES IA)\n")
    for log in logs_teste:
        executar_pipeline_multi_agente(log)
        time.sleep(1)
