import basic_functions
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os
import time
import utility_methods
import random

class import_functions:

    def __init__(self,):

        self.base_url = 'https://www.instagram.com'
        opts = Options()

        opts.add_argument("user-agent=Chrome --- Android Mobile")

        self.driver = webdriver.Chrome('chromedriver.exe')
