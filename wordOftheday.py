#https://www.chris-wells.net/articles/2017/09/01/consistent-selenium-testing/

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.merriam-webster.com/word-of-the-day')
wordpath = driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/main/article/div[1]/div[2]/div[1]/div/h1')
word = wordpath.text
print(word)
driver.close()
