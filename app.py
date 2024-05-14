import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit Page Configuration
st.set_page_config(page_title="Data Visualization App")

# Load Data Function
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    data = pd.read_csv(url)
    return data

# Data Loading with Caching
data = load_data()

# Sidebar for User Input
st.sidebar.header("Settings")
plot_type = st.sidebar.selectbox("Select the plot type:", ["Histogram", "Boxplot", "Scatterplot"])
column_data = st.sidebar.selectbox("Select the column to display:", data.columns)

# Display Data
st.write("## Data Overview", data.head())

# Plotting based on user selection
st.write(f"## {plot_type} of {column_data}")

if plot_type == "Histogram":
    fig, ax = plt.subplots()
    sns.histplot(data[column_data], kde=True, ax=ax)
    st.pyplot(fig)
elif plot_type == "Boxplot":
    fig, ax = plt.subplots()
    sns.boxplot(x=data[column_data], ax=ax)
    st.pyplot(fig)
elif plot_type == "Scatterplot":
    secondary_column = st.sidebar.selectbox("Select the secondary column for scatterplot:", data.columns)
    fig, ax = plt.subplots()
    sns.scatterplot(x=data[column_data], y=data[secondary_column], data=data, ax=ax)
    st.pyplot(fig)

# Reset Button in Sidebar
if st.sidebar.button('Reset App'):
    st.experimental_rerun()

# Display number of data points
st.sidebar.write("Total data points:", len(data))
