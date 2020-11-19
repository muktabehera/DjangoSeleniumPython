import selenium
from selenium import webdriver
import pytest
import csv

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# @pytest.fixture()
# def setup():
def readcsv():

    userdata = list()
    # open and read csv and populate list
    datafile = open("presbotlogin.csv", "r")
    reader = csv.reader(datafile)
    next(reader)
    for row in reader:
        # ['test02', 'Qaz!1111']
        # {'username': 'test02', "password": 'Qaz!1111'}
        new_row = {'username': row[0], 'password': row[1]}

        userdata.append(new_row)

    return userdata # list of dicts


# readcsv()

def test_login():
    userlist1 = readcsv()
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