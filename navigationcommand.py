from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.joinhoney.com/trending/stores")
print(driver.title)
time.sleep(5)
driver.get("https://www.amazon.com")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)
driver.quit()



