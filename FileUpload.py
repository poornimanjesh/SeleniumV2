from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
time.sleep(7)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users//manju//OneDrive//Pictures//CCapture (4)_edited.jpg")
driver.close()