from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

try:
    buttonHome = driver.find_element(By.XPATH, "//a[contains(text(),'Hom')]")
    buttonHome.click()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    currentUrl = driver.current_url
    driver.refresh()
    time.sleep(3)

    @pytest.mark.current_url
    # validamos que la current url sea la esperada
    def test_first_url():
        expected = "https://demo.automationtesting.in/Register.html"
        assert currentUrl == expected


except Exception as e:
    print(e)

finally:
    driver.quit()