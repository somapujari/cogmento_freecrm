import time
from utility.loggeneration import Loggen
from pageobjects.loginfreecrm import Logincrm
from utility.readpropertie import ReadConifig


class Test_Login:
    base_url = ReadConifig.get_application_url()
    username = 'somapujari0@gmail.com'
    password = ReadConifig.getpassword()
    logger = Loggen.loggen()

    def test_login(self, setup):
        self.logger.info('test_login is started')
        self.driver = setup
        self.logger.info('opening url')
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lg = Logincrm(self.driver)
        self.logger.info('clicking on login link ')
        self.lg.click_loginlink()
        self.logger.info('entering usermame ')
        self.lg.username_enter(self.username)
        self.logger.info('entering a paswword')
        self.lg.password_enter(self.password)
        self.logger.info('clicking login submit button')
        self.lg.click_login()
        self.logger.info('verifing the title')
        act_title = self.driver.title
        if act_title == 'Cogmento CRM':
            assert True
            self.logger.info('assert true')
        else:
            self.logger.info('title is not matching ')
            assert False

        self.logger.info('test_login is completed ')
        time.sleep(5)


