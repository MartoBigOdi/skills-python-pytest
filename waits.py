from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import utility.tools
import time


#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()

try:
    # tiempo de espera de ejecutar, para le ejecucion en esa linea.
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[text()='Add/Remove Elements']").click()
    # implicity wait cuando el DOM necesita tiempo para cargar.
    driver.implicitly_wait(3)
    buttonAdd = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    utility.tools.highlight(buttonAdd)
    # Frezamos el hilo de ejecucion
    wait = WebDriverWait(driver, 3)
    wait.until(EC.element_to_be_clickable(buttonAdd))


except Exception as e:
    print(e)

finally:
    driver.quit()