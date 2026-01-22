FROM python:3.11-slim

WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar os diretórios
COPY ./src ./src
COPY ./modelos ./modelos

# Garantir que o modelo seja treinado durante o build (opcional)
# Se você já tiver o .joblib, pode comentar a linha abaixo
RUN python src/treinar_modelo.py

# Porta da API
EXPOSE 8000

# Comando para rodar a aplicação apontando para a pasta src
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]