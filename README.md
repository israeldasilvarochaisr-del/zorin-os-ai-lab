# 🐧 Zorin OS & AI Local Lab (`zorin-os-ai-lab`)

Este repositório registra o meu progresso prático em **Linux (Zorin OS)**, automação com **Python** e utilização de **IA Local (Ollama)** focada em tarefas de **Cibersegurança e SOC N1**.

---

## 💻 Ambiente de Trabalho

* **Sistema Operativo:** Zorin OS (Linux)
* **Ferramenta de IA:** Ollama (Execução 100% Offline via CPU)
* **Modelo Principal:** `qwen2.5:1.5b` (Otimizado com Few-Shot Prompting)
* **Foco:** Análise de Logs, Automação em Python, SOC N1 e Cibersegurança Defensiva

---

## 🛠️ Módulos do Laboratório

### 1. `analisador_local.py` (Triagem Individual de Logs SSH)
* **Objetivo:** Consumir a API REST do Ollama (`127.0.0.1:11434`) sem dependências externas para analisar e estruturar falhas de login.
* **Técnica:** *Few-Shot Prompting* para garantir saída determinística sem adjetivos ou alucinações.

### 2. `detector_brute_force.py` (Detecção de Ataques de Força Bruta)
* **Objetivo:** Correlacionar múltiplos eventos sequenciais de falha de autenticação para identificar padrões de ataque sistemático.
* **Técnica:** Análise de contexto (intervalos curtos, repetição de IP e usuário).

### 3. `analisador_web_sec.py` (Triagem de Logs Web / OWASP)
* **Objetivo:** Inspecionar requisições HTTP (Nginx/Apache) para identificar vetores de ataque web comuns.
* **Ameaças Detectadas:** SQL Injection (SQLi), Cross-Site Scripting (XSS) e Directory/Path Traversal.
* **Técnica Avançada:** Pré-processamento em Python (Decodificação de URL com `urllib.parse.unquote`) combinado com *Few-Shot Prompting* para eliminar **Falsos Negativos** na detecção da IA.

---

## 🔐 Compliance & Segurança (LGPD)

* **Privacidade Total:** Processamento local sem envio de logs ou IPs internos para APIs na nuvem.
* **Código Nativo:** Desenvolvido puramente em Python (`urllib.request` e `json`), reduzindo a superfície de ataque por dependências de terceiros.
