from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import utility.tools
from utility import tools
import time


#setting driver
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

try:
    # tiempo de espera de ejecutar, para le ejecucion en esa linea.
    time.sleep(2)
    buttonHome = driver.find_element(By.XPATH,"//a[contains(text(),'Hom')]")
    # implicity wait cuando el DOM necesita tiempo para cargar.
    driver.implicitly_wait(3)
    utility.tools.highlight(buttonHome)
    buttonHome.click()
    # Frezamos el hilo de ejecucion
    wait = WebDriverWait(driver, 3)
    # wait.until(EC.element_to_be_clickable(buttonHome))

finally:
    driver.quit()