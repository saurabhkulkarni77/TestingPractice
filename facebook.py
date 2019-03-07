import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
 
class MyWikiTestCase(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/saurabh/Desktop/chromedriver')
    def test_Wiki(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://en.wikipedia.org')
        driver.find_element_by_id('searchInput').send_keys('Sachin Tendulkar')
        driver.find_element_by_id('searchButton').click()
        print("Test Passed")
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main(exit = False,testRunner=HTMLTestRunner(output='example_dir'))
