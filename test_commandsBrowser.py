from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
    driver.get("https://demo.automationtesting.in/Index.html")
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.refresh()
    time.sleep(3)
    currentUrl = driver.current_url


    @pytest.mark.current_url
    # validamos que la current url sea la esperada
    def test_first_url():
        expected = "https://demo.automationtesting.in/Register.html"
        assert currentUrl == expected


finally:
    driver.quit()