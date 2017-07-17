import unittest
import LaptopPage


from selenium import webdriver


class FirstTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\Program Files (x86)\ChromeDriver\chromedriver.exe')
        self.driver.get('http://rozetka.com.ua/ua/')
        #self.driver.get('http://rozetka.com.ua/ua/notebooks/c80004/filter/')


    def test_image(self):
        laptop_page = LaptopPage.LaptopPage(self.driver)
        laptop_page.get_img()



    # TODO скріншот при падінні
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()