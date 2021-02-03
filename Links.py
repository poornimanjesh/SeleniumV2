from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.gap.co.uk/")
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of Links Present:", len(links))
#for link in links:
   # print(link.text)
time.sleep(10)
#driver.find_element(By.LINK_TEXT,"FIND A STORE").click()
driver.find_element(By.PARTIAL_LINK_TEXT," A STORE").click()
time.sleep(5)
driver.close()
