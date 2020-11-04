#https://www.chris-wells.net/articles/2017/09/01/consistent-selenium-testing/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = 'https://www.merriam-webster.com/word-of-the-day'
driver.get(url)
wordpath = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/main/article/div[1]/div[2]/div[1]/div/h1')
word = wordpath.text
print(word)
driver.close()