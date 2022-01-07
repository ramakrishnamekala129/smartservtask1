import pandas as pd
import streamlit as st
import plotly.express as px
import os

@st.cache
def get_data(url):
    #url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
    df=pd.read_json(url)
    df=df['products']
    #df=pd.DataFrame(df)
    df = pd.json_normalize(df)
    df['price']=pd.to_numeric(df['price'])
    df['popularity']=pd.to_numeric(df['popularity'])
    df['title']=df['title'].apply(str)
    return df



#df = get_data()

st.title("Products Display")

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

#filename = file_selector()
#st.write('You selected `%s`' % filename)
h=st.file_uploader('Step 1 Upload File',type=['json','csv'])
if h is not None:
	option = st.selectbox('Step 2 File Format',['JSON','CSV'])

	if option=='CSV':
		k = pd.read_csv(h)
		k=pd.DataFrame(k)
		#print(k)
	elif option=='JSON':
		k=get_data(h)
	#if k:
	options = st.multiselect('Step 3 Select Columns to be Displayed',k.columns)
	#k=pd.DataFrame(h)
	if options is not None:
		dataframe=k[list(options)]
		st.dataframe(dataframe)