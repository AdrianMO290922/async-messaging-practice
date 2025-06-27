# Imagen oficial de python
FROM python:3.12-slim

# Directorio de trabajo, este se crea al momento de construir la imagen, propia de docker
WORKDIR /app

# Copiar los directorios e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente, lo copea de la dirección actual al la del directorio de trabajo
COPY src/ ./src/
# Comando por defecto (puedes sobrescribirlo al ejecutar)
CMD ["python", "./src/producer/rabbitmq_producer.py"]