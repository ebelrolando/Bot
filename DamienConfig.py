import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1225254959:AAH6z_2KmkYRSSL6XFH9nKt5TFX8sjvD0Vo"
    APP_ID = "1266744"
    API_HASH = "f0db5ee8d1d0ec0ba1c288d11455529d"

class Messages():
      HELP_MSG = [
        ".",

        "**Hello 🌍 World**",
        
        "Another Text 😅",
        
        "**[👨‍💻](https://i.imgur.com/TaOKIkf.gif) Developed By : @AmineSoukara**"
      ]

      X_MSG = "Hey! [👋](https://i.imgur.com/Ljhp9Kk.gif) [{}](tg://user?id={}) \n©️ Read /help & /about"

      ABOUT_MSG = "©️ https://t.me/DamienSoukara"



