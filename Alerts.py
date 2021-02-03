from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://demoqa.com/alerts")
driver.find_element_by_id("confirmButton").click()
time.sleep(5)
#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
driver.close()

