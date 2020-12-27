import pika, json

params = pika.URLParameters('amqps://ktjontbf:CWDWCU4NbBH584bgh7VjDgCAPsw8KgE7@finch.rmq.cloudamqp.com/ktjontbf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    #properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body='HEloo')#, properties=properties)