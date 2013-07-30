from pewbot.commands.base import PewbotCommand

class Command(PewbotCommand):
    help = "Say pew again, I dare you!"
    def handle(self, message):
        if 'pew' in message and 'pewbot' not in message:
            return ['pew!']
