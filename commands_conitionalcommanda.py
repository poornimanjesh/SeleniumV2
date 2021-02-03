from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://longfield-harrow.secure-dbprimary.com/service/util/login?path=/harrow/primary/longfield")
name=driver.find_element_by_id("displayUsername")
print(name.is_displayed())
print(name.is_enabled())
driver.find_element_by_id("displayUsername").send_keys("aadyam")
driver.find_element_by_name("password").send_keys("quartz")
driver.find_element_by_id("loginButton").click()
print(driver.current_url)
print(driver.title)
time.sleep(5)
driver.close()

