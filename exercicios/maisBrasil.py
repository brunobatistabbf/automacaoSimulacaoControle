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

    def maisBrasil(self):
        self.get("https://voluntarias.plataformamaisbrasil.gov.br/voluntarias/Principal/Principal.do?Usr=guest&Pwd=guest")
        self.implicitly_wait(5)
        column = self.find_element(By.CLASS_NAME, "col1")
        convenio = column.find_elements(By.TAG_NAME, "div")[3]

        convenio.click()
        consultaConvenios = self.find_element(By.TAG_NAME, "li")
        consultaConvenios.click()

    def consultaConvenio(self):
        numeroConvenio = self.find_element(By.NAME, "numeroConvenio")
        submitConsulta = self.find_element(By.ID, "form_submit")

        numeroConvenio.send_keys("882885")
        submitConsulta.click()


bot = Principal()
bot.maisBrasil()
bot.consultaConvenio()