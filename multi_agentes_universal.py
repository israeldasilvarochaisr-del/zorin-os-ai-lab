import json
import urllib.request
import time

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

def executar_comite_ia(entrada, agente1_cfg, agente2_cfg, agente3_cfg):
    print("="*60)
    print(f"🎯 ENTRADA / TEMA: {entrada}")
    print("="*60)
    
    # 1. Agente Explorador/Estruturador
    print(f"\n🧠 [AGENTE 1: {agente1_cfg['papel']}]")
    prompt1 = f"Você é um {agente1_cfg['papel']}. {agente1_cfg['instrucao']}\n\nEntrada: {entrada}"
    res1 = chamar_ollama(prompt1)
    print(res1)
    
    # 2. Agente Estrategista/Especialista
    print(f"\n💡 [AGENTE 2: {agente2_cfg['papel']}]")
    prompt2 = f"Você é um {agente2_cfg['papel']}. {agente2_cfg['instrucao']}\n\nCom base na análise do Agente 1:\n{res1}"
    res2 = chamar_ollama(prompt2)
    print(res2)
    
    # 3. Agente Auditor/Crítico
    print(f"\n🔍 [AGENTE 3: {agente3_cfg['papel']}]")
    prompt3 = f"Você é um {agente3_cfg['papel']}. {agente3_cfg['instrucao']}\n\nRevise e refine a proposta do Agente 2:\n{res2}"
    res3 = chamar_ollama(prompt3)
    print(res3)
    print("="*60 + "\n")

# --- EXEMPLO DE USO EM OUTROS DOMÍNIOS ---
if __name__ == "__main__":
    
    # EXEMPLO: Análise Financeira / Mercado
    print("🚀 EXECUTANDO COMITÊ MULTI-AGENTE: MÓDULO FINANCEIRO / NEGÓCIOS\n")
    
    tema_negocio = "Como estruturar uma reserva de emergência e transição de carreira para a área de Tecnologia/Cybersecurity?"
    
    agente_1 = {
        "papel": "Analista de Dados Financeiros",
        "instrucao": "Resuma os pontos principais do pedido e estruture os dados necessários em tópicos objetivos."
    }
    
    agente_2 = {
        "papel": "Estrategista de Carreira e Finanças",
        "instrucao": "Crie um plano prático de ação em 3 passos com foco em viabilidade e métricas reais."
    }
    
    agente_3 = {
        "papel": "Auditor de Riscos",
        "instrucao": "Aponte 2 riscos ocultos no plano e dê um parecer final direto de aprovação ou ajuste."
    }
    
    executar_comite_ia(tema_negocio, agente_1, agente_2, agente_3)
