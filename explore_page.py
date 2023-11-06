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

