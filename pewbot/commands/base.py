
class PewbotMeta(type):
    def __repr__(self):
        if getattr(self, '__str__', False):
            return str(self)
        else:
            return self.__class__.__name__

class PewbotCommand(object):
    __metaclass__ = PewbotMeta
    help = ""

    def handle(self, message):
        return []

    def help(self):
        return self.help