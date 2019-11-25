from selenium import webdriver
import time

url = 'https://socialrocket.in/'
driver = webdriver.Chrome('chromedriver.exe')

driver.get(url)
driver.maximize_window()

time.sleep(3)

for i in range(1,100):
    name_field = driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > section.index-module--section--20zZC.index-module--hasBackgroundSecondary--2s7kJ.index-module--has-text-centered--3XPnf > div > div > div:nth-child(1) > form > div:nth-child(2) > div > input')
    name_field.send_keys('spam' + str(i) + ' lul' + str(100-i))
    
    email_field = driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > section.index-module--section--20zZC.index-module--hasBackgroundSecondary--2s7kJ.index-module--has-text-centered--3XPnf > div > div > div:nth-child(1) > form > div.index-module--field--AqZ9Y.index-module--is-horizontal--3thvl > div:nth-child(1) > div > div > input')
    email_field.send_keys('spamemail' + str(i) +'@gmail.com')
    
    comp_name = driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > section.index-module--section--20zZC.index-module--hasBackgroundSecondary--2s7kJ.index-module--has-text-centered--3XPnf > div > div > div:nth-child(1) > form > div.index-module--field--AqZ9Y.index-module--is-horizontal--3thvl > div:nth-child(2) > div > div > input')
    comp_name.send_keys('The ' + str(i) + ' spam company')
    
    mess_field = driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > section.index-module--section--20zZC.index-module--hasBackgroundSecondary--2s7kJ.index-module--has-text-centered--3XPnf > div > div > div:nth-child(1) > form > div:nth-child(4) > div > textarea')
    mess_field.send_keys('Have fun with this ' + str(i) + ' messages spammed')
    
    submit_button = driver.find_element_by_css_selector('#gatsby-focus-wrapper > div > section.index-module--section--20zZC.index-module--hasBackgroundSecondary--2s7kJ.index-module--has-text-centered--3XPnf > div > div > div:nth-child(1) > form > button')
    submit_button.click()
    time.sleep(5)
   
    return_button = driver.find_element_by_css_selector('#back-link')
    
    return_button.click()
    time.sleep(5)

    print ('The ' + str(i) + 'spam is being sent')

