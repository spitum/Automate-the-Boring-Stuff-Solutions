from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


def gmail_sender():
    ''' open gmail in firefox, pass sys.argv as user credentials. send test email'''
    # check to make sure correct number of sys args passed.
    if len(sys.argv) == 5:
        try:
            gmail_url = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
            browser = webdriver.Firefox()
            browser.get(gmail_url)

            # enter email address and move to password screen
            email_field = browser.find_element_by_name('identifier')
            email_field.send_keys(sys.argv[1])
            email_field.send_keys(Keys.ENTER)
            time.sleep(3)

            #enter password and wait for 5 seconds
            password_field = browser.find_element_by_name("password")
            password_field.send_keys(sys.argv[2])
            password_field.send_keys(Keys.ENTER)
            time.sleep(5) 

            #Click Next on password screen
            compose_field = browser.find_element_by_class_name("z0")
            compose_field.click()
            time.sleep(5) #Wait for the e-mail screen to open

            #Populate 'To' field
            to_field = browser.find_element_by_name("to")
            to_field.send_keys(sys.argv[3])
            time.sleep(1) #Wait for the e-mail screen to open

            #add subject -- test email. change to whatever you like
            subj_field = browser.find_element_by_name("subjectbox")
            subj_field.send_keys('test email')
            time.sleep(1) #Wait for the e-mail screen to open

            #add body of email
            body_field = browser.find_element_by_css_selector("div[aria-label='Message Body']")
            body_field.send_keys(sys.argv[4])

            #send email
            send_button = browser.find_element_by_css_selector("div[aria-label='Send ‪(Ctrl-Enter)‬']")
            send_button.click()
            
            browser.quit()
            
        except Exception:
            pass

    else:
        print('Please check the number of variables passed. Argument length: ' + str(len(sys.argv)-1))

if __name__ == '__main__':
    gmail_sender() #call through command line with paramters sent as sys args

##sample call: gmail_firefox sys arg.py 'test@email.com' 'password' 'test@email.com' 'test email from selenium'
