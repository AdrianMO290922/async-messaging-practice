# Imagen oficial de python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiar los directorios e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ ./src/