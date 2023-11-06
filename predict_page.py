import streamlit as st
import pandas as pd
import re

def show_predict_page():
    st.title(" ✈️ Fare Prediction")
    st.write(""" This project is for the user and students to searching the total fare from related information""")
    st.subheader("We need some information to predict the total Fare for your trip")
