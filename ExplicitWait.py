from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.google.com/")
# WebDriverWait(driver,5).until(ec.presence_of_element_located((By.ID, "hptl" )))
# driver.close()

driver.get("http://www.webcountdown.net/?c=3") # Starts a 3 second timer.
# if WebDriverWait(driver,4).until(ec.presence_of_element_located((By.ID,"popupiframe"))):
#     print("Pop up opened successfully")
wait = WebDriverWait(driver,4)
element = wait.until(ec.presence_of_element_located((By.ID,"popupiframe")))
print("Pop up opened successfully")



