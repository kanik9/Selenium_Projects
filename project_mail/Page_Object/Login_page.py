class LoginPage():
    id_email = "identifierId"
    xpath_email_next = "//*[@id='identifierNext']/div/button/div[2]"
    xpath_password = "//*[@id='password']/div[1]/div/div[1]/input"
    xpath_password_next = "//*[@id='passwordNext']/div/button/div[2]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.id_email).clear()
        self.driver.find_element_by_id(self.id_email).send_keys(email)
        self.driver.find_element_by_xpath(self.xpath_email_next).click()

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.xpath_password).clear()
        self.driver.find_element_by_xpath(self.xpath_password).send_keys(password)
        self.driver.find_element_by_xpath(self.xpath_password_next).click()

    def getTitle(self):
        return self.driver.title




