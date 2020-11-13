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
        
        "**[👨‍💻](https://grouphelp.top/channel/api/beta/?file_id=AgACAgEAAxkBAAIrSV9yvE6VnQ9etRrWBUNPy07NoiegAAKVqTEbkLGYR-sHxxAbGYBQC-NuBgAEAQADAgADeQADb6AEAAEbBA.jpg) Desarrollado por : @AmineSoukara**"
      ]

      X_MSG = "Hola! [👋](https://i.ibb.co/FbJNC3b/botttt-jeva.jpg) [{}](tg://user?id={}) \n©️ Lee /help & /about"

      ABOUT_MSG = "©️ https://t.me/DamienSoukara"
      

 
