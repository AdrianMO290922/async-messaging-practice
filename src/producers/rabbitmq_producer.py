#!/usr/bin/env python
import pika,os,json
from datetime import datetime
from uuid import uuid4
from utils.config import load_rabbitmq_config

# Cargar la configuración de RabbitMQ desde el archivo .env
config = load_rabbitmq_config()

mensaje = {
    'id':str(uuid4()),
    'monto':1313.00,
    'tipo_pago':'envio',
    'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}
#Convertir a JSON
mensaje_json = json.dumps(mensaje)


#Nos conectamos al broker
credentials = pika.PlainCredentials(config['user'],config['password'])
parameters = pika.ConnectionParameters(
    config['host'],
    config['port'], '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
#Mandamos el mensaje
channel.queue_declare(queue='transaccion_pago_2')
#Nunca se mandan directo, necesita pasar por el extchange
channel.basic_publish(exchange='',
                      routing_key = 'transaccion_pago_2',
                      body = mensaje_json)
print("Su transaccion ha sido enviado")
connection.close()

#if __name__ == '__main__':
    #send_payment_message()