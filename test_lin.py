from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
print("testcase started")

driver.maximize_window()
driver.get("https://www.linkedin.com/login")
driver.find_element_by_name("session_key").send_keys("navakanthreddy4445@gmail.com")
time.sleep(2)
driver.find_element_by_name("session_password").send_keys("navakanth@12YJ")
time.sleep(2)
driver.find_element_by_class_name("btn__primary--large.from__button--floating").send_keys(Keys.ENTER)
time.sleep(20)
driver.close()
print("testcase ended")