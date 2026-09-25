# 🐧 Zorin OS & AI Local Lab (`zorin-os-ai-lab`)

Este repositório regista o meu progresso prático em **Linux (Zorin OS)**, automação com **Python** e utilização de **IA Local (Ollama)** focada em tarefas de **Cibersegurança e SOC N1**.

---

## 💻 Ambiente de Trabalho
* **Sistema Operativo:** Zorin OS (Linux)
* **Ferramenta de IA:** Ollama (Instalação Nativa)
* **Modelo Principal:** `qwen2.5:0.5b` (Otimizado para execução local)
* **Foco:** Análise de Logs, Automação em Python e Fundamentos de Redes

---

## 📝 Registo de Comandos e Resolução de Problemas

### 1. Reinstalação Limpa e Execução Nativa do Ollama
* **Objetivo:** Limpar resíduos de instalações anteriores e garantir a execução nativa do Ollama no Linux.
* **Comandos Executados:**
  ```bash
  # Parar serviços antigos e remover ficheiros
  sudo systemctl stop ollama
  sudo rm -f /usr/local/bin/ollama /usr/bin/ollama
  rm -rf ~/.ollama

  # Reinstalação limpa via script oficial
  curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
