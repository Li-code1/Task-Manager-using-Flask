FROM python:3.9-slim

RUN apt-get update && apt-get install -y rsyslog && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Injeta a pasta correta no mapeamento de módulos do Python
ENV PYTHONPATH=/app/todo_project

EXPOSE 5000

# Executa o arquivo usando o caminho absoluto mapeado na raiz /app
CMD ["python", "todo_project/todo_project/run.py"]