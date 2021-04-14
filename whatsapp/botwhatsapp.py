from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import peewee
import os, sys
import logging

def create_log(name: str, logfile) -> logging.getLogger:
    filename = filename=os.environ.get("LOGFILE", logfile)
    filename = os.path.join(os.getcwd(), filename[2:]).replace("\\", "/")

    if not os.path.isfile(filename):
        dir, name = os.path.split(filename)
        os.mkdir(dir)
        with open(filename, "w") as f:
            f.close()

    # import ipdb; ipdb.set_trace()
    logging.basicConfig(
        format = "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt = "%d-%m-%y %H:%M:%S",
        filename = filename,
        encoding = "utf-8",
        filemode = "a",
        level = int(os.environ.get("LOGLEVEL", logging.NOTSET)) 
        )
    
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    
    log = logging.getLogger(name)
    log.info(f'Criado o arquivo de log no diretório: "{filename}"')
    return log


class BotWhatsApp(object):
    url_base = "https://web.whatsapp.com"

    def __init__(self, name: str, logfile="/log/BotWhatsApp.log") -> None:
        self.log = create_log(name, logfile)


    def login(self) -> None:
        pass
