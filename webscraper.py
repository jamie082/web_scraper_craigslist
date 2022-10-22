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
writer.writerow(["column #1", "column #2", "Link"])

for cl_job in cl_jobs:

    href_url = soup.find(class_="result-title").text.strip()

    # third entry
    time = soup.find(class_="result-date").text.strip() # 12:23

    # fourth entry
    link = soup.find(class_="result-heading").text.strip()

    writer.writerow([href_url, time, link])

file.close()
