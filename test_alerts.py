from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utility import tools
import pytest
import time

#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

try:

    buttonAlert = driver.find_element(By.XPATH, "//button[@class='btn btn-danger']")
    tools.highlight(buttonAlert)
    buttonAlert.click()
    time.sleep(2)
    # aceptamos el alert importando la clase Alert
    Alert(driver).accept()
    # otra forma es directamente desde driver e ir ingresando a sus clases para buscar el metodo accept()
    # driver.switch_to.alert.accept()
    time.sleep(2)
    buttonAlert.click()
    # tambien podemos hascer dismiss() al alert
    Alert(driver).dismiss()
    time.sleep(2)
    buttonAlert.click()
    txt_alert = driver.switch_to.alert.text
    time.sleep(2)

    @pytest.mark.alert
    def test_buttonAlert():
        assert buttonAlert is not None

    @pytest.mark.alert
    def test_txt_alert():
        expected = "I am an alert box!"
        assert txt_alert == expected

except Exception as e:
    print(e)

finally:
  driver.quit()
