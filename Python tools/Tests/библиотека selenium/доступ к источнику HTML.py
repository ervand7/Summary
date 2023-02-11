from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox(executable_path='/Users/USER/Downloads/geckodriver')
driver.get("https://coderoad.ru/7861775/Python-Selenium-доступ-к-источнику-HTML")

html_source = driver.page_source
if "whatever" in html_source:
    print(True)
else:
    print(False)





