import streamlit as st 

st.write("Hello world")

st.sidebar.header("Welcome")
st.sidebar.text_input("Enter your email")
st.sidebar.text_input("Enter your password")

st.text_area("Submit recommendations")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    #["Yellow", "Red"],
)

st.write("You selected:", options)