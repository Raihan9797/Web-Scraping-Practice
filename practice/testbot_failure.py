from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("Starting")

def help(update, context):
    update.message.reply_text("I will help you")

def main():
    updater = Updater() # bot deleted

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle() 

if __name__=='__main__':
    main()