from selenium import webdriver
import os
import time


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')

        

    def login(self):
        
        self.driver.get('{}/accounts/login/?source=auth_switcher'.format(self.base_url))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input').send_keys(self.username)
        self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input').send_keys(self.password)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()

        

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url,user))


    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button')
        follow_button.click()

    def scroll_by_value(self, value): #for smooth post by post scrolling use values from 20 - 30
        for i in range(1,value):
            self.driver.execute_script('window.scrollBy(0,{})'.format(i))


    def like_image(self,):
        like_button = self.driver.find_element_by_tag_name('span')
        print(like_button)
        like_button.click()

    def find_posts(self,):
        image_list = self.driver.find_elements_by_tag_name('img')
        num = 1
        for element in image_list:
            print("{} : {} Image Link is : \n {} \n".format(num,element.get_attribute('alt'),element.get_attribute('src')))
            num += 1
    



if __name__ == '__main__':
        ig_bot = InstagramBot('__dead__meme__', 'Hrishi$00')
        ig_bot.login()
        time.sleep(2)
        ig_bot.find_posts()
        # ig_bot.scroll_by_value(43)
        # time.sleep(1)
        
