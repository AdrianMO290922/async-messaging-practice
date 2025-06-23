import pika, sys, os
from utils.config import load_rabbitmq_config


def main():
    config = load_rabbitmq_config()
    #Nos conectamos al broker
    credentials = pika.PlainCredentials(config['user'], config['password'])
    parameters = pika.ConnectionParameters(
        host=config['host'],
        port=config['port'],
        credentials=credentials
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    #Buena práctica volver a declararla, para que no haya problemas en caso de que no se haya corrido el primero
    channel.queue_declare(queue = 'transaccion_pago')
    #Con esta función podremos recibir el mensaje 
    def callback(ch, method, properties,body):
        print(f"Recibido {body}")
    #Ahora debemmos de decir cual en partucular la funciónque queremos llamar
    print('Antes de consumir')
    channel.basic_consume(queue = 'transaccion_pago',
                        auto_ack = True,
                        on_message_callback = callback)
    #Después entraremos en un ciclo en lo que esperamoslos mensajes de la cola
    print('Esperando mensajes. Para salir presione CTRL+C')
    channel.start_consuming()
#El siguiente código es para que detecte errores y los maneje
if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)