import sys 
import os
import requests
import json
import urllib
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "1766275270:AAEtwSEQ7RIVCDQtLhpN-0kCxgb6IpOlJ-0"

def start(bot,update):
    try:

        username = update.message.from_user.username
        message = "Hola " + username
        update.message.reply_text(message)

    except Exception as e:
        print ("Error001: {}".format(error.args[0]))

def echo(bot,update):
    try:
        update.message.reply_text(update.message.text)

    except Exception as e:
        print ("Error002: "+type(e).__name__)

def help(bot,update):
    try:

        message = "Puedes enviar texto o imagenes"
        update.message.reply_text(message)

    except Exception as e:
        print ("Error003: "+type(e).__name__)

def getImage(bot,update):
    try:

        message = "Recibiendo imagen"
        update.message.reply_text(message)

        file = bot.getFile(update.message.photo[-1].file_id)
        id = file.file_id
            
        filename = os.path.join("src/","{}.jpg".format(id))

        file.download(filename)

        url = "https://8080-copper-quail-f7bqyrmp.ws-us03.gitpod.io/cheese"

        response = requests.post(url, myfile=filename)

        cheese =  response.json()
        
        x = json.loads(cheese)

        message = ["resultado"]

        update.message.reply_text(message)

    except Exception as e:
        print ("Error007: "+type(e).__name__)

def error (bot, update, error):
    try:

        print(error)

    except Exception as e:
        print ("Error004: "+type(e).__name__)


    
def main():
    try:
        token = "1766275270:AAEtwSEQ7RIVCDQtLhpN-0kCxgb6IpOlJ-0"

        updater = Updater(token)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_handler(MessageHandler(Filters.photo, getImage))

        dp.add_error_handler(error)

        updater.start_polling()
        updater.idle()

    except Exception as e:
        print ("Error005: "+type(e).__name__)
    
if __name__ == "__main__":
    try: 
        main()
    except Exception as e:
        print ("Error006: "+type(e).__name__)