from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utility import tools
import time

# flag del flujo
pasa = False

#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

try:

    # Haacemos click para que se abra la nueva pestaña del navegador
    buttonNewWindows = driver.find_element(By.XPATH,"//button[contains(text(),'click')]")
    tools.highlight(buttonNewWindows)
    buttonNewWindows.click()
    time.sleep(2)
    parent = driver.current_window_handle
    # manejamos las ventanas en una lista
    windows = driver.window_handles
    # con el for pasamos de una ventana a otra
    for win in windows:
        if win is not parent:
            driver.switch_to.window(win)
            pasa = True

    # espera en la nueva ventana
    time.sleep(2)

    h1_nuevaVentana = driver.find_element(By.XPATH, "//*[contains(text(),'Selenium automates browsers')]")
    tools.highlight(h1_nuevaVentana)
    txt_h1 = h1_nuevaVentana.text

    def test_pasaTrue():
        assert pasa == True

    # falla para mostrar el error de la assertion, para hacerlo solo descomenta el primer str expected.
    def test_txt_h1():
       # expected = "New Windo"
        expected = "Selenium automates browsers. That's it!"
        assert txt_h1 == expected

finally:
  driver.quit()
