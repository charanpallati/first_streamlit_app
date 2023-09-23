import streamlit
import pandas as pd
streamlit.header("Menu")

streamlit.title("Breakfast favorites")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
