from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def clear(text,element):
   for char in text:
       element.send_keys(Keys.BACK_SPACE)

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox(executable_path="")

searchtext = "helloworld"
driver.get("https://www.google.com/")
s = driver.find_element_by_name("q")
s.send_keys(searchtext)
# s.clear()

# for char in 'selenium':
#     s.send_keys(Keys.BACK_SPACE)


# def cleartext(text):
#     for char in text:
#         s.send_keys(Keys.BACK_SPACE)
#
# cleartext(searchtext)

clear(searchtext,s)