#!/usr/bin/env python
import pika,os,json
from dotenv import load_dotenv
from datetime import datetime
from uuid import uuid4
#variables de entorno
load_dotenv('.env')
rmq_user =os.getenv('RABBITMQ_USER')
rmq_pass =os.getenv('RABBITMQ_PASSWORD')
rmq_host =os.getenv('RABBITMQ_HOST')
rmq_port =os.getenv('RABBITMQ_PORT')

mensaje = {
    'id':str(uuid4()),
    'monto':1313.00,
    'tipo_pago':'envio',
    'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}
#Convertir a JSON
mensaje_json = json.dumps(mensaje)


#Nos conectamos al broker
credentials = pika.PlainCredentials(rmq_user,rmq_pass)
parameters = pika.ConnectionParameters(rmq_host, rmq_port, '/', credentials)
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