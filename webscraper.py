#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

URL = "https://sandiego.craigslist.org/search/sof"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

results = soup.find(id="search-results")
cl_jobs = results.find_all("li", class_="result-row") # for main loop

_href_url = []
_time = []
_job_location = []

file = open('cl-jobs.csv','w')
writer = csv.writer(file)

# write header rows
writer.writerow(["Title", "Date", "Location"])

href_url = []
time = []
job_location = []
for cl_job in cl_jobs:
    
    #for i in soup.findAll('li'):
    #    print(i.text.strip())

    href_url.append = soup.findAll(class_="result-title")[0].text.strip()

    time.append = soup.find(class_="result-date")[0].text.strip() # 12:23

    job_location.append = soup.find(class_="result-hood")[0].text.strip() # location (city)

    writer.writerow([href_url, time, job_location])

file.close()
