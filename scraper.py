from twitter_scraper_selenium import scrape_profile
import json
import pandas as pd


def writeToJson(data):
    with open("./server/data_new.json", 'w') as f:
        data.to_json(f, orient='records')


def fixer(data):
        # Create a list to hold the flattened data

    jsonData = json.loads(data)
    
    flat_data = []

    # Iterate through each tweet in the JSON data
    for tweet_id, tweet_data in jsonData.items():
    # Create a dictionary to store the tweet's attributes
        tweet_dict = {}
        for key, value in tweet_data.items():
            tweet_dict[key] = value
        flat_data.append(tweet_dict)

        # Create the DataFrame from the flattened data
        df = pd.DataFrame(flat_data)
    
    return df

def main(username):
    print("Started Scraping")
    try:
        data = scrape_profile(twitter_username=username,output_format="json",browser="firefox",tweets_count=10)
    except:
        
        print("Twitter Scraping Error")
        return

    df = fixer(data)
    writeToJson(df)



if __name__ == "__main__":
    main("microsoft")
    print("Written Successfully in main instance")