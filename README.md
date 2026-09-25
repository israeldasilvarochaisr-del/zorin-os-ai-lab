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
  -------------------------------------------*******----------------------------------------------------------
  israel@israel-VivoBook-ASUSLaptop-X540MAR-X540MAR:~$ ollama run
Error: requires at least 1 arg(s), only received 0
israel@israel-VivoBook-ASUSLaptop-X540MAR-X540MAR:~$ # 1. Para e desativa o serviço
sudo systemctl stop ollama
sudo systemctl disable ollama

# 2. Apaga os arquivos executáveis e de serviço
sudo rm -f /etc/systemd/system/ollama.service
sudo rm -f /usr/local/bin/ollama
sudo rm -f /usr/bin/ollama

# 3. Apaga os dados, modelos baixados e o usuário do serviço
sudo userdel ollama 2>/dev/null
sudo rm -rf /usr/share/ollama
rm -rf ~/.ollama
[sudo] senha para israel:       
Failed to stop ollama.service: Unit ollama.service not loaded.
Failed to disable unit: Unit file ollama.service does not exist.
israel@israel-VivoBook-ASUSLaptop-X540MAR-X540MAR:~$ curl -fsSL https://ollama.com/install.sh | sh
>>> Cleaning up old version at /usr/local/lib/ollama
>>> Installing ollama to /usr/local
>>> Downloading ollama-linux-amd64.tar.zst
######################################################################## 100.0%
>>> Creating ollama user...
[sudo] senha para israel:       
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
israel@israel-VivoBook-ASUSLaptop-X540MAR-X540MAR:~$ ollama run qwen2.5:0.5b
pulling manifest 
pulling c5396e06af29: 100% ▕▏ 397 MB/397 MB   18 MB/s      0s
verifying sha256 digest 
writing manifest 
success 
>>> Send a message (/? for help)
Resumo do markdown acima: ### 2. Instalação Nativa do Ollama e Execução do Modelo Qwen 2.5 (0.5B)

* **Objetivo:** Realizar a instalação limpa do Ollama no Zorin OS e executar um modelo de linguagem leve otimizado para execução offline via CPU.
* **Comandos de Limpeza e Instalação Executados:**
  ```bash
  # Limpeza de versões/serviços antigos
  sudo systemctl stop ollama
  sudo rm -f /usr/local/bin/ollama /usr/bin/ollama

  # Instalação nativa via script oficial
  curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh

  Saida de instalação: >>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.

 Download e execução de modelo: ollama run qwen2.5:0.5b
