import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 0,100, 25)
st.write("your age is:", age)
color = st.color_picker("Pick your favorite color:", "#00f900")
st.write("Your favorite color is:", color)

st.date_input("Select your birth date:")    
st.time_input("Select a time:")


choice = st.selectbox("choose your favourite language!:", options=["Python", "Java", "C++", "JavaScript"])
st.write("you selected:", choice,".")

multi_choice = st.multiselect("Select your preferred programming languages:", options=["Python", "Java", "C++", "JavaScript", "Ruby", "Go"])
st.write("You selected:", multi_choice)

uploaded_file = st.file_uploader("upload a file:", type=["csv", "txt", "xlsx"]  )

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)