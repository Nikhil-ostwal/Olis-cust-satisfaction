from numpy import hstack
import streamlit as st
import pandas as pd





data = pd.read_csv("preprocessed_data.csv")


st.markdown("## Here you can perform prediction on the new data and check the model performance.")

st.markdown("Enter the product information below to predict the score")

#number = col1.number_input("Enter number")

#col1.markdown(type(number))

def fun_pred():
    st.write("Inside fun_pred()")




# Numerical Features Features

col1, col2 = st.columns(2)


payment_sequential = col1.number_input("Payment Sequential")

payment_installments = col1.number_input("Payment Installments ")

payment_value = col1.number_input("Payment Value ")

price = col1.number_input("Price ")

freight_value = col1.number_input("Freight Value")

product_name_length  = col1.number_input("Product Name Length")

product_description_length = col1.number_input("Product Description Length ")

product_photos_qty = col1.number_input("Product Pictures Qty ")

delivery_days = col1.number_input("Delivery Days ")

estimated_days = col1.number_input("Estimated Days")

ships_in = col1.number_input("Ships In ")

seller_popularity = col2.number_input("Seller popularity")


# Categorical Features

payment_type = col2.selectbox("Choose Payment Type", ['Credit card','voucher','boleto','Debit card'])

customer_state = col2.selectbox("Customer Sate", data.customer_state.unique())

seller_state = col2.selectbox("Seller state", data.seller_state.unique())

product_category_name = col2.selectbox("Product Category", data.product_category_name.unique())

arrival_time = col2.selectbox("Arrival Time", data.arrival_time.unique())

delivery_impression = col2.selectbox("Delivery Impression", data.delivery_impression.unique())

estimated_del_impression = col2.selectbox("Estimated Delivery Impression",data.estimated_del_impression.unique())

ship_impression = col2.selectbox("Ship Impression", data.ship_impression.unique())

existing_cust = col2.selectbox("Existing Customer", data.existing_cust.unique())



test_vec = hstack((payment_sequential,payment_installments,payment_value,price,
                      freight_value,product_name_length,product_description_length,
                      product_photos_qty,delivery_days,estimated_days,ships_in,
                      payment_type,customer_state,seller_state,product_category_name,
                      arrival_time,delivery_impression,estimated_del_impression,
                     ship_impression,seller_popularity))

#st.write(test_vec)

predict = st.button("Predict Customer Satisfaction Score!",on_click=fun_pred())

