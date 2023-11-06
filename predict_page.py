import streamlit as st
import pandas as pd
import re

def show_predict_page():
    st.title("🤖 Salary Prediction")
    st.write(""" This project is for the job-seeker and students to searching the expected salary from related information, such as location or job subclassification""")
    st.subheader("We need some information to predict the salary")
