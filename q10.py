import unittest
import selenium
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.google.com/')

    def test_search(self):
        self.driver.get('https://www.google.com/')
        elem = self.driver.find_element_by_name('q')
        elem.send_keys('selenide')
        elem.send_keys(Keys.ENTER)
        elem = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
        print(elem.text)
        elem.send_keys(Keys.ENTER)
        self.driver.back()
        time.sleep(1)
        elem = self.driver.find_element_by_xpath('// *[ @ id = "hdtb-msb"] / div[1] / div / div[3] / a')
        elem.send_keys(Keys.ENTER)
        elem = self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]')
        print(elem.text)
        first_window_handler = self.driver.current_window_handle
        elem.send_keys(Keys.ENTER)
        sec_window_handler = self.driver.window_handles[1]
        time.sleep(2)
        self.driver.switch_to.window(sec_window_handler)
        self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(first_window_handler)
        self.driver.back()
        elem = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a')
        print(elem.text)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)


    def tearDown(self):
         self.driver.close()


if __name__ == '__main__':
    unittest.main()




