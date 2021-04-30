from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import io
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
def take_first(string):
	list = string.split(" ")
	return list[0]
def take_totalnumber(browser):
	Total = []
	page_source = BeautifulSoup(browser.page_source,"html.parser")
	total_number = page_source.find_all('div',class_='pb2 t-black--light t-14')
	for tag in total_number:
		Total.append(tag.text.strip())
	number_searchs = take_first(Total[0])
	return number_searchs 			


def GetData():
	index =0
	index2 =0
	input_page = 3
	f_data   = open('data_data.txt','w')
	f_data.close()
	with open("Output.csv","w",encoding = "utf8 ",newline = '') as file_csv:    
			header = ["Order","Name Group","Members","Details"]
			writer = csv.writer(file_csv)
			writer.writerow(header)
	for i in range(input_page):

		sleep(5)
		page_source = BeautifulSoup(browser.page_source,"html.parser")
		strings_title= page_source.find_all('a',class_='app-aware-link')
		strings_member = page_source.find_all('div',class_= 'entity-result__primary-subtitle t-14 t-black')
		string_detail = page_source.find_all('p',class_="entity-result__summary t-12 t-black--light ")
		
		
		Titles = []
		Members = []
		Details = []
		
		for tag in strings_title:
			Titles.append(tag.text.strip())	
		for tag in strings_member:
			Members.append(tag.text.strip())
		for tag in string_detail:
			Details.append(tag.text.strip())
		Titles_final = []
		for j in range(len(Titles)):
			if Titles[j] != "" and j != 0 and Titles[j] not in Titles_final:
				Titles_final.append(Titles[j])
		
		f_data   = open('data_data.txt','a')
		for i in range(len(Titles_final)):
				f_data.write("\n")
				f_data.write("Group " + str(index+1) )
				f_data.write("\n")
				f_data.write("Title : " + str(Titles_final[i]) )
				f_data.write("\n")
				f_data.write("Member : "+ str(Members[i]) )
				f_data.write("\n")
				f_data.write("Detail : "+ str(Details[i]) )
				f_data.write("\n")
				f_data.write("----------------------------")
				index = index+1
		
		with open("Output.csv","a",encoding = "utf8 ",newline = '') as file_csv:
		    writer = csv.writer(file_csv)
		    for i in range(len(Titles_final)):
		    	string = ["Group" + str(index2+1),Titles_final[i],Members[i],Details[i]]
		    	writer.writerow(string)
		    	index2 = index2 +1

		sleep(8)		
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		sleep(8)
		Next_button = browser.find_element_by_xpath('//*[@aria-label="Next"]')
		Next_button.click()


#open Web
browser = webdriver.Firefox()
browser.get("https://www.linkedin.com/checkpoint/lg/login")
#Login
Infor = open("Infor.txt",'r')
line = Infor.readlines()
username = line[0]
password = line[1]
txtUser = browser.find_element_by_id("username")
txtUser.send_keys(username)
txtPass = browser.find_element_by_id("password")
txtPass.send_keys(password)
txtPass.send_keys(Keys.ENTER)
sleep(15)
#Search tab 
Search = browser.find_element_by_xpath('//*[@class="search-global-typeahead__input always-show-placeholder"]')
Search_input = "Software Engineer"
Search.send_keys(Search_input)
# search_input = input("what profile do you want ?")
# sleep(5)
# Search.send_keys(search_input)
Search.send_keys(Keys.ENTER)
sleep(20)
Groups = browser.find_element_by_xpath('//*[@aria-label="Groups"]')
Groups.click()
sleep(10)
total_number = take_totalnumber(browser)
print(total_number)
GetData()

