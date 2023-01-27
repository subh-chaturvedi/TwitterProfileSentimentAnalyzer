import requests
import pandas as pd
import json
import ast
import yaml

import os
print(os.listdir())

# Creating the right URL

def create_twitter_url(username):
    handle = username
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        mrf, q
    )
    
    return url


#Authenticating and connecting to the Twitter API
def process_yaml():
    with open("./server/config.yaml") as file:
        return yaml.safe_load(file)

#access the bearer token from your config.yaml file
def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]

#connect to the Twitter API
def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    # print(response.json())
    return response.json()



def main(username):
    url = create_twitter_url(username)
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    res_json = twitter_auth_and_connect(bearer_token, url)

    # print(res_json)

    with open("./server/tweetsdata.json","w") as f:
        f.write(json.dumps(res_json["data"],indent=4))
        

if __name__ == "__main__":
    main("devanshu_yadav")
    print("running in main, uninteded")

