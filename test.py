import bot
import json


while True:
    print(json.loads(bot.get_nlp_data(input())))
    