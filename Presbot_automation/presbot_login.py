import logging
from selenium import webdriver
driver = webdriver.Firefox(
            executable_path="C:\\Users\\mbehera\\Desktop\\PROJECTS\\Automation\\DjangoSeleniumPython\\driver\\geckodriver.exe")

class LoginTests():

    def test_login(self):
        # FF browser command
        #driver = webdriver.Firefox(executable_path="C:\\Users\\mbehera\\Desktop\\PROJECTS\\Automation\\DjangoSeleniumPython\\driver\\geckodriver.exe")
        # Opens the url
        baseurl = "https://presbot.com"
        driver.get(baseurl)
        loginelement = driver.find_elements_by_xpath("/html/body/header/nav/div/div/ul/li[3]/a/span")
        # loginelement = driver.find_elements_by_link_text("Login")
        # loginelement.click()
        loginelement[0].click()
        user = driver.find_elements_by_id("id_username")
        user[0].click()
        user[0].send_keys("mukta.behera")
        pw = driver.find_elements_by_id("id_password")
        pw[0].send_keys("Qaz!1111")
        button = driver.find_elements_by_xpath("/html/body/header/div[1]/div/div[3]/div[2]/div/div/div[1]/form/button")
        button[0].click()
        driver.implicitly_wait(10)
        manageprofile = driver.find_elements_by_link_text("Manage Profile")
        manageprofile[0].click()
        currposition = driver.find_elements_by_xpath("/html/body/header/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div/div[2]/div/div/form/div[1]/div/div[1]")
        currposition[0].clear()
        currposition[0].send_keys("Senior Software QA Engineer")
        Headline = driver.find_elements_by_xpath("/html/body/header/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div/div[2]/div/div/form/div[2]/div/div[1]")
        Headline[0].clear()
        Headline[0].send_keys("I have over 10 years exp in Software Quality Assurance..")
        driver.implicitly_wait(10)
        summary = driver.find_elements_by_xpath("/html/body/header/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div/div[2]/div/div/form/div[3]/div/div[1]")
        print(summary)
        # summary.clear()
        # summary[0].send_keys("10+ years of experience in Quality Assurance, testing, requirements gathering and documentation. Extensive skill in Testing of Client Server and Web based applications..")
        # logging.info()

        save = driver.find_elements_by_id("Save")
        save[0].click()

log = LoginTests()
log.test_login()


