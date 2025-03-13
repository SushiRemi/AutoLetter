#####################################################
#
#   Do not overuse/spam api, may risk being reviewed
#   for suspicious activity by LinkedIn 
#
#####################################################
 
import json
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

default_evade()

# GET user id in order to get data
profile = api.get_user_profile(use_cache=False)
print(profile)

# retrieve publicID
public_identifier = profile.get('miniProfile', {}).get('publicIdentifier', None)
print(public_identifier)
default_evade()

# GET data from user profile
user_data = api.get_profile(public_id=public_identifier)

# put user data into json format
with open('userdata_cache.json', 'w') as f:
    json.dump(user_data, f, indent=4)



