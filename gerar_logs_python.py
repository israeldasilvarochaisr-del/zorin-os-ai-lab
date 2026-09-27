import logging
import time
import random

# Arquivo onde os logs serão salvos
arquivo_saida = "aplicacao_python.log"

# Configuração do padrão de log nativo do Python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(arquivo_saida),  # Salva permanentemente no arquivo
        logging.StreamHandler()              # Exibe em tempo real na tela do terminal
    ]
)

logger = logging.getLogger("Modulo_SOC_Python")

print(f"🚀 Gerador de Logs Python Iniciado!")
print(f"📁 Os logs estão sendo salvos em '{arquivo_saida}'")
print("Pressione Ctrl+C para parar.\n")

# Lista de eventos simulados da aplicação
eventos = [
    (logger.info, "Sessão de usuário criada com sucesso (UID: 1000)."),
    (logger.info, "Requisição HTTP GET /api/v1/healthcheck finalizada [200 OK]."),
    (logger.warning, "Uso de memória da aplicação ultrapassou 75%."),
    (logger.warning, "Tentativa de login com senha incorreta registrada."),
    (logger.error, "Falha ao conectar com o serviço de banco de dados."),
    (logger.critical, "Tentativa de exploração de vulnerabilidade detectada na API!"),
]

try:
    while True:
        funcao_log, mensagem = random.choice(eventos)
        funcao_log(mensagem)
        time.sleep(random.uniform(1.5, 3)) # Gera um log a cada 1.5 a 3 segundos
except KeyboardInterrupt:
    print("\n🛑 Geração de logs encerrada pelo usuário.")
