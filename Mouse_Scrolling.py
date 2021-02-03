from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#driver.execute_script("window.scrollBy(0,1000)","")
#flag=driver.find_element_by_xpath("//img[@alt='Flag of Seychelles']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.close()

