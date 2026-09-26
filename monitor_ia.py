import time
import json
import urllib.request
import urllib.parse

arquivo_log = "servidor_web.log"
arquivo_alertas = "alertas_soc.log" # ⬅️ NOVO: Arquivo onde os pareceres da IA serão salvos

def analisar_com_ia(linha_log):
    log_decodificado = urllib.parse.unquote(linha_log.strip())
    
    prompt = f"""Você é um analista SOC. Identifique a ameaça na linha de log abaixo.
Responda APENAS com:
- Tipo: [SQLi, XSS ou Path Traversal]
- IP Ofensor: [Extraia o IP]
- Ação: [Bloquear IP / Sanitizar Entrada]

Log: {log_decodificado}
"""
    
    url = "http://localhost:11434/api/generate"
    payload = {"model": "qwen2.5:1.5b", "prompt": prompt, "stream": False}
    
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            resposta_ia = res.get('response')
            
            # 1. Mostra na tela (Terminal)
            print(f"\n🚨 [ALERTA DE SEGURANÇA DETECTADO] 🚨\nLog Bruto: {linha_log.strip()}\n--- Parecer da IA ---\n{resposta_ia}\n{'-'*50}")
            
            # 2. GERA O LOG DA IA (Salva no arquivo)
            with open(arquivo_alertas, "a") as f_alerta:
                data_hora = time.strftime("[%d/%b/%Y:%H:%M:%S]")
                f_alerta.write(f"{data_hora} - INCIDENTE CONFIRMADO\n")
                f_alerta.write(f"Log Ofensor: {linha_log.strip()}\n")
                f_alerta.write(f"Diagnóstico Qwen:\n{resposta_ia}\n")
                f_alerta.write("="*50 + "\n")
                
    except Exception as e:
        print(f"Erro na IA: {e}")

print(f"👁️  Agente SOC Ativado! Monitorando '{arquivo_log}'...")
print(f"📁 Os laudos da IA serão salvos permanentemente em '{arquivo_alertas}'.\n")

with open(arquivo_log, "r") as f:
    f.seek(0, 2)
    while True:
        linha = f.readline()
        if not linha:
            time.sleep(1)
            continue
            
        if "index.php" not in linha and "contato.php" not in linha:
            analisar_com_ia(linha)
