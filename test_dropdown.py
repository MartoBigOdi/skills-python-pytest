from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from utility import tools
import pytest
import time


#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

try:
   select_dropdown = driver.find_element(By.XPATH,'//*[@id="Skills"]')
   tools.highlight(select_dropdown)
   sel = Select(select_dropdown)
   # select by index
   sel.select_by_index(1)
   tools.highlight(select_dropdown)
   time.sleep(3)
   # select by valur
   sel.select_by_value("Android")
   tools.highlight(select_dropdown)
   time.sleep(3)
   # select by visible text
   sel.select_by_index(7)
   tools.highlight(select_dropdown)



   @pytest.mark.dropdown
   # validamos que el objeto no venga None
   def test_dropdown():
       assert select_dropdown is not None


except Exception as e:
    print(e)

finally:
    driver.quit()