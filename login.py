import selenium
from selenium import webdriver
import logging
import config

#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common import keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://presbot.com/login/")
#click(), clear(), sendkeys(), submit()
driver.find_elements_by_xpath('//*[@id="id_username"]')[0].send_keys(config.username)
driver.find_elements_by_xpath('//*[@id="id_password"]')[0].send_keys(config.password)
driver.find_elements_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/div[1]/form/button')[0].submit()
text1 = driver.find_elements_by_xpath('//*[@id="link1"]/div/header/span')[0].text
if text1== "My Dashboard":
    print("Loged in user is navigating successfully to dashboard page")


