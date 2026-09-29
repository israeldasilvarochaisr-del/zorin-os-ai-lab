import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

log_filename = f"logs/execucao_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("Iniciando o processamento do laboratório...")
logging.info("Executando tarefas do sistema...")
logging.info("Processamento finalizado com sucesso.")
