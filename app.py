
import streamlit as st

# Title
st.title("Business Dashboard with Streamlit Layouts")

# Objective
msg = "## Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard."
st.write(msg)

col1, col2 = st.columns(2)
with col1:
    st.header("Q1 2024")
with col2:
    st.header("Q2 2024")
