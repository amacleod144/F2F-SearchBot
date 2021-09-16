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
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = wd.Chrome(PATH)

driver.get("https://www.facetofacegames.com/")
#(driver.title)
