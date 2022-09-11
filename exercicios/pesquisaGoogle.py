from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class Principal(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions().add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(ChromeDriverManager().install())
        super(Principal, self).__init__(service=service, options=options)
        self.maximize_window()

    def pesquisaGoogle(self):
        self.get('https://www.google.com')
        self.implicitly_wait(5)
        caixa_busca = self.find_element(By.NAME, 'q')
        caixa_busca.send_keys('Automação de Processos')
        caixa_busca.submit()



bot = Principal()
bot.pesquisaGoogle()