from selenium.webdriver.common.by import By


class Logincrm:
    login_lnk_xpath = (By.XPATH,"//span[contains(text(),'Log In')]")
    email_inp_name = (By.NAME, 'email')
    password_inp_name = (By.NAME, 'password')
    login_btn_inp_xpath = (By.XPATH,"//div[contains(text(),'Login')]")

    def __init__(self, driver):
        self.driver = driver

    def click_loginlink(self):
        self.driver.find_element(*Logincrm.login_lnk_xpath).click()

    def username_enter(self, username):
        self.driver.find_element(*Logincrm.email_inp_name).clear()
        self.driver.find_element(*Logincrm.email_inp_name).send_keys(username)

    def password_enter(self,password):
        self.driver.find_element(*Logincrm.password_inp_name).clear()
        self.driver.find_element(*Logincrm.password_inp_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Logincrm.login_btn_inp_xpath).click()

    def verify_login(self):
        act_title = self.driver.title
        if act_title == 'Cogmento CRM':
            assert True
        else:
            self.driver.seve_screenshot('./screenshots/login.png')
            assert False

