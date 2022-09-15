# Telegram notification

This service is used to send notifications to Telegram channel via bot. Reads messages from RabbitMQ queue and sends them to Telegram channel.

The message in queue should be in JSON format:
```json
    {
        "chat_id": "123456789",
        "text": "Hello, world!"
    }
```

## Configuration

Configuration is taken from environment variables:

* `TG_NX_TOKEN`: Telegram bot token
* `TG_NX_CHAT_ID`: Telegram chat id

* `RMQ_HOST`: RabbitMQ host
* `RMQ_PORT`: RabbitMQ port
* `RMQ_USER`: RabbitMQ user
* `RMQ_PASSWORD`: RabbitMQ password
* `RMQ_EXCHANGE`: RabbitMQ exchange
* `RMQ_QUEUE`: RabbitMQ queue
* `RMQ_ROUTING_KEY`: RabbitMQ routing key