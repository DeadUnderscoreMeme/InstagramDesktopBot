from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
    

    def find_images(self,):
        self.image_list = self.driver.find_elements_by_tag_name('img')

        self.displaypic_list = []
        self.post_images_list = []
        for element in self.image_list:
            # print("{} : {} Image Link is : \n {} \n".format(num,element.get_attribute('alt'),element.get_attribute('src')))
            alt_str = element.get_attribute('alt')
            if 'profile picture' in alt_str:
                self.displaypic_list.append(element)
            else :
                self.post_images_list.append(element)

        # print ('The profile pics are: \n')
        # for ele in displaypic_list:
        #     print(ele.get_attribute('alt'))

        # print ('The image posts are : \n')
        # for ele in post_images_list:
        #     print(ele.get_attribute('alt'))


    def find_posts_by_image(self,):
        self.post_list = []
        for element in self.post_images_list:
            # print(element.get_attribute('src'))
            parent = element.find_element_by_xpath('//ancestor::article')
            # print(parent.get_attribute('class'))
            self.post_list.append(parent)
            # print(parent)
        # print(self.post_list)
        # for element in self.post_list:
        #     print(element.get_attribute('class'))


    def find_posts_by_pfp(self,):
        self.post_list_by_pfp = []
        for element in self.displaypic_list:
            self.post_list_by_pfp.append(element.find_element_by_xpath('../../../..'))
        
        # for element in self.post_list_by_pfp:
        #     print(element.get_attribute('class'))


    def find_like_button_of_post(self,):
        self.like_buttons = []
        
        for element in self.post_list:
            like_button = element.find_element_by_xpath("./div[2]/section[1]/span[1]/button/*[contains(@class,'Heart')]")
            self.like_buttons.append(like_button)
            # print(element.find_element_by_xpath("./div[2]/section[1]/span[1]/button/*[contains(@class,'Heart')]").get_attribute('class'))

        for element in self.like_buttons:
            print(element.get_attribute('aria-label'))

if __name__ == '__main__':
        ig_bot = InstagramBot('__dead__meme__', 'Hrishi$00')
        ig_bot.login()
        time.sleep(1)
        ig_bot.find_images()
        ig_bot.find_posts_by_image()
        ig_bot.find_like_button_of_post()
   