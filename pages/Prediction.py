import streamlit as st
import pandas as pd




df = pd.read_csv("preprocessed_data.csv")


st.markdown("## Here you can perform prediction on the test data and check the model performance.")

st.markdown("Select the type of insight to look into from the left panel.")