import streamlit as st
import pandas as pd
import numpy as np

## title of the application 
st.title("Hello Streamlit App")

## display simple text
st.write("This is a simple text")

## creating a dataframe
df=pd.DataFrame({
    "first column":[1,2,3,4],
    "second column":[10,20,30,40]
})

## Display the dataframe
st.write("This is a simple dataframe")
st.write(df)

## create aline chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

