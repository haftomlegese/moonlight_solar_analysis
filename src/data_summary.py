import pandas as pd
import os

def calculate_summary_statistics(file_paths):
    summary_stats_list = []

    for file_path in file_paths:
        try:
            # Load data from CSV file into DataFrame
            df = pd.read_csv(file_path)

            # Calculate summary statistics for numeric columns in the DataFrame
            summary_stats = df.describe()

            # Extract file name from the file path
            file_name = os.path.basename(file_path)

            # Append summary statistics to the list along with the file name
            summary_stats_list.append((file_name, summary_stats))

        except FileNotFoundError:
            # Handle file not found error
            print(f"Error: File not found at path '{file_path}'")

    return summary_stats_list

def display_summary_statistics(summary_stats_list):
    for file_name, summary_stats in summary_stats_list:
        print(f"Summary Statistics for Dataset '{file_name}':")
        print(summary_stats)
        print("\n")