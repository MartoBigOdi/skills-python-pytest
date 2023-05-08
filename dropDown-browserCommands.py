from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utility import tools
import pytest


#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

try:
   select = driver.find_element(By.XPATH,'//*[@id="dropdown"]')
   tools.highlight(select)
   print("Cerrando Browser")


   @pytest.mark.ejecutar
   def test_selectElementTrue():
       assert select != None

finally:
    driver.quit()