from flask import Flask, request, jsonify, render_template
import utils
import scraper
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/get_sentimentanalysis_overall', methods=['GET','POST'])
def get_sentimentanalysis_overall():

    username = request.form['username']
    print("\nUsername requested ->",username)

    scraper.main(username)

    df = pd.read_json('./server/data_new.json')
    df['predictions'] = df['content'].apply(utils.sentimentanalyze)

    avg_sentiment = df["predictions"].mean()
    print(avg_sentiment, "Sentimental Analysis Successful")

    avg_sentiment_text = utils.valuetofeeling(avg_sentiment)

    response = jsonify({
        'avg_sentiment_float': round(avg_sentiment,2),
        'avg_sentiment_text': avg_sentiment_text
    })

    print("RESPONDED",response)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server...")
    utils.load_saved_artifacts()
    app.run(port=4996)
