import time
import unittest
import HtmlTestRunner
from selenium import webdriver


import sys
sys.path.append("/home/kanik/PycharmProjects/Selenium_tutorials/project_mail")
from Page_Object.Login_page import LoginPage
from Page_Object.send_mail import SendMail
from Page_Object.read_mail import ReadMail


class Task_test(unittest.TestCase):
    baseURL = "https://www.gmail.com"
    email = "vijay123456789ram@gmail.com"
    password = "Test_password"

    driver = webdriver.Chrome(executable_path="../Driver/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        time.sleep(2)
        login.setPassword(self.password)
        time.sleep(5)
        title = login.getTitle()
        self.assertEqual(title, self.driver.title, "Web Page title is not same")

    def test_sendMail(self):
        SendMail()

    def test_readMail(self):
        ReadMail()


    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/kanik/PycharmProjects/Selenium_tutorials/project_mail/Report/"))

