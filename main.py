import os
import streamlit as st  
from helper_functions.utility import check_password  
from helper_functions.llm import generate_data_store

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="talking flexi homepage"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("_talking flexi_")

st.markdown(
    """
    <style>
    .custom-text {
        font-family: 'Cursive', sans-serif;
        color: #A9A9A9;  
        font-size: 24px;  
    }
    </style>
    <p class="custom-text">Practise having difficult conversations with your
    boss or report! And learn more about how flexible work arrangements could
    work for you and your organisation.</p>
    """, unsafe_allow_html=True
)
