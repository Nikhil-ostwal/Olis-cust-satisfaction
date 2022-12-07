import streamlit as st
import pandas as pd

df = pd.read_csv("preprocessed_data.csv")

st.markdown("## Here you can explore the data set. ")

st.markdown("Select the type of insight to look into from the left panel.")

if st.sidebar.button('Dataset Quick Look'):
    st.subheader('Dataset Quick Look:')
    st.write(df.head())           
if st.sidebar.button('Statistical Description'):
    st.subheader('Statistical Data Descripition')
    st.write(df.describe())
if st.sidebar.button('Missing Values'):
    st.subheader('Missing values')
    st.write(df.isnull().sum())
if st.sidebar.button('Corelation'):
    st.subheader('Corelation between the features')
    st.write(df.corr())    



