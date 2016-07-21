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


#replace the username of some friend with the username of a friend
driver.get("https://www.facebook.com/messages/\\\\\username of one of your friend")
search = driver.find_elements_by_xpath("//div/div[1]/div/div[2]/div[1]/div[2]/span/span/input")
name = raw_input("Whose messages to read?")
search[0].send_keys(name)
search[0].send_keys(Keys.RETURN)
url = driver.current_url
start = url.find('search/')+7
end = url.find('?')
username = url[start:end]
url = "https://www.facebook.com/messages/"+str(username)+"/"
driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page,"html.parser")
#for div in soup.find_all("div","_38 direction_ltr"):
#	print str(div.parent.parent.parent.previous_sibling.find_all("a")[0].string) + " : " + str(div.string)

length = len(soup.find_all("div","_38 direction_ltr"))
index=0
for i in range(length):
	div = soup.find_all("div","_38 direction_ltr")[length-i-1]
	if str(div.parent.parent.parent.previous_sibling.find_all("a")[0].string)=="Krunal Shah":
		index = length-1-i
		print "break"
		break
print index
print length
for i in range(index+1,length):
	print str(soup.find_all("div","_38 direction_ltr")[i].string)



