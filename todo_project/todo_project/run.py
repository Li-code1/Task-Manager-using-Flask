import logging
from logging.handlers import SysLogHandler
from todo_project import app

# 1. Configuração Obrigatória do Syslog (Executada ANTES do servidor subir)
try:
    syslog_handler = SysLogHandler(address='/dev/log')
    syslog_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - TaskManager - %(levelname)s - %(message)s')
    syslog_handler.setFormatter(formatter)
    app.logger.addHandler(syslog_handler)
except Exception as e:
    # Fallback caso o ambiente de teste local não tenha o endpoint /dev/log
    logging.basicConfig(level=logging.INFO)
    app.logger.warning(f"Não foi possível conectar ao Syslog local (/dev/log): {e}. Usando log padrão.")

# 2. Inicialização do Servidor Flask
if __name__ == '__main__':
    # Apenas UM app.run com o host configurado para o Docker escutar externamente
    app.run(host='0.0.0.0', port=5000, debug=True)