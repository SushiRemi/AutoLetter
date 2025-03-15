#####################################################
#
#   Do not overuse/spam api, may risk being reviewed
#   for suspicious activity by LinkedIn 
#
#####################################################
 
import json
import os
from datetime import datetime
import random
import requests
from time import sleep
from linkedin_api import Linkedin

def default_evade():
    """
    A catch-all method to try and evade suspension from Linkedin.
    Currently, just delays the request by a random (bounded) time
    """
    sleep(random.randint(2, 5))  # sleep a random duration to try and evade suspention


# authenticate using any Linkedin user account credentials
email = input("Enter email: ")
password = input("Enter password: ")

api = Linkedin(email, password, refresh_cookies=True)

if api:
    default_evade()

# GET user id in order to get data
profile = api.get_user_profile(use_cache=False)

# retrieve publicID
public_identifier = profile.get('miniProfile', {}).get('publicIdentifier', None)
default_evade()

# GET data from user profile
if public_identifier:
    user_data = api.get_profile(public_id=public_identifier)
else:
    raise ValueError("Failed to get public identifier.")

# put user data into json format
with open('userdata.json', 'w') as user_file:
    json.dump(user_data, user_file, indent=4)


#########################################################################
#
# Goal: Give user's personalized job listing (recommended jobs) based on
# skills and location 
#
# We have 25 requests per month (10 job postings per request = 250)
#
#########################################################################

DATE_CREATED = datetime.now().strftime("%Y-%m")
FOLDER_NAME = f"jobs_{DATE_CREATED}"  # Folder to store job postings
os.makedirs(FOLDER_NAME, exist_ok=True)  # Create folder if it doesn't exist

# API details
MAX_REQUESTS_PER_MONTH = 25
MAX_REQUESTS_PER_CALL = 1
API_ENDPOINT = "https://daily-international-job-postings.p.rapidapi.com/api/v2/jobs/search"
API_HOST = "daily-international-job-postings.p.rapidapi.com"
API_KEY = "094cbd248cmsh1dc58a3054eecefp166012jsnc0a70c15b441"

# query parameters
parameters = {
  "dateCreated": DATE_CREATED,
  "countryCode": "us",
  "city": user_data.get("geoLocationName", "").split(",")[0].strip(),
  "state": user_data.get("geoLocationName", "").split(",")[1].strip() if "," in user_data.get("geoLocationName", "") else "",
  "title": user_data.get("experience", [{}])[0].get("title", ""),
  "skills": ",".join(skill["name"] for skill in user_data.get("skills", []) if "name" in skill) or ""
}

#print(f"Fetching job postings for date: {DATE_CREATED}")

PAGE = 1
TOTAL_COUNT = 0
i = 0
while i < MAX_REQUESTS_PER_CALL:
  # Add pagination to parameters
    parameters["page"] = PAGE
    #print(f"Querying: {API_ENDPOINT} with parameters {parameters}")

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

    # exit after getting job postings
    if PAGE > MAX_REQUESTS_PER_CALL:
        #print("Max requests reached. Exiting.")
        break
    # sleep due to throttled access to API
    sleep(1)
