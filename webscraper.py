#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

URL = "https://sandiego.craigslist.org/search/sof"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

results = soup.find(id="search-results")
cl_jobs = results.find_all("li", class_="result-row") # for main loop

file = open('cl-jobs.csv','w')
writer = csv.writer(file)

# write header rows
writer.writerow(["Title", "Date"])

here = soup.find_all('ul')

for cl_job in cl_jobs:
    
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll("li"):
                href_url = soup.find(class_="result-title").text.strip()
                time = soup.find(class_="result-date").text.strip()
                writer.writerow([href_url, time])
                #job_location = soup.find(class_="result-hood").text.strip() # location (city)
    finally:
        file.close()
