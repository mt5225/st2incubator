from socketIO_client import SocketIO, LoggingNamespace
from st2actions.runners.pythonrunner import Action


class PostMessageAction(Action):
    def __init__(self, config):
        super(PostMessageAction, self).__init__(config=config)

    def run(self, **kwargs):
        self.logger.info(kwargs)

        # get socketio server info from configuration
        config = self.config['socketio']

        # get message from parameter
        message = kwargs['socketio_message']

        #send message to socketio server
        try:
            with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
                socketIO.emit(config['topic'], message)
            return "socket.io message sent success"
        except Exception, e:
            raise e
