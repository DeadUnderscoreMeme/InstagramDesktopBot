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

    
    



if __name__ == '__main__':
        ig_bot = InstagramBot('_dead_meme_pvt_', 'Hrishi$00')
        
