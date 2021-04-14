#interface com o usuário
import os
from whatsapp.botwhatsapp import BotWhatsApp
os.environ["LOGLEVEL"] = "20"
os.environ["LOGFILE"] = "./logs/BotWhatsApp.log"
bot = BotWhatsApp("Danilo")