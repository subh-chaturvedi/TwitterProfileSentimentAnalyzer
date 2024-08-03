import streamlit as st
import requests

# Set the title of the web app
st.title('Twitter Analyzer App')

#Twitter logo GIF
twitter_giphy = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWk3OTZnY3pqdzE2b2xhNTR5OG5xc2VwMjhqc2RwMmtjdWRmbmtwOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SMKiEh9WDO6ze/giphy.gif"

#Ensuring that the twitter GIF is centered
#Utilized tables
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(twitter_giphy, width = 200)

title_alignment="""
<style>
h1 {
  text-align: center
}
body {
    text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)


# Add a text input box for entering the URL
url = st.text_input('Enter the Twitter username:')

def call_sentiment_api(url):
    # Make an API call
    apiURL = "https://subhchaturvedi.pythonanywhere.com/get_sentimentanalysis_overall" # Flask microservice URL
    response = requests.post(apiURL,data={'username': url})
    if response.status_code == 200:
        data = response.json()
        error_code = data.get('error')
        avg_sentiment = data.get('avg_sentiment_text')
        avg_sentiment_ft = data.get('avg_sentiment_float')
        if error_code==0:
            print('API call was successful!')
            st.write(f'Average Sentiment: {avg_sentiment} with score of {avg_sentiment_ft}')
        elif error_code==1:
            st.write("Hosting Server faced error code [1]. Please raise an issue.")
    else:
        st.write(f'Twitter Server currently busy, please try again later.')


# Add a submit button
if st.button('Submit'):
    if url:
        call_sentiment_api(url)
    else:
        st.write('Please enter a valid username.')
    
    



