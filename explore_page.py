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
    # Sort the DataFrame by 'flightdate' to ensure it's in chronological order
    df.sort_values('flightDate', inplace=True)

    # Create a line plot
    fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size as needed
    ax.plot(df['flightDate'], df['totalFare'], label='Total Fare', color='b', marker='o')
    ax.set_title('Total Fare Over Time')
    ax.set_xlabel('Flight Date')
    ax.set_ylabel('Total Fare')
    ax.grid(True)
    ax.legend()
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better readability

    # Display the plot in Streamlit
    st.pyplot(fig)


