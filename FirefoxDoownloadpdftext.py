from selenium import webdriver
import time

from selenium import webdriver
import time
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting",False)
driver=webdriver.Firefox(executable_path="C:\Drivers\Firefox\geckodriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element_by_id("textbox").send_keys("This is download file from chrome")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
time.sleep(5)
driver.find_element_by_id("pdfbox").send_keys("this is pdf download")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(5)
driver.close()
