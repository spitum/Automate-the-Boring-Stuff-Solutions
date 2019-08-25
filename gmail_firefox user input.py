from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def gmail_sender( email_address, password, recipient, message):
    gmail_url = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    browser = webdriver.Firefox()
    browser.get(gmail_url)

    email_field = browser.find_element_by_name('identifier')
    email_field.send_keys(email_address)
    email_field.send_keys(Keys.ENTER)
    time.sleep(3)

    password_field = browser.find_element_by_name("password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    time.sleep(5) #Wait for the e-mail screen to open

    compose_field = browser.find_element_by_class_name("z0")
    compose_field.click()
    time.sleep(5) #Wait for the e-mail screen to open

    to_field = browser.find_element_by_name("to")
    to_field.send_keys(recipient)
    time.sleep(1) #Wait for the e-mail screen to open

    subj_field = browser.find_element_by_name("subjectbox")
    subj_field.send_keys('test email')
    time.sleep(1) #Wait for the e-mail screen to open

    body_field = browser.find_element_by_css_selector("div[aria-label='Message Body']")
    body_field.send_keys(message)

    send_button = browser.find_element_by_css_selector("div[aria-label='Send ‪(Ctrl-Enter)‬']")
    send_button.click()

if __name__ == '__main__':
    gmail_user = input("Please enter gmail user: ")
    gmail_password = input ("Please enter gmail password:")
    recipient_email = input('Please enter recipient email: ')
    message_body = input("Please enter test message to send to recipient: ")
    gmail_sender(gmail_user, gmail_password, recipient_email, message_body) #Enter in your parameters here.