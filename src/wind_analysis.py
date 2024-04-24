import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_wind_speed(df, file_name):
    """
    Plot wind speed variables (WS, WSgust, WSstdev) over time.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['WS'], label='Wind Speed')
    plt.plot(df['Timestamp'], df['WSgust'], label='Wind Gust Speed')
    plt.plot(df['Timestamp'], df['WSstdev'], label='Wind Speed Standard Deviation')
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Speed (m/s)')
    plt.title(f'Wind Speed Over Time for Dataset: {file_name}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_wind_direction(df, file_name):
    """
    Plot wind direction variables (WD, WDstdev) over time.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['WD'], label='Wind Direction')
    plt.plot(df['Timestamp'], df['WDstdev'], label='Wind Direction Standard Deviation')
    plt.xlabel('Timestamp')
    plt.ylabel('Wind Direction (°N)')
    plt.title(f'Wind Direction Over Time for Dataset: {file_name}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def perform_wind_analysis(file_paths):
    """
    Perform wind analysis on the dataset.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.

    Returns:
        None
    
    """
    for file_path in file_paths:
        df = pd.read_csv(file_path) 
        file_name = os.path.basename(file_path)
        # Plot wind speed variables
        plot_wind_speed(df,file_name)

        # Plot wind direction variables
        plot_wind_direction(df,file_name)