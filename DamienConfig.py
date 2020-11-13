import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1352432671:AAEzHRx-4F08H2Ja7CjFxnY7MStkB4fQG5Y"
    APP_ID = "2190647"
    API_HASH = "c9bec948217c0eae66f8f85e0e48d881"

class Messages():
      HELP_MSG = [
        ".",

        "**Hola mundo**",
        
        "Otro texto 😅",
        
        "**[👨‍💻](https://i.imgur.com/TaOKIkf.gif) Desarrollado por : @AmineSoukara**"
      ]

      X_MSG = "Hey! [👋](https://i.imgur.com/Ljhp9Kk.gif) [{}](tg://user?id={}) \n©️ Read /help & /about"

      ABOUT_MSG = "©️ https://t.me/DamienSoukara"
      
      
    def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1352432671:AAEzHRx-4F08H2Ja7CjFxnY7MStkB4fQG5Y", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pizza))

        def pizza(update, context): > 
        if (update.message.reply.text_upper().find("MANZANAS VERDES") > 0 ):
             update.message.reply_text("Prefiero comer pizza")
            
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
  
      
      
      
