#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

URL = "https://sandiego.craigslist.org/search/sof"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="search-results")
cl_jobs = results.find(class_="result-row") # for main loop

file = open('cl-jobs.csv','w')
writer = csv.writer(file)

# write header rows
writer.writerow(["column #1", "column #2"])

for cl_job in cl_jobs:

    # one entry
    #job_title = cl_job.find("li", class_=)

    # second entrye

    #href_url = cl_job.find('a')

    # third entry
    time = soup.find(class_="result-date") # 12:23

    # fourth entry
    h3_tag = soup.find("h3")

    writer.writerow([time, h3_tag])

file.close()
