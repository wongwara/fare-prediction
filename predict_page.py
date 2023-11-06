import streamlit as st
import pandas as pd
import re
import datetime

def show_predict_page():
    st.title(" ✈️ Fare Prediction")
    st.write(""" This project is for the user and students to search the total fare from related information""")
    st.subheader("We need some information to predict the total Fare for your trip")

    # Input search date
    search_date = st.date_input("Search Date, value=datetime.today())
    # Input flight date with a calendar widget
    flight_date = st.date_input("Flight Date", use_container_width=True, value=pd.to_datetime("2023-11-01"))

    # Input cabin code
    cabin_code = st.text_input("Cabin Code", "Economy")

    # Input starting airport
    starting_airport = st.text_input("Starting Airport", "JFK")

    # Input destination airport
    destination_airport = st.text_input("Destination Airport", "LAX")

    # Example usage of the collected inputs
    st.write("Selected Flight Date:", flight_date)
    st.write("Cabin Code:", cabin_code)
    st.write("Starting Airport:", starting_airport)
    st.write("Destination Airport:", destination_airport)
