from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import peewee
import os, sys
import logging

def create_log(name: str, logfile) -> logging.getLogger:
    filename = filename=os.environ.get("LOGFILE", logfile)
    filename = os.path.join(os.getcwd(), filename[2:]).replace("\\", "/")
    criou = False
    if not os.path.isfile(filename):
        dir, name = os.path.split(filename)
        os.mkdir(dir)
        with open(filename, "w") as f:
            f.close()
            criou = True

    # import ipdb; ipdb.set_trace()
    formatter = "%(asctime)s | name:{0} | %(levelname)s | %(message)s".format(name)
    logging.basicConfig(
        format = formatter,
        datefmt = "%d-%m-%y %H:%M:%S",
        filename = filename,
        encoding = "utf-8",
        filemode = "a",
        level = int(os.environ.get("LOGLEVEL", logging.NOTSET)) 
        )
    
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(formatter)
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    
    log = logging.getLogger(name)
    if criou: log.info(f'Criado o arquivo de log no diretório: "{filename}"')
    return log


class BotWhatsApp(object):
    url_base = "https://web.whatsapp.com"

    def __init__(self, name: str, logfile="/log/BotWhatsApp.log") -> None:
        if os.environ.get("OS").lower() == "windows_nt":
            executable = "./webdriver/chromedriver.exe"
        else:
            executable = "./webdriver/chromedriver"


        self.log = create_log(name, logfile)
        
        filename = os.path.join(os.getcwd(), f"webdriver/Chrome/{name}")
        filename = filename.replace("\\", "/")
        options = Options()
        # import ipdb; ipdb.set_trace()
        options.add_argument(f"--user-data-dir=webdriver/Chrome/{name}")
        self.driver = webdriver.Chrome(executable_path=executable, chrome_options=options)
        self.driver.get("www.google.com")

    def login(self) -> None:
        pass
