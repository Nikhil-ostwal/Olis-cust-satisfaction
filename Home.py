import streamlit as st

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import pandas as pd 
import numpy as np

st.set_page_config(layout="wide")
st.title("Market Basket Project on E-Commerce")
#st.sidebar.subheader('Navigation')
st.markdown(" ## Problem statement:")
st.markdown("Most customers do not post a review rating or any comment after purchasing a product which is a challenge for any ecommerce platform to perform If a company predicts whether a customer liked/disliked a product so that they can recommend more similar and related products as well as they can decide whether or not a product should be sold at their end. This is crucial for ecommerce based company because they need to keep track of each product of each seller , so that none of products discourage their customers to come shop with them again.")
st.markdown("Moreover, if a specific product has very few rating and that too negetive, a company must not drop the product straight away, may be many customers who found the product to be useful haven't actually rated it.Some reasons could possibly be comparing your product review with those of your competitors beforehand,gaining lots of insight about the product and saving a lot of manual data pre-processin,maintain good customer relationship with company,lend gifts, offers and deals if the company feels the customer is going to break the relation.")
st.markdown("Objective of this case study is centered around predicting customer satisfaction with a product which can be deduced after predicting the product rating a user would rate after he/she makes a purchase.")
st.markdown("#### Dataset:")
st.markdown("This is a Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. We also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates. This is real commercial data, it has been anonymised, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses.")

st.markdown("The data set can be found [here](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")

