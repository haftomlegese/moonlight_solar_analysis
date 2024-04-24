import streamlit as st
import pandas as pd
import plotly.express as px

# Load data functions (assuming data is stored locally)
def load_benin_data():
    return pd.read_csv('data/benin-malanville.csv')

def load_sierra_leone_data():
    return pd.read_csv('data/sierraleone-bumbuna.csv')

def load_togo_data():
    return pd.read_csv('data/togo-dapaong_qc.csv')


# Title and description
st.title('Solar Radiation and Environmental Measurements Dashboard')
st.write('Explore and visualize solar radiation and environmental data for Benin, Sierra Leone, and Togo.')

# Sidebar for dataset selection
location = st.sidebar.selectbox('Select Location', ['Benin', 'Sierra Leone', 'Togo'])

# Load data based on selection
if location == 'Benin':
    selected_df = load_benin_data()
elif location == 'Sierra Leone':
    selected_df = load_sierra_leone_data()
else:
    selected_df = load_togo_data()

# Show dataset information
st.subheader(f'Selected Location: {location}')

def show_full_dataset():
  st.dataframe(selected_df.copy())  # Avoid modifying original data

if st.button('Show Full Dataset'):
  show_full_dataset()

# Data Cleaning and Preprocessing

# Handle missing values (consider vectorized operations)
def fill_missing_values(df):
  return df.fillna(df.mean())

selected_df = fill_missing_values(selected_df.copy())

# Remove rows with entirely null comments
selected_df.dropna(subset=['Comments'], how='all', inplace=True)

# Remove outliers (using IQR method) for 'GHI' column
def remove_outliers(df, column):
  Q1 = df[column].quantile(0.25)
  Q3 = df[column].quantile(0.75)
  IQR = Q3 - Q1
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR
  df_clean = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
  return df_clean

# Apply data reduction strategy if dataset is large
if len(selected_df) > 10000:
  st.warning('Dataset is large. Applying data reduction strategy...')
  sample_size = st.sidebar.slider('Sample Size for Visualization', min_value=1000, max_value=len(selected_df), value=10000, key='sample_size')
  cleaned_df = remove_outliers(selected_df.sample(n=sample_size), 'GHI')
else:
  cleaned_df = remove_outliers(selected_df, 'GHI')

# Data Summary
st.subheader('Data Summary')
st.write(cleaned_df.describe())

# Data Visualization
st.subheader('Data Visualization')

# Scatter plot: GHI vs. Tamb
fig1 = px.scatter(cleaned_df, x='GHI', y='Tamb', title='Global Horizontal Irradiance (GHI) vs. Ambient Temperature (Tamb)')
st.plotly_chart(fig1)

# Histogram: GHI distribution
fig2 = px.histogram(cleaned_df, x='GHI', nbins=20, title='Histogram: Global Horizontal Irradiance (GHI)')
st.plotly_chart(fig2)

# Box plot: Solar Radiation (GHI, DNI, DHI)
fig3 = px.box(cleaned_df, y=['GHI', 'DNI', 'DHI'], title='Box Plot: Solar Radiation (GHI, DNI, DHI)')
st.plotly_chart(fig3)