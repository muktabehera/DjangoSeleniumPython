from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.get("https://www.github.com/")
driver.find_element_by_xpath("/html/body/div[4]/main/div[1]/div[1]/div/div/div[2]/div[1]/form/auto-check[1]/dl/dt/label")
driver.close()