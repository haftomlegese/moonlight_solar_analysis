import pandas as pd
from data_summary import display_summary_statistics,calculate_summary_statistics
from data_quality_check import perform_data_quality_checks
from time_series_analysis import perform_time_series_analysis


def main():
    # List of file paths for the datasets
    file_paths = ['../data/benin-malanville.csv', '../data/sierraleone-bumbuna.csv', '../data/togo-dapaong_qc.csv']

    try:       
        
        # Calculate summary statistics for each dataset using utility function
        summary_stats_list = calculate_summary_statistics(file_paths)

        # Display summary statistics for each dataset
        display_summary_statistics(summary_stats_list)
        
        # Perform data quality checks for each dataset
        for file_path in file_paths:
            perform_data_quality_checks(file_path)
            
        # Perform time series analysis for each dataset
        for file_path in file_paths:
            perform_time_series_analysis(file_path, True)
        

    except FileNotFoundError as e:
        # Handle file not found error
        print(f"Error: {e.strerror} - {e.filename}")
    except Exception as e:
        # Handle other exceptions
        print(f"Error: An unexpected error occurred - {e}")
    
if __name__ == "__main__":
    main()