import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("https://raw.githubusercontent.com/wongwara/flight-streamlit-at3/main/data/sample_itineraries.csv?token=GHSAT0AAAAAACETSXPAZBNEACHN4ZUWZIW4ZKISTOA")

#transform date column: searchDate
df['searchDate'] = pd.to_datetime(df['searchDate'])
df['searchDate_day'] = df['searchDate'].dt.day
df['searchDate_month'] = df['searchDate'].dt.month
df['searchDate_year'] = df['searchDate'].dt.year

#transform date column: flightDate
df['flightDate'] = pd.to_datetime(df['flightDate'])
df['flightDate_day'] = df['flightDate'].dt.day
df['flightDate_month'] = df['flightDate'].dt.month
df['flightDate_year'] = df['flightDate'].dt.year

#drop date cols
df = df.drop(columns=['searchDate', 'flightDate'])
df['DepartTime'] = df['segmentsDepartureTimeEpochSeconds'].apply(lambda x: x[0])

df = df[['totalTravelDistance', 'isNonStop', 'isBasicEconomy', 'startingAirport', 'destinationAirport', 'segmentsCabinCode','flightDate_day', 'flightDate_month', 'flightDate_year',
                         'DepartTime_hour', 'DepartTime_minute', 'DepartTime_second','totalFare']]

