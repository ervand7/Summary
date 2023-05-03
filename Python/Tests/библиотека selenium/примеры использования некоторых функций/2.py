from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='/Users/USER/Downloads/geckodriver')
driver.get("https://www.aviasales.ru/?gclid=Cj0KCQiA4L2BBhCvARIsAO0SBdbkqn"
           "Q953CFSxuCOxrj9RGTWW4Fa_hLzj0hwKpEEoetMfegLPLx0TsaAqR9EALw_wcB")
sleep(0.5)
element = driver.find_element_by_xpath("//div[@class='additional-fields --avia']").click()
sleep(1)
element2 = driver.find_element_by_xpath("//*[text()='Первый класс']").click()
sleep(1)
element3 = driver.find_element_by_xpath("//*[contains(text(), 'Найти билеты')]").click()
sleep(1)
driver.get("https://www.google.com")
input_element = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
sleep(1)
input_element.send_keys("Ерванд Агаджанян")
sleep(1)
input_element.clear()
sleep(1)
input_element.send_keys("родион замуруев")
input_element.send_keys(Keys.RETURN)
sleep(2)

driver.close()




