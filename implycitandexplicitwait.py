from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://longfield-harrow.secure-dbprimary.com/service/util/login?path=/harrow/primary/longfield")
driver.find_element_by_id("displayUsername").send_keys("aadyam")
driver.find_element_by_name("password").send_keys("quartz")
driver.find_element_by_id("loginButton").click()
print(driver.title)
#implicit wait works based on time, once you mention implcit wait it aply for all level in same program
