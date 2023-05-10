from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import utility.tools
import pytest


# setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Register.html")
driver.implicitly_wait(2)
driver.maximize_window()


try:
    buttonSubMit = driver.find_element(By.XPATH, "//button[@value='sign up']")
    driver.execute_script('window.scrollBy(0, 1500)')
    utility.tools.highlight(buttonSubMit)
    # con actions tambien podemos enviar keys a un input por ejemplo
    # a.move_to_element(buttonSubMit).send_keys("password").perform()
    a = ActionChains(driver)
    a.move_to_element(buttonSubMit).perform()
    txtButton = buttonSubMit.text
    time.sleep(2)


    @pytest.mark.hover
    def test_hover_button():
        expected = "Submit"
        assert txtButton == expected

finally:
    driver.quit()
