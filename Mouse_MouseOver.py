from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
print(driver.title)
admin=driver.find_element_by_xpath("//b[.='Admin']")
UserM=driver.find_element_by_id("menu_admin_UserManagement")
user=driver.find_element_by_id("menu_admin_viewSystemUsers")
actions=ActionChains(driver)
time.sleep(5)
actions.move_to_element(admin).move_to_element(UserM).move_to_element(user).click().perform()
time.sleep(5)

driver.close()