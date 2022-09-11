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

    def loginGuru(self):
        self.get('https://www.demo.guru99.com/test/newtours')
        usuario = self.find_element(By.NAME, "userName")
        senha = self.find_element(By.NAME, "password")
        submit = self.find_element(By.NAME, "submit")

        usuario.send_keys('mercury')
        senha.send_keys('mercury')
        submit.click()




bot = Principal()
bot.loginGuru()