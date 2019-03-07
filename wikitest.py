import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pyunitreport import HTMLTestRunner
class MyFbTestCase(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/saurabh/Desktop/chromedriver')
    def test_Wiki(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://www.google.com')
        driver.find_element_by_name('q').send_keys("Facebook", Keys.ENTER)
        driver.find_element_by_class_name('LC20lb').click()
        driver.find_element_by_id('email').send_keys("test@t.com")
        driver.find_element_by_id('pass').send_keys("test123")
        print("Test passed")
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main(exit= False,testRunner=HTMLTestRunner(output='example_dir'))