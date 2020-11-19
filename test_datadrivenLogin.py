import selenium
from selenium import webdriver
import pytest

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# @pytest.fixture()
# def setup():

userlist1 = [
   {
      "username":"test02",
      "password":"Qaz!1111"
   },
   {
      "username":"test03",
      "password":"Qaz!1111"
   },
   {
      "username":"test04",
      "password":"Qaz!1111"
   }
]

def test_login():
    for x in range(0, len(userlist1)):
        driver.get("https://presbot.com/login/")
        driver.maximize_window()
        print(x)
        driver.find_elements_by_xpath('//*[@id="id_username"]')[0].send_keys(userlist1[x]['username'])
        driver.find_elements_by_xpath('//*[@id="id_password"]')[0].send_keys(userlist1[x]['password'])
        driver.find_elements_by_xpath('/html/body/header/div[1]/div/div/div[2]/div/div/div[1]/form/button')[0].submit()
        print(f"completed login for {userlist1[x]['username']}")
        driver.implicitly_wait(5)


test_login()