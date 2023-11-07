import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import seaborn as sns
import numpy as np

def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/wongwara/fare-prediction/main/data/sample_itineraries.csv")
    
    return df

df = load_data()

def show_explore_page():
    st.title("💰 Fare Prediction")
  
    st.write(
        """ 
        The task is to build a data product that will help users in the USA to better estimate their local travel airfare. Users will be able to provide details of their trip and the app will predict the expected flight fare.
        """
    ) 
    st.write(
        """
             Therefore, the objective of this project would be to develop a machine learning model that accepts airport name and flightdate return the predict total fare.
             """
            )
    import matplotlib.pyplot as plt
    st.subheader("Historical Total Fare Trends")
    # Sort the DataFrame by 'flightdate' to ensure it's in chronological order
    df.sort_values('flightDate', inplace=True)

    # Create a line plot
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    plt.plot(df['flightDate'], df['totalFare'], label='Total Fare', color='b', marker='o')
    plt.title('Total Fare Over Time')
    plt.xlabel('Flight Date')
    plt.ylabel('Total Fare')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()


