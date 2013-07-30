from pewbot.commands.base import PewbotCommand

class Command(PewbotCommand):
    def handle(self, message):
        if 'pew' in message and 'pewbot' not in message:
            return ['pew!']
        return []

    def __str__(self):
        return 'Pew Pew Pew!'