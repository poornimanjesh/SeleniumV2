from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//button[.='    click   ']").click()
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(5)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
driver.quit()