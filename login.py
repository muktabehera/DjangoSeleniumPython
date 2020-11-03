import selenium
from selenium import webdriver
import logging

#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://presbot.com/login/")
#click(), clear(), sendkeys(), submit()
driver.find_elements_by_xpath('//*[@id="id_username"]')[0].send_keys("usernameisf")
driver.find_elements_by_xpath('//*[@id="id_password"]')[0].send_keys("jhg")
driver.find_elements_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/div[1]/form/button')[0].submit()



