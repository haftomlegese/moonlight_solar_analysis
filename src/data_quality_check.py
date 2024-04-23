import pandas as pd
import os


def check_missing_values(df):
    """
    Check for missing values in the DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame.

    Returns:
        dict: Dictionary containing column names with missing values and their counts.
    """
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    return missing_values.to_dict()

def detect_outliers(df, columns):
    """
    Detect outliers in specified columns of the DataFrame using z-score method.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        columns (list): List of column names to check for outliers.

    Returns:
        dict: Dictionary containing column names and corresponding outlier counts.
    """
    outlier_counts = {}
    z_score_threshold = 3

    for col in columns:
        z_scores = ((df[col] - df[col].mean()) / df[col].std()).abs()
        outlier_count = (z_scores > z_score_threshold).sum()
        outlier_counts[col] = outlier_count

    return outlier_counts

def check_incorrect_entries(df, columns, condition):
    """
    Check for incorrect entries in specified columns based on a condition.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        columns (list): List of column names to check.
        condition (callable): Condition function to apply to each value in the specified columns.

    Returns:
        dict: Dictionary containing column names and counts of incorrect entries.
    """
    incorrect_counts = {}

    for col in columns:
        incorrect_mask = ~df[col].apply(condition)
        incorrect_count = incorrect_mask.sum()
        incorrect_counts[col] = incorrect_count

    return incorrect_counts


def perform_data_quality_checks(file_path):
    """
    Perform data quality checks on a dataset.

    Args:
        file_path (str): Path to the CSV file containing the dataset.

    Returns:
        bool: True if data quality checks pass, False otherwise.
    """
    # Load data from CSV file into DataFrame
    df = pd.read_csv(file_path)
    file_name = os.path.basename(file_path)
    
    # Data Quality Checks
    missing_values = check_missing_values(df)
    if missing_values:
        print(f"Missing Values in '{file_name}':")
        print(missing_values)
        print()
        return False

    outlier_counts = detect_outliers(df, ['GHI', 'DNI', 'DHI'])
    if outlier_counts:
        print(f"Outliers in '{file_name}':")
        print(outlier_counts)
        print()
        return False

    # Check for negative values in specified columns
    negative_value_condition = lambda x: x < 0
    incorrect_entries = check_incorrect_entries(df, ['GHI', 'DNI', 'DHI'], negative_value_condition)
    if incorrect_entries:
        print(f"Incorrect Entries (Negative Values) in '{file_name}':")
        print(incorrect_entries)
        print()
        return False

    return True