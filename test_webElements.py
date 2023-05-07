import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utility import tools
import pytest


# config environment flag
pasa = False

#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

try:

    tools.highlight(driver.find_element(By.XPATH, '//*[@id="checkboxes"]'))
    checkBox1 = driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]")
    checkBox1.click()
    checkBox2 = driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[2]")
    checkBox2.click()
    tools.highlight(checkBox1)
    time.sleep(3)

    # guardamos en una lista los dos elementos para recorrerlos y hacer el click en ellos
    checkBoxes = [checkBox1, checkBox2]
    for check in checkBoxes:
     check.click()
     print(check.get_attribute('id'))
     tools.highlight(check)
     pasa = True
     print(check)


     @pytest.mark.front
     @pytest.mark.ejecutar
     # flow testing
     def test_flow():
         assert pasa == True

finally:
    driver.quit()





