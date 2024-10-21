import os
import streamlit as st  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="How it works"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("How it works")

st.markdown(
    """
    <style>
    .custom-text {
        font-family: 'Cursive', sans-serif;
        color: #A9A9A9;  
        font-size: 24px;  
    }
    </style>
    <p class="custom-text">This section will cover 
    comprehensive explanation of the data flows and implementation details, 
    including flowcharts for the process flows.</p>
    """, unsafe_allow_html=True
)