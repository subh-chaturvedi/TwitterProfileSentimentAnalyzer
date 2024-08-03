# Twitter Profile Sentiment Analyzer  

## Overview 

I have built this using a model with two microservices: a Flask server for backend operations and a Streamlit server for frontend operations. The Flask server handles data processing and sentiment analysis, while the Streamlit server provides a user-friendly interface for interacting with the application.

## Streamlit Server 

![stlt_screengrab](https://github.com/user-attachments/assets/e498c5c8-21f2-4a40-9c62-a7838a80f6ee)

### Setup and Deployment 

 
1. **Install Dependencies** :

```bash
pip install -r requirements.txt
```
 
2. **Start the Server** :

```bash
streamlit run index.py
```

## Flask Server 


### Flask Server Architecture 
 
1. **User Input** : The user provides a Twitter username through the Streamlit interface.
 
2. **Flask Endpoint** : The username is sent to the Flask server endpoint `/get_sentimentanalysis_overall`.
 
3. **Scraper Module** : The Flask server calls the `scraper.main(username)` function to scrape the latest tweets from the provided username.
 
4. **Data Processing** : The scraped tweets are processed using various utility functions in `utils.py`.
 
5. **Sentiment Analysis** : The processed tweets are analyzed for sentiment using a pre-trained model.
 
6. **Response** : The average sentiment score and corresponding sentiment label (Positive, Neutral, Negative) are returned to the Streamlit interface.



**Endpoints** : 
  - **GET `/`** : Returns the homepage.
 
  - **POST `/get_sentimentanalysis_overall`** : Accepts a Twitter username and returns the average sentiment score and label.

### Modules Descriptions 
 
- **server.py** : Main entry point for the Flask server.
 
- **utils.py** : Contains utility functions for data cleaning and sentiment analysis.
 
- **scraper.py** : Handles scraping tweets from Twitter.


### Utility Functions 
 
- **`valuetofeeling(i)`** : Converts a sentiment score to a textual representation.
 
- **`cleanREGEX(raw)`** : Cleans raw text using regex to remove HTML tags and special characters.
 
- **`deEmojify(x)`** : Removes emojis from the text.
 
- **`remove_punct(text)`** : Removes punctuation and numbers from the text.
 
- **`lower_case(df)`** : Converts text to lowercase.
 
- **`cleaner(df)`** : Applies a series of cleaning functions to the dataframe.
 
- **`sentimentanalyze(tweet)`** : Analyzes the sentiment of a tweet.
 
- **`load_saved_artifacts()`** : Loads the pre-trained model and vectorizer from disk.


