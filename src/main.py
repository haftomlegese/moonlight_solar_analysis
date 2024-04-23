from data_summary import display_summary_statistics,calculate_summary_statistics


def main():
    # List of file paths for the datasets
    file_paths = ['../data/benin-malanville.csv', '../data/sierraleone-bumbuna.csv', '../data/togo-dapaong_qc.csv']

    # Calculate summary statistics for each dataset using utility function
    summary_stats_list = calculate_summary_statistics(file_paths)

    # Display summary statistics for each dataset
    display_summary_statistics(summary_stats_list)
    
if __name__ == "__main__":
    main()