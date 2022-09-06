from telegram.ext import Updater
from config import read_config_from_env
import logging
import pika
import os
import json
import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


config = read_config_from_env()

updater = Updater(token=config['tg_bot_token'], use_context=True)

def callback(ch, method, properties, body):
    """Callback function"""
    logging.info(" [x] Received %r" % body)
    body = json.loads(body.replace(b"'", b'"'))
    message = f"Сегодня {body['days_since_first_meet']} дней с первой встречи или {body['days_since_first_meet'] * 24} часов или {body['days_since_first_meet']//7} недель"
    updater.bot.send_message(chat_id=config['chat_id'], text=message)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=config['host']))
    channel = connection.channel()
    channel.queue_declare(queue=config['queue'])
    channel.basic_consume(queue=config['queue'], on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
