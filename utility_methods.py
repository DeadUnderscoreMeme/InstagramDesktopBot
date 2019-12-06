import math
import os
from selenium import webdriver

def scrape_keywords(posts):
    print(posts)
    image_list = []
    for element in posts:
        print(element.get_attribute('class'))
        image = element.find_element_by_xpath("./*[contains(@src,'instagram')]")
        image_list.append(image)
        image_src = image.get_attribute('src')
        print(image_src)

    