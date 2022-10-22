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

href_url = []
time = []
job_location =[]
for cl_job in cl_jobs:

    href_url = cl_job.find(class_="result-title").text.strip()

    time = soup.find(class_="result-date").text.strip() #12:23

    job_location = soup.find(class_="result-hood").text.strip() #location (city)
    
    writer.writerow([href_url, time, job_location])

file.close()
