from telegram.ext import CommandHandler, MessageHandler, Filters 
from bot_token import token

### creating the updater and dispatcher
from telegram.ext import Updater
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher


### logging to see errors
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


########## start function ##########

## storing list of letters and dictionary into the bot_data
fn = 'meta_letters/Volume 1.txt'
with open(fn, 'r') as fo:
    vol1 = fo.read()
fn = 'meta_letters/Volume 2.txt'
with open(fn, 'r') as fo:
    vol2 = fo.read()

fn = 'all_letters/dict_0to10.json'
with open(fn, 'r') as fo:
    import json
    letters = json.load(fo)

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Starting! \nType '/help' to know the commands!")
    # store data
    context.bot_data['vol 1'] = vol1
    context.bot_data['vol 2'] = vol2
    context.bot_data['letters'] = letters


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

######### list letter names function #########
def list_letters(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = str(context.bot_data['vol 1']) )
    context.bot.send_message(chat_id = update.effective_chat.id, text = str(context.bot_data['vol 2']) )

list_handler = CommandHandler('list', list_letters)
dispatcher.add_handler(list_handler)

####### read a letter function #########
def read(update, context):
    key = update.message.text.partition(' ')[2]

    try:
        letter_to_read = context.bot_data['letters'][key]
        for l in letter_to_read:
            update.message.reply_text(l)

    except KeyError:
        update.message.reply_text("no such letter found")

read_handler = CommandHandler('read',read)
dispatcher.add_handler(read_handler)

def help(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "/list: list all the letters \n/read letter <number>: fetches the full letter")
help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
updater.idle()