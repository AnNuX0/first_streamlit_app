import streamlit
import pandas

streamlit.title('Hello! World, StreamLet App here!')

streamlit.header('Header Text') 

streamlit.text(' 🥣 🥗 🐔 🥑 🍞')

streamlit.text('Text2!')
streamlit.text('Text3!')
streamlit.text('Text4!')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
