# 🐧 Zorin OS & AI Local Lab (`zorin-os-ai-lab`)

Este repositório registra o progresso prático em **Linux (Zorin OS)**, automação em **Python** e integração de **IA Local (Ollama - Qwen 2.5:1.5B)** para operações de **Cibersegurança e SOC N1**.

---

## 💻 Ambiente de Trabalho

* **Sistema Operativo:** Zorin OS (Linux)
* **Motor de IA:** Ollama (`qwen2.5:1.5b` executado 100% offline via CPU)
* **Análise de Logs Nativos:** Inspeção de `/var/log/syslog`, `/var/log/auth.log` e subsistema PAM
* **Foco:** Triagem de Incidentes, Detecção de OWASP Top 10, Automação em Python e Monitoramento Contínuo

---

## 🛠️ Módulos do Laboratório

### 1. `gerador_de_logs.py` (Simulador de Tráfego de Produção)
* **Função:** Gera fluxos contínuos de logs HTTP (Nginx/Apache), intercalando requisições legítimas e tentativas de ataque em tempo real.

### 2. `monitor_ia.py` (Agente SIEM & Triagem em Tempo Real)
* **Função:** Atua como um *daemon* de monitoramento (`tail -f` nativo em Python).
* **Engenharia de Prompt & Decodificação:** Decodifica parâmetros de URL (`urllib.parse.unquote`) eliminando Falsos Negativos antes do processamento pela IA.
* **Persistência:** Escreve laudos técnicos detalhados e carimbos de data/hora no registro de auditoria `alertas_soc.log`.

### 3. `analisador_web_sec.py` & `detector_brute_force.py` (Módulos de Triagem)
* **Função:** Motores de análise pontual e correlação de eventos sequenciais para ataques de Força Bruta e vulnerabilidades Web (SQLi, XSS, Path Traversal).

---

## 🔍 Auditoria Forense Local (Linux)
O laboratório engloba a identificação de eventos reais de autenticação do sistema via PAM (`kscreenlocker_greet` e `auth.log`), validando a captura de falhas de login físicas e remotas.
