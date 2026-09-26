import time
import random

arquivo_log = "servidor_web.log"

ips = ["192.168.1.50", "10.0.0.15", "172.16.0.88", "203.0.113.5", "192.168.15.10"]
requisicoes = [
    '"GET /index.php HTTP/1.1" 200 1024',
    '"GET /contato.php HTTP/1.1" 200 850',
    '"GET /login.php?user=admin%27%20OR%20%271 HTTP/1.1" 200 4523',
    '"GET /../../../../etc/passwd HTTP/1.1" 404 230',
    '"GET /search.php?q=<script>alert(1)</script> HTTP/1.1" 200 1204'
]

print("📡 Simulador de Servidor Web Iniciado!")
print(f"Gravando logs no arquivo: {arquivo_log}")
print("Pressione Ctrl+C para parar.\n")

try:
    with open(arquivo_log, "a") as f:
        while True:
            ip = random.choice(ips)
            req = random.choice(requisicoes)
            data_hora = time.strftime("[%d/%b/%Y:%H:%M:%S]")
            f.write(f"{ip} - - {data_hora} {req}\n")
            f.flush()
            time.sleep(random.uniform(1, 4))
except KeyboardInterrupt:
    print("\n🛑 Simulador interrompido.")
