import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from pageobjects.addcontacts import AddContacts
from pageobjects.loginfreecrm import Logincrm
driver = webdriver.Chrome()
driver.get("https://freecrm.com/")
driver.implicitly_wait(10)

driver.find_element(*Logincrm.login_lnk_xpath).click()
driver.find_element(*Logincrm.email_inp_name).clear()
driver.find_element(*Logincrm.email_inp_name).send_keys('somapujari0@gmail.com')
driver.find_element(*Logincrm.password_inp_name).clear()
driver.find_element(*Logincrm.password_inp_name).send_keys('Test@2323')
driver.find_element(*Logincrm.login_btn_inp_xpath).click()

# time.sleep(3).
el = driver.find_element(*AddContacts.cont_icon_xpath)
act = ActionChains(driver)
act.move_to_element(el).perform()
driver.find_element(*AddContacts.contactsadd_btn_xpath).click()

driver.find_element(*AddContacts.tags_box_xpath).click()
time.sleep(2)
driver.find_element(*AddContacts.tags_box_xpath).send_keys('business')
driver.find_element(*AddContacts.tag_active_xpath).click()
# driver.execute_script('arguments[0].click()', el1)

time.sleep(5)
