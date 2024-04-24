import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_time_series(df, variable, ylabel, file_name):
    """
    Plot time series for a specific variable.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.
        variable (str): Name of the variable to plot (e.g., 'GHI', 'DNI', 'DHI', 'Tamb').
        ylabel (str): Label for the y-axis in the plot.

    Returns:
        None
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df[variable], marker='o', linestyle='-')
    plt.xlabel('Timestamp')
    plt.ylabel(ylabel)
    plt.title(f'Time Series Analysis: {variable} over Time for dataset {file_name}')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def perform_time_series_analysis(file_path, downsample=False, max_data_points=10000):
    """
    Perform time series analysis on the dataset.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.
        downsample (bool): Whether to downsample the data for faster plotting (default: False).
        max_data_points (int): Maximum number of data points to plot if downsampling (default: 1000).

    Returns:
        None
    """
    # Optionally downsample the data for faster plotting
    df = pd.read_csv(file_path)
    file_name = os.path.basename(file_path)
    if downsample and len(df) > max_data_points:
        df = df.sample(max_data_points)  # Randomly sample data points

    # Plot time series for specific variables
    plot_time_series(df, 'GHI', 'Global Horizontal Irradiance (W/m²)', file_name)
    plot_time_series(df, 'DNI', 'Direct Normal Irradiance (W/m²)', file_name)
    plot_time_series(df, 'DHI', 'Diffuse Horizontal Irradiance (W/m²)', file_name)
    plot_time_series(df, 'Tamb', 'Ambient Temperature (°C)', file_name)