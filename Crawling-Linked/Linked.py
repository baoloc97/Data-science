from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import io
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
	input_page = 3
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
		
		f_data   = open('data_data.txt','a+')
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
		sleep(5)		
		browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		sleep(10)
		Next_button = browser.find_element_by_xpath('//*[@aria-label="Next"]')
		Next_button.click()


#open Web
browser = webdriver.Firefox()
browser.get("https://www.linkedin.com/checkpoint/lg/login")
#Login
txtUser = browser.find_element_by_id("username")
txtUser.send_keys("baolochuynh24@gmail.com")
txtPass = browser.find_element_by_id("password")
txtPass.send_keys("Baoloc2509")
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

# page_source = BeautifulSoup(browser.page_source,"html.parser")
# total_number = page_source.find_all('div',class_='pb2 t-black--light t-14')
# strings_title= page_source.find_all('a',class_='app-aware-link')
# strings_member = page_source.find_all('div',class_= 'entity-result__primary-subtitle t-14 t-black')
# string_detail = page_source.find_all('p',class_="entity-result__summary t-12 t-black--light ")
# #All number of research can find
# Total = []
# #Title, number of member and all detail
# Titles = []
# Members = []
# Details = []
# for tag in total_number:
# 	Total.append(tag.text.strip())
# for tag in strings_title:
#     Titles.append(tag.text.strip())	
# for tag in strings_member:
# 	Members.append(tag.text.strip())
# for tag in string_detail:
# 	Details.append(tag.text.strip())
# Titles_final = []
# number_searchs = take_first(Total[0])
# print(number_searchs) 
# for i in range(len(Titles)):
# 	if Titles[i] != "" and i != 0 :
# 		Titles_final.append(Titles[i])
# f_data   = open('data_data.txt','w')
# for i in range(len(Titles_final)):
# 		f_data.write("\n")
# 		string = "Group " 
# 		f_data.write("Group " + str(i+1) )
# 		f_data.write("\n")
# 		f_data.write("Title : " + str(Titles_final[i]) )
# 		f_data.write("\n")
# 		f_data.write("Member : "+ str(Members[i]) )
# 		f_data.write("\n")
# 		f_data.write("Detail : "+ str(Details[i]) )
# 		f_data.write("\n")
# 		f_data.write("----------------------------")

#scroll to bottom

#find button next
# f.write(strings_member)

# Name = []
# for string in strings:
# 	if "alt=" and "class" in string:
# 		start = strings.index("alt=")+4
# 		end   = strings.index("class=")
# 		name = strings[start:end]
# 		Name.append(name)
# txt = page_source.find_all('button',class_='artdeco-pill artdeco-pill--slate artdeco-pill--2 artdeco-pill--choice ember-view search-reusables__filter-pill-button')
# print(txt)
# # 6. Đóng browser
# browser.close()
# 1. pip install selenium

# 2. Download the selenium firefox wbedriver(geclodriver)
#      https://github.com/mozilla/geckodrive...​

# 3. Move the firefox webdriver to your bin folder
#     $ sudo mv geckodriver /usr/local/bin

# 4. set the PATH
#      export PATH=$PATH:/usr/local/bin/geckodriver

# dùng xpath với class nhé, em thay cú pháp như này là chạy được nè: 
# search_field = driver.find_element_by_xpath('//*[@class="search-global-typeahead__input always-show-placeholder"]')
