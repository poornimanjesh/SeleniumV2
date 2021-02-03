from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.amazon.com/")
print(driver.title)

#driver.get_screenshot_as_file("C:\Test\m.jpg")
driver.save_screenshot("C:\Test\s.png\q.png")


driver.close()