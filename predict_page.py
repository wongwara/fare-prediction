import streamlit as st
import pandas as pd
import re
from datetime import datetime

# from prediction import load_model
# data = load_model()
# regressor_loaded = data["model"]

def show_predict_page():
    st.title(" ✈️ Fare Prediction")
    st.write(""" This project is for the user and students to search the total fare from related information""")
    st.subheader("We need some information to predict the total Fare for your trip")

    # Input search date
    searchDate = st.date_input("Search Date", value=datetime.today(), format="YYYY-MM-DD")
    # Input flight date with a calendar widget
    flightDate = st.date_input("Flight Date", value=datetime.today(), format="YYYY-MM-DD")
    # Starting Airport
    airport_dict = {
        'OAK - Oakland International Airport':15,
        'DEN - Denver International Airport':3,
        'LGA - LaGuardia Airport':10,
        'LAX - Los Angeles International Airport':9,
        'ATL - Hartsfield-Jackson Atlanta International Airport':0,
        'CLT - Charlotte Douglas International Airport':2,
        'PHL - Philadelphia International Airport':13,
        'DTW - Detroit Metropolitan Wayne County Airport':5,
        'IAD - Washington Dulles International Airport':7,
        'JFK - John F. Kennedy International Airport':8,
        'DFW - Dallas/Fort Worth International Airport':4,
        'BOS - Logan International Airport':1,
        'EWR - Newark Liberty International Airport':6,
        'SFO - San Francisco International Airport':14,
        'ORD - O Hare International Airport':12,
        'MIA - Miami International Airport':11
            }
    airport_options = list(airport_dict.keys())
    starting_airport = st.selectbox("Starting Airport", airport_options)
    startingAirport = airport_dict[starting_airport]
    
    destination_airport = st.selectbox("Destination Airport", airport_options)
    destinationAirport = airport_dict[destination_airport]

    # Input departure time with hours, minutes, and seconds
    departure_hour = st.selectbox("Departure Hour", list(range(24)))
    departure_minute = st.selectbox("Departure Minute", list(range(60)))
    departure_second = st.selectbox("Departure Second", list(range(60)))

    # Combine the selected values into a datetime object
    departure_time = f"{departure_hour:02d}:{departure_minute:02d}:{departure_second:02d}"
        
    #Input cabin code
    cabin_dict = {'coach - coach':0,
                  'coach - coach - coach':1,
                  'coach':2,
                  'coach - coach - premium coach':3,
                  'first - first - first':4,
                  'coach - coach - coach - coach':5,
                  'coach - first - first':6,
                  'coach - premium coach - premium coach':7,
                  'coach - first - coach':8,
                  'first - first - coach':9,
                  'coach - business - business':10,
                  'business - coach':11,
                  'coach - premium coach - coach':12,
                  'first - first':13,
                  'first - coach':14,
                  'coach - coach - first':15,
                  'coach - business':16,
                  'business - coach - coach':17,
                  'business - business':18,
                  'first - coach - coach':19,
                  'coach - business - coach':20,
                  'first - coach - first':21,
                  'coach - coach - business':22,
                  'coach - premium coach':23,
                  'premium coach':24,
                  'business - business - coach':25,
                  'coach - first':26,
                  'business - coach - business':27,
                  'first':28,
                  'premium coach - premium coach':29,
                  'coach - coach - coach - premium coach':30,
                  'premium coach - coach':31,
                  'premium coach - coach - coach':32,
                  'business':33,
                  'first - coach - business':34,
                  'coach - coach - coach - first':35,
                  'premium coach - premium coach - premium coach':36,
                  'premium coach - premium coach - coach':37,
                  'first - business':38,
                  'first - first - coach - coach':39,
                  'first - coach - coach - coach':40,
                  'premium coach - coach - coach - coach':41,
                  'premium coach - first':42,
                  'coach - business - first':43,
                  'business - first':44,
                  'business - first - first':45,
                  'premium coach - business - coach':46,
                  'coach - coach - first - coach':47,
                  'coach - coach - premium coach - premium coach':48,
                  'coach - coach - first - first':49,
                  'coach - coach - premium coach - coach':50,
                  'coach - coach - business - coach':51
                 }
    cabin_options = list(cabin_dict.keys())
    cabin = st.selectbox("cabin code", cabin_options)
    segmentsCabinCode = cabin_dict[cabin]
    ok = st.button("Calculate total fare for your trip")
    if ok:
        X = pd.DataFrame({
        'searchDate':[searchDate],
        'flightDate':[flightDate],
        'startingAirport':[startingAirport],
        'destinationAirport':[destinationAirport],
        'departuretime':[departuretime],
        'SegmentsCabincode':[segmentsCabinCode]
        })
    prediction = regressor_loaded.predict(X)
    prediction = np.round(prediction, 2)  # Round the value to two digits
    prediction_str = str(prediction[0])  # Convert to string
    st.write(f"the predict total fare spending for your trip would be {prediction_str}$")
    
    # Example usage of the collected inputs
    st.write("Selected Flight Date:", flight_date)
    st.write("Cabin Code:", segmentsCabinCode)
    st.write("Starting Airport:", starting_airport)
    st.write("Destination Airport:", destination_airport)
    st.write("Departure Time:", departure_time)
