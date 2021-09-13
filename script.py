from bs4 import BeautifulSoup
from string import *
import csv
from urllib.request import Request, urlopen
for i in range(1,7):
    urlpage = 'URL/page-'+str(i)+'/'
    page = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
    webpage_byte = urlopen(page).read()
    webpage = webpage_byte.decode('utf-8')
    results = BeautifulSoup(webpage, 'html.parser')
    job_elements = results.find_all("div", class_="prod_list")
    for job_element in job_elements:
	    name = getattr(job_element.find("span", class_="titleSpan"), 'text', None)
	    address = getattr(job_element.find("span", class_="placeText"), 'text', None)
	    phone = getattr(job_element.find("a", class_="coordonneesItemLink showMobile"), 'text', None)
	    print(str(name)+";"+str(address)+";"+str(phone).strip())
