import streamlit as st
import pandas as pd
import re
from datetime import datetime

def show_predict_page():
    st.title(" ✈️ Fare Prediction")
    st.write(""" This project is for the user and students to search the total fare from related information""")
    st.subheader("We need some information to predict the total Fare for your trip")

    # Input search date
    search_date = st.date_input("Search Date", value=datetime.today(), format="YYYY-MM-DD")
    # Input flight date with a calendar widget
    flight_date = st.date_input("Flight Date", value=datetime.today(), format="YYYY-MM-DD")
    # Starting Airport
    airport_dict = {
        'OAK: Oakland International Airport':15,
        'DEN: Denver International Airport':3,
        'LGA: LaGuardia Airport':10,
        'LAX: Los Angeles International Airport':9,
        'ATL: Hartsfield-Jackson Atlanta International Airport':0,
        'CLT: Charlotte Douglas International Airport':2,
        'PHL: Philadelphia International Airport':13,
        'DTW: Detroit Metropolitan Wayne County Airport':5,
        'IAD: Washington Dulles International Airport':7,
        'JFK: John F. Kennedy International Airport':8,
        'DFW: Dallas/Fort Worth International Airport':4,
        'BOS: Logan International Airport':1,
        'EWR: Newark Liberty International Airport':6,
        'SFO: San Francisco International Airport':14,
        'ORD: O Hare International Airport':12,
        'MIA: Miami International Airport':11
            }
        airport_options = list(airport_dict.keys())
        staring_airport = st.selectbox("Staring Airport", airport_options)
        startingAirport = airport_dict[staring_airport]
        destination_airport = st.selectbox("Destination Airport", airport_options)
        destinationAirport = airport_dict[destination_airport]
        
    #Input cabin code
    cabin_dict = {'coach||coach':0,
                  'coach||coach||coach':1,
                  'coach':2,
                  'coach||coach||premium coach':3,
                  'first||first||first':4,
                  'coach||coach||coach||coach':5,
                  'coach||first||first':6,
                  'coach||premium coach||premium coach':7,
                  'coach||first||coach''first||first||coach':8,
                  'coach||business||business':9,
                  'business||coach':10,
                  'coach||premium coach||coach':11,
                  'first||first':12,
                  'first||coach':13,
                  'coach||coach||first':14,
                  'coach||business':15,
                  'business||coach||coach':16,
                  'business||business':17,
                  'first||coach||coach':18,
                  'coach||business||coach':19,
                  'first||coach||first':20,
                  'coach||coach||business':21,
                  'coach||premium coach':22,
                  'premium coach':23,
                  'business||business||coach':24,
                  'coach||first':25,
                  'business||coach||business':26,
                  'first':27,
                  'premium coach||premium coach':28,
                  'coach||coach||coach||premium coach':29,
                  'premium coach||coach':30,
                  'premium coach||coach||coach':31,
                  'business':32,
                  'first||coach||business':33,
                  'coach||coach||coach||first':34,
                  'premium coach||premium coach||premium coach':35,
                  'premium coach||premium coach||coach':36,
                  'first||business':37,
                  'first||first||coach||coach':38,
                  'first||coach||coach||coach':39,
                  'premium coach||coach||coach||coach':40,
                  'premium coach||first':41,
                  'coach||business||first' :42,
                  'business||first':43,
                  'business||first||first':44,
                  'premium coach||business||coach':45,
                  'coach||coach||first||coach':46,
                  'coach||coach||premium coach||premium coach':47,
                  'coach||coach||first||first':48,
                  'coach||coach||premium coach||coach':49,
                  'coach||coach||business||coach':50
                 }
    cabin_options = list(cabin_dict.keys())
        cabin = st.selectbox("cabin code", cabin_options)
        segmentsCabinCode = cabin_dict[cabin]

    # Input starting airport
    starting_airport = st.text_input("Starting Airport", "JFK")

    # Input destination airport
    destination_airport = st.text_input("Destination Airport", "LAX")

    # Example usage of the collected inputs
    st.write("Selected Flight Date:", flight_date)
    st.write("Cabin Code:", cabin_code)
    st.write("Starting Airport:", starting_airport)
    st.write("Destination Airport:", destination_airport)
