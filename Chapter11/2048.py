from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com/#automate')
# linkElem = browser.find_element_by_link_text('Read Online for Free')
# linkElem.click() # follows the "Read It Online" link

from selenium.webdriver.common.keys import Keys
import getpass


browser = webdriver.Firefox()
browser.get('https://play2048.co/')
browser.implicitly_wait(5)


i= 0
while i < 100:
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.RIGHT)
    i+=1
    
browser.implicitly_wait(5)
browser.close()