from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/register.php")
print(driver.title)
element=driver.find_element_by_name("country")
drp=Select(element)
#drp.Select_by_visible_text("ALBANIA")
#con=drp.select_by_index(2)
#print(con)
#con=drp.select_by_value("ANGOLA")
#print(con)
print(len(drp.options))
all_option=drp.options
for option in all_option:
    print(option.text)

time.sleep(5)

driver.close()