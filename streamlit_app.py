import streamlit
import pandas as pd
import snowflake.connector
streamlit.header("Menu")

streamlit.title("Breakfast favorites")

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

## Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display the table
streamlit.dataframe(fruits_to_show)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.header("Fruit load list contains")
#streamlit.dataframe(my_data_row)


stremlit.header("The fruit load list contains:")

def get_fruit_load_list():
    with my_cur.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
if streamlit.button("Get Fruit load list"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
