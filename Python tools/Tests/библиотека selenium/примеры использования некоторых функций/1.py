# статья про javascript-in-python: https://dzone.com/articles/perform-actions-using-javascript-in-python-seleniu

# делаем нужные импорты
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# указываем путь к скаченному драйверу (предварительно разархивировав его)
driver = webdriver.Firefox(executable_path='/Users/USER/Downloads/geckodriver')

# и дальше уже делаем все, что хотим
driver.get("http://www.python.org")
# пример использования execute_script("какой-то javascript")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(4)

first_element = driver.find_elements_by_xpath("//*[text()='Events']")
first_element[0].click()
second_element = driver.find_elements_by_xpath("//*[text()='Events']")

# находим локацию определенных элементов
location = second_element[0].location
print(location)
# находим size определенных элементов
size = second_element[0].size
print(size)

# находим title
print(driver.title)

print(driver.w3c)  # True
print(type(driver.page_source))  # <class 'str'>
print(driver.page_source)


driver.get("http://stackoverflow.com/questions/7794087/running-javascript-in-selenium-using-python")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)

# закрываем браузерное окно
driver.close()




