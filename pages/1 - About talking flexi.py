import os
import streamlit as st  

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About talking flexi"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About _talking flexi_")

st.markdown(
    """
    <style>
    .custom-text {
        font-family: 'Cursive', sans-serif;
        color: #A9A9A9;  
        font-size: 24px;  
    }
    </style>
    <p class="custom-text">This section will cover the project scope, 
    objectives, data sources, and features.</p>
    """, unsafe_allow_html=True
)