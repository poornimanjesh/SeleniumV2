from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.joinhoney.com/trending/stores")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Trending:Stores:index-div:argos-uk']/div/div[2]/div/div[2]/span/div[2]/div/div").click()
time.sleep(5)
driver.close()
driver.quit()

