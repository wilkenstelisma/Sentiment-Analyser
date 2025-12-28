
import streamlit as st
from textblob import TextBlob

def get_sentiment_score(statement):
    blob = TextBlob(statement)
    score = blob.sentiment.polarity
    if score > 0.75:
        return "Very Positive"
    elif score > 0.25:
        return "Positive"
    elif score < -0.75:
        return "Very Negative"
    elif score < -0.25:
        return "Negative"
    else:
        return "Neutral"

st.title("Sentiment Analysis App")
st.write("Enter a statement below to get its sentiment.")

if "run_trigger" not in st.session_state:
    st.session_state.run_trigger = False

def _trigger_run():
    # Run when Enter is pressed in the input box.
    st.session_state.run_trigger = True

user_input = st.text_input("Your Statement:", "", on_change=_trigger_run)

run_clicked = st.button("Analyze Sentiment")
should_run = run_clicked or st.session_state.run_trigger

if should_run:
    st.session_state.run_trigger = False
    if user_input:
        sentiment = get_sentiment_score(user_input)
        st.write(f"The sentiment of your statement is: **{sentiment}**")
    else:
        st.write("Please enter a statement to analyze.")
