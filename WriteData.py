import XLUtils
from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

path=r"C:\users\manju\Documents\Poornima\excel\openpy.xlsx"
rows=XLUtils.getRowCount(path,"open1")

for r in range(2,rows+1):
    time.sleep(2)
    username=XLUtils.readData(path,"open1",r,1)
    time.sleep(2)
    password=XLUtils.readData(path,"open1",r,2)

    driver.find_element_by_id("txtUsername").send_keys(username)
    time.sleep(2)
    driver.find_element_by_id("txtPassword").send_keys(password)


    driver.find_element_by_id("btnLogin").click()
    time.sleep(2)
    print(driver.title)

    if driver.title == "OrangeHRM":

        print("test passed")
        #time.sleep(2)
        XLUtils.writeData(path,"open1",r,3,"test passed")
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


    else:
        print("test failed")
        #time.sleep(2)
        XLUtils.writeData(path,"open1",r,3,"test failed")


driver.close()

