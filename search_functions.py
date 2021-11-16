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
search_bar = driver.find_element_by_id("search_query")

search_bar.send_keys("goldspan dragon")
search_bar.send_keys(Keys.RETURN)

#results = driver.find_element_by_class_name("productGrid") #currently does not include prices

results = driver.find_elements_by_xpath("//span[@data-product-price-without-tax") #attempt to get just prices

#"data-product-price"#another attempt to get prices

print(results.text)

#driver.quit()
