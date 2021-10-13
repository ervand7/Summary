import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/USER/Downloads/geckodriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        sleep(2)
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
