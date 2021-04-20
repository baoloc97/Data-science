from selenium import webdriver
class craigslist_crawler(object):
	def close_webdriver(self):
			self.driver.close()
			print("good bye")

	def __init__(self,query,max_price):
		self.max_price = max_price
		self.query = query
		self.url = f"https://seoul.craigslist.org/search/sss?query={query}&max_price={max_price}"
		self.driver = webdriver.Firefox()
		self.delay = 5

	def load_page(self):
		driver = self.driver
		driver.get(self.url)
		all_data = driver.find_elements_by_class_name("result-row")
		for data in all_data:
			title = data.text.split("$")
			if title[0] == "":
				title = title[1]
			else:
				title = title[0]
			title = data.text.split("\n")	
			price = title[0]
			title = title[-1]
			title = title.split(" ")
			month = title[0]
			day = title[1]
			title = ' '.join(title[2:])
			date = month + " "+ day
			print("TITLE : ", title)
			print("PRICE : ",price)
			print("DATE : ",date)
			

query = "iphone"
max_price = 2200000
crawler = craigslist_crawler(query,max_price)
crawler.load_page()
crawler.close_webdriver()

# 1. pip install selenium

# 2. Download the selenium firefox wbedriver(geclodriver)
#      https://github.com/mozilla/geckodrive...​

# 3. Move the firefox webdriver to your bin folder
#     $ sudo mv geckodriver /usr/local/bin

# 4. set the PATH
#      export PATH=$PATH:/usr/local/bin/geckodriver
