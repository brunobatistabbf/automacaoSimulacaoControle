from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class Principal(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions().add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        super(Principal, self).__init__(service=service, options=options)
        self.maximize_window()

    def abrirFace(self):
        self.get('https://www.facebook.com')
        self.close()
        print("O titulo da aplicação é:", self.title)
        print("O endereço url é:", self.current_url)
        self.close()





bot = Principal()
bot.abrirFace()