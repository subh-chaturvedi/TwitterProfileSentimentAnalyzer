from flask import Flask, request, jsonify
import utils
import pandas as pd
import retrival


# app = Flask(__name__)

# @app.route('get_semtimentanalysis_overall', methods=['GET','POST'])
# def get_semtimentanalysis_overall():

# username = request.form['username']
username = "LinusTech"
retrival.main(username)

df = pd.read_json('./server/tweetsdata.json')
utils.load_saved_artifacts()

print(df.head())

df['predictions'] = df['text'].apply(utils.sentimentanalyze)

print(df.head())

avg_sentiment = df["predictions"].mean()

print(avg_sentiment)

    # response = jsonify({
    #     'estimated_price': util.sentimentanalyze(tweet)
    # })