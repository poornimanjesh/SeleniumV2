from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
source=driver.find_element_by_id("box5")
target=driver.find_element_by_id("box105")
actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()
time.sleep(5)
driver.close()