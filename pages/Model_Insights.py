import streamlit as st
import pandas as pd



st.set_page_config(layout="wide")
st.markdown("#### The table below gives an quick overview of the models chosen along with their performance")


table = pd.read_csv('../Olis-cust-satisfaction/models.csv')

st.table(table)