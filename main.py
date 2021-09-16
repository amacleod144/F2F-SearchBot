#Python bot to search cards and return prices
#Alex MacLeod
#2021


#Main resource used for web scraping:
#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/

#imports and basic setup

from bs4 import BeautifulSoup as bs
import urllib.request as url
import pandas as pd
from selenium import webdriver as wd
import search_functions as sf

#set up page and query
f2f_url = "https://www.facetofacegames.com/"

f2f_page = url.urlopen(f2f_url)

f2f_soup = bs(f2f_page,'html.parser')

#print(f2f_soup.prettify) #just for viewing html, can also just look at page source

#find the right html element (searchbar)
searchbar = f2f_soup.input #searchbar is only input on the page










