from flask_socketio import emit

class Logger:
    def __init__(self, name, trigger=None) -> None:
        self.name = name
        self.trigger = trigger

    def print(self, *x, **kwargs):
        if self.trigger is not None:
            self.trigger({
                'type': 'print',
                'name': self.name,
                'args': x,
                'kwargs': kwargs
            })
            return
        emit('log_message',
             {'type': 'print', 'name': self.name, 'message': ' '.join(map(str, x)), 'kwargs': kwargs})

    def imshow(self, img):
        if self.trigger is not None:
            self.trigger({
                'type': 'imshow',
                'name': self.name,
                'args': img
            })
            return
        emit('log_message', {'type': 'imshow', 'name': self.name, 'image': img})

    @classmethod
    def get_logger(cls, name):
        logger = cls(name, trigger=Logger.global_trigger)
        cls.loggers.setdefault(id(logger), logger)
        return logger


Logger.loggers = {}
Logger.global_trigger = None
