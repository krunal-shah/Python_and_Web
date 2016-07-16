import urllib2
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

testcode=input("Test Code:")

driver = webdriver.Chrome()
main_window = driver.current_window_handle

		
flag = 0
for x in range(0,10):
	for y in range(0,10):
		roll_number = 87000 + 10*x + y
		driver.get("http://bothraclasses.com/evalution-report")
		roll = driver.find_element_by_name("rollno")
		roll.clear()
		roll.send_keys(roll_number)
		roll.send_keys(Keys.RETURN)
		page = driver.page_source
		soup = BeautifulSoup(page,"html.parser")
		
		for span in soup.find_all("span"):
			if span.string == "Invalid Roll Number":
				break
				flag = 1
		
		if flag == 1:
			flag = 0
			continue

		tables = soup.find_all("tbody")
		table = tables[len(tables)-1]

		i=0
		foo = 0
		j=0
		string = []
		for tr in table.find_all("tr"):
			i=0
			string.append([])
			for tc in tr.find_all("td"):
				string[j].append(tc.string)
				i+=1
			j+=1
		index=0
		a=0
		for a in range(j):
			if string[a][1] == str(testcode):
				index = a
		if index!= 0:
			print str(roll_number) + " " + string[index][4] +","+string[index][3]


