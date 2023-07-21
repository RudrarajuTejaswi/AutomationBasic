from selenium import webdriver
from selenium.webdriver.common.by import By
import time

''' this is to stop browser from closing, instead of using sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=chrome_options)
'''
chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window() #opens full screen chrome window
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html') #opens the given url
# assert returns true or false based on the condition given
assert 'Show Message' in chrome_browser.page_source
#to get the element by id
user_msg = chrome_browser.find_element(By.ID, 'user-message')
# clearing the input box
user_msg.clear()
#inputting to the input box
user_msg.send_keys("I am sucesssful")
#clicking the button
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()
#grab the message displayed
output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I am sucesssful' in output_message.text #checking whether we grabbed the msg
time.sleep(1000)
#chrome_browser.close() # for closing the browser
#chrome_browser.quit() # for closing all browsers opened in one shot