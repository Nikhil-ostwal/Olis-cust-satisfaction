import streamlit as st
import pandas as pd

df = pd.read_csv("preprocessed_data.csv")
st.set_page_config(layout="wide")
st.markdown("## Here you can get an quick overview of the clean dataset")

col1, col2, col3, col4 = st.columns(4)
        
st.markdown("Select the choice of insight from the left panel:")

if st.sidebar.button('Dataset Quick Look'):
    st.subheader('Dataset Quick Look:')
    st.write(df.head())           
if st.sidebar.button('Statistical Description'):
    st.subheader('Statistical Data Descripition')
    st.write(df.describe())
if st.sidebar.button('Missing Values'):
    st.subheader('Sum of Missing values in each column')
    st.write(df.isnull().sum())
if st.sidebar.button('Corelation'):
    st.subheader('Corelation between the features')
    st.write(df.corr())



# with col1:
#     st.header("A column")
#     st.button('BUT 1')
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A col2")
#     st.button('But 2')
#     st.image("https://static.streamlit.io/examples/dog.jpg")



