import streamlit as st 
import openai
openai.api_key = st.secrets["openai"]["api_key"] 

import os
from langsmith import Client

client = Client(api_key=st.secrets("LANGSMITH_API_KEY"))

#Avoid hardcoding API keys — use environment variables instead 

def sentiment_analysis(text): 
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Analyze the sentiment of the following text:\n\n{text}"}
            ],
            max_tokens=100
        )
        #return response["choices"][0]["message"]["content"] 
        print("Add response", response)
        #return response.choices[0].message["content"]
        return response.choices[0].message.content
        #return response
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Enter a text below to analyze its sentiment:")

user_input = st.text_area("Input text", "")

if st.button("Analyze Sentiment"): 
    if user_input.strip():
        sentiment = sentiment_analysis(user_input)
        st.success(f"**Sentiment analysis result:** {sentiment}")
    else:
        st.warning("Please enter some text to analyze.")
