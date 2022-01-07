import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache
def get_data():
    url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    df=pd.read_json(url)
    df=df['products']
    #df=pd.DataFrame(df)
    df = pd.json_normalize(df)
    df['price']=pd.to_numeric(df['price'])
    df['popularity']=pd.to_numeric(df['popularity'])
    df['title']=df['title'].apply(str)
    return df



df = get_data()

st.title("Products Display")

st.dataframe(df)