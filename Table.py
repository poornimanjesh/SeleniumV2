
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/table-pagination-demo.html")

rows=(len(driver.find_elements_by_xpath("//*[@id='myTable']/tr")))
cols=(len(driver.find_elements_by_xpath("//*[@id='myTable']/tr[1]")))
print(rows)
print(cols)
for r in range(2,rows+1):
        value=driver.find_element_by_xpath("//*[@id='myTable']/tr["+(r)+"]").text()
        print(value,end=' ')
print()
driver.close()
