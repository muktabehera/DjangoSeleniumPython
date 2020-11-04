#https://www.chris-wells.net/articles/2017/09/01/consistent-selenium-testing/

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://en.wikipedia.org/wiki/Main_Page')
search = driver.find_element_by_id('searchInput')
search.send_keys('python')
#search.submit()       #submitting using element

# button = driver.find_element_by_xpath('//*[@id="searchButton"]')
# button.click()       #submitting using click()

# search.send_keys(Keys.RETURN)   #submitting using RETURN

