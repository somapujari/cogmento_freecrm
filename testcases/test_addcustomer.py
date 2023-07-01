import time
from pageobjects.loginfreecrm import Logincrm
from pageobjects.addcontacts import AddContacts
from utility.readpropertie import ReadConifig
from utility.loggeneration import Loggen


class Test_AddContact:
    base_url = ReadConifig.get_application_url()
    username = 'somapujari0@gmail.com'
    password = ReadConifig.getpassword()
    first_name = 'sonali'
    last_name = 'bendre'
    logger = Loggen.loggen()

    def test_addcontact(self, setup):
        self.logger.info('test_addcontact started ')
        self.driver = setup
        self.logger.info('opening url')
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lg = Logincrm(self.driver)
        self.logger.info('clicking login link ')
        self.lg.click_loginlink()
        self.logger.info('entering username')
        self.lg.username_enter(self.username)
        self.logger.info('entering password ')
        self.lg.password_enter(self.password)
        self.logger.info('clicking login')
        self.lg.click_login()
        self.logger.info('verifying login ')
        self.lg.verify_login()

        self.logger.info('creating addtocontact  object')
        self.ad = AddContacts(self.driver)
        self.driver.implicitly_wait(20)
        self.ad.contactadd_click()
        self.logger.info('entering firat_name')
        self.ad.first_name_enter(self.first_name)
        self.logger.info('entering last_name')
        self.ad.last_name_enter(self.last_name)
        self.logger.info('entering middle_name')
        self.ad.middle_name_enter('b')
        self.logger.info('enter company name')
        self.ad.company_enter('abc.pvt.ltd')
        # self.ad.tags_add('Business')
        self.logger.info('enter a email')
        self.ad.email_enter('vilas@gmail.com')
        self.logger.info('select category')
        self.ad.category_select('Customer')
        self.logger.info('select status ')
        self.ad.status_select('Active')

        self.ad.description_enter('new costumer')
        self.ad.time_zone("India")
        self.ad.street_address_enter('pune')
        self.ad.city_enter('pune')
        self.ad.state_enter('maharashtra')
        self.ad.post_enter('40000')
        self.ad.county_select('India')
        self.ad.phone_country_select()
        self.ad.phonenumber_enter('8805663333')
        self.ad.homephone_enter('4564564567')
        self.ad.position_enter('software test engg')
        self.ad.department_enter('IT')
        self.ad.supervisor_enter('Anita')
        self.ad.assistent_enter('vishal')
        self.ad.referedby_enter('vinod')
        self.ad.source_select('Google')
        self.ad.day_enter('2')
        self.ad.month_enter('March')
        self.logger.info('selecting  year')
        self.ad.year_select('2000')
        self.logger.info('clicking save button ')
        self.ad.save_click()
        time.sleep(3)
        print(self.ad.customer_verify())
        print(self.first_name + ' ' + self.last_name)

        self.logger.info('verifying the customer created ')
        if self.ad.customer_verify() == (self.first_name+' '+self.last_name):
            assert True
            self.logger.info('customer created')
            self.driver.save_screenshot('./screenshots/addcust_pass.png')
        else:
            self.logger.info('customer not created')
            self.driver.save_screenshot('./screenshots/addcust_fail.png')
            assert False
        self.logger.info('test_addtocontact is completed')
