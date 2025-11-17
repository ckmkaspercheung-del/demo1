
import streamlit as st

st.title("Retail business Dashboard")

st.header("header")
st.write("message")

age=st.number_input("Enter monthly Sales Target(in USD):"
                   min_value=0
				   max_value=100000
				   value=50000)
