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
* **Saída Esperada:**
  ```text
  - IP de Origem: 192.168.1.50
  - Usuário: invalid user
  - Porta: 44221
  - Status: Falha de autenticação SSH# 🐧 Zorin OS & AI Local Lab (`zorin-os-ai-lab`)

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
* **Saída Esperada:**
  ```text
  - IP de Origem: 192.168.1.50
  - Usuário: invalid user
  - Porta: 44221
  - Status: Falha de autenticação SSH
