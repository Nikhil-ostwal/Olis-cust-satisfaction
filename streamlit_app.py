# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()



# def main_page():
    
#     st.markdown("# Market Basket Project on E-Commerce")
#     st.markdown("Objective of this case study is centered around predicting customer satisfaction with a product which can be deduced after predicting the product rating a user would rate after he/she makes a purchase.")
#     st.sidebar.markdown("## Dashboard")
#     st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")
    







# st.header("Now you can explore the data set.")
# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading dataset...')
#     # Load 10,000 rows of data into the dataframe.
# df = pd.read_csv("preprocessed_data.csv", nrows = 100)
#     # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading palmerpenguins dataset...Completed!')

# if st.sidebar.checkbox("Show Raw Data Sample", False):
#     st.subheader('Raw data')
#     st.write(df.head())


