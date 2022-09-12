from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import constants


driver = webdriver.Chrome()

driver.get("htpps://jquery.com/resources/demos/progressbr/download.html")
driver.implicitly_wait(5)
download =  driver.find_element(By.NAME, "downloadButton")

download.click()
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'progress-label'), 'Complete!')
)

progress_element = driver.find_element(By.CLASS_NAME, "progress-label")
print(f"{progress_element == 'Complete!'}")
driver.quit()