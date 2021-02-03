from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
element=driver.find_element_by_xpath("//button[.='Copy Text']")
actions=ActionChains(driver)
actions.double_click(element).perform()
time.sleep(10)
driver.close()