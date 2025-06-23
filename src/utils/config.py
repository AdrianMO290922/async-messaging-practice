from dotenv import load_dotenv
import os

load_dotenv('.env')

def load_rabbitmq_config():
    return {
        'user': os.getenv('RABBITMQ_USER'),
        'password': os.getenv('RABBITMQ_PASSWORD'),
        'host': os.getenv('RABBITMQ_HOST'),
        'port': int(os.getenv('RABBITMQ_PORT', 5672))
    }