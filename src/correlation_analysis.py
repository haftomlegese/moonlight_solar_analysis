import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def calculate_correlation_matrix(df, variables):
    """
    Calculate the correlation matrix for specified variables in the DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing the dataset.
        variables (list): List of variable names for correlation analysis.

    Returns:
        pandas.DataFrame: Correlation matrix for the specified variables.
    """
    # Select subset of DataFrame with specified variables
    subset_df = df[variables]

    # Calculate correlation matrix
    correlation_matrix = subset_df.corr()

    return correlation_matrix

def visualize_correlation_matrix(correlation_matrix, dataset_name):
    """
    Visualize the correlation matrix as a heatmap.

    Args:
        correlation_matrix (pandas.DataFrame): Correlation matrix to visualize.
        dataset_name (str): Name of the dataset for plotting.

    Returns:
        None
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix for Dataset: {dataset_name}')
    plt.show()

def perform_correlation_analysis(file_paths):
    """
    Perform correlation analysis on multiple datasets.

    Args:
        datasets (list): List of tuples (df, dataset_name) containing DataFrame and dataset name.

    Returns:
        None
    """
    # Define variables of interest for correlation analysis
    variables_of_interest = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
    
    # Calculate and visualize correlation matrices for each dataset
    for file_path in file_paths:
        df = pd.read_csv(file_path) 
        file_name = os.path.basename(file_path)    
        
        # Calculate correlation matrix
        correlation_matrix = calculate_correlation_matrix(df, variables_of_interest)

        # Visualize correlation matrix
        visualize_correlation_matrix(correlation_matrix, file_name)