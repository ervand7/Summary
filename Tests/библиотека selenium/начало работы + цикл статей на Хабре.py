# https://habr.com/ru/post/248559/
# 1) отсюда скачиваем geckodriver: https://github.com/mozilla/geckodriver/releases
# 2) заходим в настройки "защита и безопасность" мака -> основные, и в левом нижнем углу убираем замочек

# делаем нужные импорты
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 3) указываем путь к скаченному драйверу (предварительно разархивировав его)
driver = webdriver.Firefox(executable_path='/Users/USER/Downloads/geckodriver')

# и дальше уже делаем все, что хотим
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
sleep(2)
assert "No results found." not in driver.page_source
print(driver.title)
print(driver.w3c)
print(driver.page_source)
driver.close()