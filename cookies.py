
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\Drivers\Chrome\chromedriver.exe")
driver.get("https://www.amazon.com/")

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

cookie={'name':'mycooki','value':'1254367'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('mycooki')
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)




driver.close()