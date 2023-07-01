from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddContacts:
    contactsadd_btn_xpath = (By.XPATH, "//span[contains(text(),'Contacts')]/ancestor::div[4]/div/div/div[3]/button/i")
    first_name_inp_name = (By.NAME, 'first_name')
    last_name_inp_xpath = (By.XPATH, "//input[@name='last_name']")
    middle_name_inp_Xpath = (By.XPATH, "//input[@name='middle_name']")
    company_inp_xpath = (By.XPATH, "//div[@name='company']//input[@type='text']")
    tags_box_xpath = (By.XPATH, "//div[@class='ui fluid multiple search selection dropdown']/input")
    tag_active_xpath = (By.XPATH, "//div[@class='selected item addition']//span[@class='text']")
    email_inp_xpath = (By.XPATH, "//input[@placeholder='Email address']")
    category_xpath = (By.XPATH, "//div[@name='category' and @role='listbox']")
    # categories_xpath = (By.XPATH, "//div[@name='category' and @role='listbox']/div/div/span")
    lead_sel_xpath = (By.XPATH, "//div[@name='category' and @role='listbox']/div/div[2]")
    customer_sel_xpath = (By.XPATH, "//div[@name='category' and @role='listbox']/div/div[3]")
    contact_role_xpath = (By.XPATH, "//div[@name='category' and @role='listbox']/div/div[4]")
    affiliate_sel_xpath = (By.XPATH, "//div[@name='category' and @role='listbox']/div/div[5]")
    status_box_xpath = (By.XPATH, "//div[@name='status' and @role ='listbox']")
    status_sel_xpath = (By.XPATH, "//div[@name='status' and @role ='listbox']/div/div/span")
    description_xpath = (By.XPATH, "//textarea[@name='description']")
    time_zone_xpath = (By.XPATH, "//div[@name='timezone']//input[@type='text']")
    street_ad_inp_xpath = (By.XPATH, "//input[@placeholder='Street Address']")
    city_inp_xpath = (By.XPATH, "//input[@placeholder='City']")
    state_inp_xpath = (By.XPATH, "//input[@placeholder='State / County']")
    post_inp_xpath = (By.XPATH, "//input[@placeholder='Post Code']")
    country_clk_xpath = (By.XPATH, "//div[@name='country']//i[@class='dropdown icon']")
    country_sel_xpath = (By.XPATH, "//div[@name='country' ]/div[2]/div//span")
    phone_country_clk_xpath = (By.XPATH, '//div[@name="hint"]')
    phone_country_select_xpath = (By.XPATH, "//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']")
    phone_number_inp_xpath = (By.XPATH, "//input[@placeholder='Number']")
    home_phone_inp_xpath = (By.XPATH, "//input[@placeholder='Home, Work, Mobile...']")
    position_inp_xpath = (By.XPATH, "//input[@name='position']")
    department_inp_xpath = (By.XPATH, "//input[@name='department']")
    supervisor_clk_xpath = (By.XPATH, "//div[@name='supervisor']//input[@type='text']")
    supervisor_select_xpath = (By.XPATH, "//div[@class='active selected item addition']//span[@class='text']")
    assistent_clk_inp_xpath = (By.XPATH, "//div[@name='assistant']//input[@type='text']")
    assistent_add_xpath = (By.XPATH, "//div[@class='selected item addition']//span[@class='text']")
    referer_clk_inp_xpath = (By.XPATH, "//div[@name='referred_by']//input[@type='text']")
    referer_add_xpath = (By.XPATH, "//div[@class='selected item addition']//span[@class='text']")
    source_inp_xpath = (By.XPATH, "//div[@name='source' and @role='listbox']")
    source_add_xpath = (By.XPATH, "//div[@name='source' and @role='listbox']/div/div/span")
    day_inp_xpath = (By.XPATH, "//input[@placeholder='Day']")
    month_inp_xpath = (By.XPATH, "//div[@name='month']")
    month_select_xpath = (By.XPATH, '//div[@name="month"]/div[2]/div/span')
    year_inp_xpath = (By.XPATH, "//input[@placeholder='Year']")
    save_btn_xpath = (By.XPATH, "//i[@class='save icon']")
    cont_icon_xpath = (By.XPATH, "//i[@class='users icon']")

    def __init__(self, driver):
        self.driver = driver

    def contactadd_click(self):
        el = self.driver.find_element(*AddContacts.cont_icon_xpath)
        self.act = ActionChains(self.driver)
        self.act.move_to_element(el).perform()
        self.driver.find_element(*AddContacts.contactsadd_btn_xpath).click()

    def first_name_enter(self, first_name):
        self.driver.find_element(*AddContacts.first_name_inp_name).clear()
        self.driver.find_element(*AddContacts.first_name_inp_name).send_keys(first_name)

    def last_name_enter(self, last_name):
        self.driver.find_element(*AddContacts.last_name_inp_xpath).clear()
        self.driver.find_element(*AddContacts.last_name_inp_xpath).send_keys(last_name)

    def middle_name_enter(self, middle_name):
        self.driver.find_element(*AddContacts.middle_name_inp_Xpath).clear()
        self.driver.find_element(*AddContacts.middle_name_inp_Xpath).send_keys(middle_name)

    def company_enter(self, company):
        self.driver.find_element(*AddContacts.company_inp_xpath).clear()
        self.driver.find_element(*AddContacts.company_inp_xpath).send_keys(company)

    def tags_add(self, tag_name):
        self.driver.find_element(*AddContacts.tags_box_xpath).click()
        self.driver.find_element(*AddContacts.tags_box_xpath).send_keys(tag_name)
        el1 = self.driver.find_element(*AddContacts.tag_active_xpath)
        self.driver.execute_script('arguments[0].click()',el1)

    def email_enter(self, email):
        self.driver.find_element(*AddContacts.email_inp_xpath).clear()
        self.driver.find_element(*AddContacts.email_inp_xpath).send_keys(email)

    def category_select(self, category):
        self.driver.find_element(*AddContacts.category_xpath).click()
        if category == 'Lead':
            self.driver.find_element(*AddContacts.lead_sel_xpath).click()
        elif category == 'Customer':
            self.driver.find_element(*AddContacts.customer_sel_xpath).click()
        elif category == 'Contact':
            self.driver.find_element(*AddContacts.contact_role_xpath).click()
        elif category == 'Affiliate':
            self.driver.find_element(*AddContacts.affiliate_sel_xpath).click()
        else:
            self.driver.find_element(*AddContacts.customer_sel_xpath).click()

    def status_select(self, status):
        self.driver.find_element(*AddContacts.status_box_xpath).click()
        sel = self.driver.find_elements(*AddContacts.status_sel_xpath)
        for i in sel:
            if i.text == status:
                i.click()
                break

    def description_enter(self, discription):
        self.driver.find_element(*AddContacts.description_xpath).send_keys(discription)

    def time_zone(self, time_zone):
        self.driver.find_element(*AddContacts.time_zone_xpath).send_keys(time_zone)

    def street_address_enter(self, street_addr):
        self.driver.find_element(*AddContacts.street_ad_inp_xpath).send_keys(street_addr)

    def city_enter(self, city):
        self.driver.find_element(*AddContacts.city_inp_xpath).send_keys(city)

    def state_enter(self, state):
        self.driver.find_element(*AddContacts.state_inp_xpath).send_keys(state)

    def post_enter(self, post_code):
        self.driver.find_element(*AddContacts.post_inp_xpath).send_keys(post_code)

    def county_select(self, country):
        self.driver.find_element(*AddContacts.country_clk_xpath).click()
        countries = self.driver.find_elements(*AddContacts.country_sel_xpath)
        for i in countries:
            if i.text == country:
                i.click()
                break

    def phone_country_select(self):
        self.driver.find_element(*AddContacts.phone_country_clk_xpath).click()
        self.driver.find_element(*AddContacts.phone_country_select_xpath).click()

    def phonenumber_enter(self, phonenumber):
        self.driver.find_element(*AddContacts.phone_number_inp_xpath).send_keys(phonenumber)

    def homephone_enter(self, homephone):
        self.driver.find_element(*AddContacts.home_phone_inp_xpath).send_keys(homephone)

    def position_enter(self, position):
        self.driver.find_element(*AddContacts.position_inp_xpath).send_keys(position)

    def department_enter(self, department):
        self.driver.find_element(*AddContacts.department_inp_xpath).send_keys(department)

    def supervisor_enter(self, supervisor):
        self.driver.find_element(*AddContacts.supervisor_clk_xpath).send_keys(supervisor)
        # self.driver.find_element(*AddContacts.supervisor_select_xpath).click()

    def assistent_enter(self, assistent):
        self.driver.find_element(*AddContacts.assistent_clk_inp_xpath).send_keys(assistent)
        # self.driver.find_element(*AddContacts.assistent_add_xpath).click()

    def referedby_enter(self, referer):
        self.driver.find_element(*AddContacts.referer_clk_inp_xpath).send_keys(referer)
        # self.driver.find_element(*AddContacts.referer_add_xpath).click()

    def source_select(self, source):
        self.driver.find_element(*AddContacts.source_inp_xpath).click()
        sources = self.driver.find_elements(*AddContacts.source_add_xpath)
        for i in sources:
            if i.text == source:
                i.click()
                break

    def day_enter(self, day):
        self.driver.find_element(*AddContacts.day_inp_xpath).send_keys(day)

    def month_enter(self, month):
        self.driver.find_element(*AddContacts.month_inp_xpath).click()
        months = self.driver.find_elements(*AddContacts.month_select_xpath)
        for i in months:
            if i.text == month:
                i.click()
                break

    def year_select(self, year):
        self.driver.find_element(*AddContacts.year_inp_xpath).send_keys(year)

    def save_click(self):
        # wait = WebDriverWait(self.driver,10)
        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='save icon']")))
        self.driver.find_element(*AddContacts.save_btn_xpath).click()


    def customer_verify(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="selectable "]')))
        name = self.driver.find_element(By.XPATH, '//span[@class="selectable "]').text
        return name

