from pewbot.commands.base import PewbotCommand
import requests
import json

class Command(PewbotCommand):
    def handle(self, message):
        if message.startswith('pewbot pug me'):
            return [requests.get('https://pugme.herokuapp.com/random').json()['pug']]

    def __str__(self):
        return 'Pew Pew Pew!'