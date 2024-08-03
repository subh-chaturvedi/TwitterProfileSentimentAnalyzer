import pickle
import json
import numpy as np
import re
import string
import pandas as pd

__model = None
__vectorizer = None

def valuetofeeling(i):
    if (i <= -0.33):
        return "Negative"
    elif (i >= 0.33):
        return "Positive"
    else:
        return "Neutral"


def cleanREGEX(raw):
    result = re.sub("<[a][^>]*>(.+?)</[a]>", 'Link.', raw)
    result = re.sub('&gt;', "", result) # greater than sign
    result = re.sub('&#x27;', "'", result) # apostrophe
#     result = re.sub('&quot;', '"', result) 
    result = re.sub('&#x2F;', ' ', result)
    result = re.sub('<p>', ' ', result) # paragraph tag
    result = re.sub('<i>', ' ', result) #italics tag
    result = re.sub('</i>', '', result) 
    result = re.sub('&#62;', '', result)
    result = re.sub("\n", '', result) # newline 
    return result


def deEmojify(x):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'', x)

def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    text = re.sub(r"[^a-zA-Z0-9?!.,]+", ' ', text)
    return text

def lower_case(df):
    df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))

def cleaner(df):
    df['og_tweet'] = df.loc[:, 'tweet']
    df1 = df.copy().dropna()

    df1['tweet'] = df1['tweet'].apply(cleanREGEX)
    df1['tweet'] = df1['tweet'].apply(deEmojify)
    df1['tweet'] = df1['tweet'].apply(lambda x: remove_punct(x))

    return df1


def sentimentanalyze(tweet):
    
    data = [tweet]
    df = pd.DataFrame(data, columns=['tweet'])
    df = cleaner(df)

    dftest = df.copy()
    # print(df.head())
    
    from sklearn.feature_extraction.text import CountVectorizer
    
    test_matrix = __vectorizer.transform(dftest['tweet'])
    i=0

    prediction = int(__model.predict(test_matrix[i])[0])

    return prediction

    # print((__model.predict(test_matrix[i])[0], df['og_tweet'].iloc[i]))


def load_saved_artifacts():
    print("loading saved artifacts...start")

    global __model
    if __model is None:
        with open('./model/twittersentimentanalysis.pickle', 'rb') as f:
            __model = pickle.load(f)

    global __vectorizer
    if __vectorizer is None:
        with open('./model/vectorizer.pickle', 'rb') as f:
            __vectorizer = pickle.load(f)

    print("loading saved artifacts...done")


# load_saved_artifacts()
if __name__ == "__main__":
    load_saved_artifacts()
    print(sentimentanalyze("I am happy."))