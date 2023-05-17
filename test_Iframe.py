from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
import utility.tools

#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

try:
    # localizamos el iframe
    # guardamos la ventana parent para movernos
    parent = driver.current_url
    iframe = driver.find_element(By.ID, "singleframe")
    utility.tools.highlight(iframe)
    time.sleep(2)
    # Moverse al Iframe con el index
    driver.switch_to.frame(0)
    # moverse con el name de la etiqueta
    #driver.switch_to.frame("singleframe")
    txt_iframe = driver.find_element(By.XPATH, "//h5[contains(text(),'iFrame Demo')]").text


    @pytest.mark.iframe
    def test_txtIframe():
        expected = "iFrame Demo"
        assert txt_iframe == expected

except Exception as e:
    print(e)

finally:
    driver.quit()