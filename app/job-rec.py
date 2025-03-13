#########################################################################
#
# Goal: Give user's personalized job listing (recommended jobs) based on
# skills and location 
#
#########################################################################

import os
import json
import requests
from time import sleep
from datetime import datetime

DATE_CREATED = datetime.now().strftime("%Y-%m")
FOLDER_NAME = f"jobs_{DATE_CREATED}"  # Folder to store job postings
os.makedirs(FOLDER_NAME, exist_ok=True)  # Create folder if it doesn't exist

# API details
MAX_REQUESTS_PER_MONTH = 25
MAX_REQUESTS_PER_CALL = 1
API_ENDPOINT = "https://daily-international-job-postings.p.rapidapi.com/api/v2/jobs/search"
API_HOST = "daily-international-job-postings.p.rapidapi.com"
API_KEY = "fd729b2308msh1a8e5b929f89989p1709eejsn76ff09d05425"

# query parameters
parameters = {
  "dateCreated": DATE_CREATED,
  "countryCode": "us",
  "city": "San Diego",
  "skills": "Java"
}

print(f"Fetching job postings for date: {DATE_CREATED}")

PAGE = 1
TOTAL_COUNT = 0
i = 0
while i < MAX_REQUESTS_PER_CALL:
  # Add pagination to parameters
    parameters["page"] = PAGE
    print(f"Querying: {API_ENDPOINT} with parameters {parameters}")

    try:
        response = requests.get(API_ENDPOINT, headers={
        "x-rapidapi-host": API_HOST,
        "x-rapidapi-key": API_KEY
        }, params = parameters)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"ERROR: Failed to fetch jobs (Maybe the API_KEY): {e}")
        break

    data = response.json()
    TOTAL_COUNT = data.get("totalCount", 0)
    page_size = data.get("pageSize", 0)
    results = data.get("result", [])
    print(f" Found {len(results)} jobs of {TOTAL_COUNT} on page: {PAGE}")

    if not results:
        print("No more jobs found. Stopping.")
        break

    # save jobs to folder 
    for idx, job in enumerate(results):
        job_filename = os.path.join(FOLDER_NAME, f"job_{PAGE}_{idx}.json")
        with open(job_filename, "w") as job_file:
            json.dump(job, job_file, indent=4)

    if len(results) < page_size:
        break

    i += 1
    PAGE += 1
    if PAGE > MAX_REQUESTS_PER_CALL:
        print("Max requests reached. Exiting.")
        break
    # sleep due to throttled access to API
    sleep(1)