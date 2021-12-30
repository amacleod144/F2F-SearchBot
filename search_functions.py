#functions for searching the f2f site

#set up and modules
from bs4 import BeautifulSoup as bs
import urllib.request as url
import pandas as pd
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

#def create_instance():

#def search_card():



#drafts for function, TODO: turn into actual functions

#establish driver path and browser instance

#NOTE: if you update chrome, you must download the new chrome driver and install it in program files,
#then paste the new path here. If you do not, code will not execute
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = wd.Chrome(PATH)

driver.get("https://www.facetofacegames.com/")
#(driver.title)

#find search bar element and pass terms
#search_bar = driver.find_element_by_id("search_query") id was removed from tag, this no longer works
search_bar = driver.find_element_by_css_selector("input[placeholder = 'Enter a search term']")

search_bar.send_keys("goldspan dragon")
search_bar.send_keys(Keys.RETURN)

#create empty lists for data from site
product_name = []
product_price = []

#create item
#https://medium.com/@jb.ranchana/web-scraping-with-selenium-in-python-amazon-search-result-part-1-f09c88090932
items = driver.find_elements_by_xpath("//div[contains(@class, 'hawk-results__item')]")



#results = driver.find_element_by_class_name("productGrid") #currently does not include prices
#results = driver.find_elements_by_xpath("//span[@data-product-price-without-tax") #attempt to get just prices
#results = driver.find_elements_by_xpath("//*[@id='product-listing-container']/form[2]/ul/li[1]/article/div[5]/div/div[1]/div[3]/span[3]") # got this by inspecting price
#results = driver.find_element_by_class_name("price price--withoutTax")

#"data-product-price"#another attempt to get prices

#print(results.text)


#driver.quit()