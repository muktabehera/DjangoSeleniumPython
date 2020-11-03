import selenium
from selenium import webdriver
import logging

#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import keys


driver = webdriver.Chrome(ChromeDriverManager().install())
# logging.info(f"{type(driver)}")
driver.get("https://presbot.com/login/")
username = driver.find_elements_by_xpath('//*[@id="id_username"]')[0].send_keys("usernameisf")
print(f"{username}")

password = driver.find_elements_by_xpath('//*[@id="id_password"]')[0].send_keys("jhg")
print(f"{password}")

#click(), clear(), sendkeys(), submit()

##


