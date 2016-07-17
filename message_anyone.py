from selenium import webdriver
from selenium.common.exceptions import TimeoutException
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


#replace the username of some friend with the username of a friend
driver.get("https://www.facebook.com/messages/\\\\\username of some of your friend")
search = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/div[1]/div[2]/span/span/input")
action.click(search)
action.perform()
name = raw_input("Whom to send the message to?")
search[0].send_keys(name)
search[0].send_keys(Keys.RETURN)
message = driver.find_element_by_name("message_body")
content = raw_input("What message to send?")
message.send_keys(content)
message.send_keys(Keys.RETURN)
