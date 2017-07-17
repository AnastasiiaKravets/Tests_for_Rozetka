import os
import time
import urllib
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


class LaptopPage:
    def __init__(self, driver):
        self.driver = driver
        #self.driver = webdriver.Chrome

    @staticmethod
    # TODO локатор передати як атрибут
    def wait_for(condition):
        i = 0
        step = 0.5
        exception = None
        for i in range(3):
            for j in range(int(45 / step)):
                print(j)
                try:
                    return exec(condition)
                except:
                    exception = sys.exc_info()[0]
                    continue
                time.sleep(step)
            i += 1
        else:
            print(exception)

    def close_addvert(self):
        pass

    def get_img(self):

        self.driver.implicitly_wait(5)

        # перехід на загальну сторінку ноутбуків
        self.driver.maximize_window()
        main_laptop_link = self.driver.find_element_by_class_name('f-menu-l-i')
        main_laptop_link.click()

        # перехід на сторінку вибору категорії ноутбуків
        secondary_laptop_link = self.driver.find_element_by_class_name('pab-h3-link')
        secondary_laptop_link.click()

        # перехід на сторінку ноутбуків
        laptop_link = self.driver.find_element_by_class_name('pab-h2-link')
        laptop_link.click()

        # перехід на сторінку певного ноута
        link_element = self.driver.find_elements_by_xpath("//div[@class = 'g-i-tile-i-title clearfix']")
        print(list(link_element))
        i = 0
        for i in range(len(link_element)):

            # TODO закриття рекламного оголошення, викидає помилку при перекритті посилання на ноут
            self.close_addvert()  # закривання ремного оголошення
            link = self.driver.find_elements_by_xpath("//div[@class = 'g-i-tile-i-title clearfix']")
            link[i].click()

            '''# створення папки з назвою ноута
            laptop_name = self.driver.find_element_by_tag_name('h1').text
            print(laptop_name)
            #path = str('./'+laptop_name)
            #os.makedirs(path)'''

            # перехід на вкладку фото
            laptop_foto = self.driver.find_element_by_name('photo')
            laptop_foto.click()

            # скачування картинок
            laptop_img = self.driver.find_elements_by_class_name('pp-photo-tab-i-img')
            j = 0

            # TODO  розбиття на папки
            for element in laptop_img:
                self.driver.execute_script("return arguments[0].scrollIntoView();", element)
                image = element.find_element_by_tag_name("img")
                src = image.get_attribute("src")
                url = urllib.parse.urlparse(src)
                image_name = os.path.split(url.path)[1]
                urllib.request.urlretrieve(src, image_name)
                j += 1
            self.driver.back()
            self.driver.back()
            i += 1








