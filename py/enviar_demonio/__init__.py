import pika
from json import dumps,loads
from os import getpid
class Cola_mensajes(object):
    def __init__(self):

        credentials = pika.PlainCredentials('test', 'test')
        parameters = pika.ConnectionParameters('200.14.84.16',
                                               5672,
                                               '/',
                                               credentials)
        self.connection = pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = loads(body)

    def enviar(self,data):
        self.response = None
        self.corr_id = str(getpid())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id ,
                                         ),
                                   body=dumps(data))
        while self.response is None:
            self.connection.process_data_events()
        return self.response