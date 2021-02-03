from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.expedia.com/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a/span").click()
time.sleep(2)
driver.find_element_by_css_selector("//button[@aria-label='Leaving from']").click()
time.sleep(5)
print(driver.title)
driver.find_element_by_id("location-field-destination-input").click()




