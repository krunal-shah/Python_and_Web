from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import getpass
from bs4 import BeautifulSoup

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
main_window = driver.current_window_handle
driver.get("https://www.facebook.com")

#Facebook login
emailid = raw_input("Facebook email id:")
email = driver.find_element_by_name("email")
email.send_keys(emailid)
pwd = getpass.getpass("Facebook password:")
password = driver.find_element_by_name("pass")
password.send_keys(pwd)
password.submit()

action= ActionChains(driver)


content=raw_input("What do you want to post?")
post = driver.find_element_by_name("xhpc_message")
action.click(post)
action.perform()
post.send_keys(content)
post.submit()