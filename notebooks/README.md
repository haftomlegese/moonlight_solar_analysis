Exploratory Data Analysis (EDA) - Solar Radiation and Environmental Measurements
Overview
This project involves conducting Exploratory Data Analysis (EDA) on solar radiation and environmental measurement datasets for three locations: Benin, Sierra Leone, and Togo. The analysis is performed using Python with Anaconda Notebook, focusing on data cleaning, visualization, and insights generation to support strategic decision-making for renewable energy investments.

Files
EDA.ipynb: Jupyter Notebook containing the Python code for data loading, cleaning, and analysis.
benin_data.csv, sierra_leone_data.csv, togo_data.csv: CSV files containing raw data for each location.
Analysis Steps

1. Data Loading
Imported necessary libraries (pandas, matplotlib, seaborn).
Loaded the datasets for Benin, Sierra Leone, and Togo into Pandas DataFrames.
python
Copy code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
benin_df = pd.read_csv('benin_data.csv')
sierra_leone_df = pd.read_csv('sierra_leone_data.csv')
togo_df = pd.read_csv('togo_data.csv')


2. Exploratory Data Analysis (EDA)
Data Quality Check
Checked for missing values, outliers, and incorrect entries in key columns (GHI, DNI, DHI).
python
Copy code
# Check for missing values in GHI, DNI, DHI columns
print("Benin Dataset - Missing Values:")
print(benin_df[['GHI', 'DNI', 'DHI']].isnull().sum())

print("\nSierra Leone Dataset - Missing Values:")
print(sierra_leone_df[['GHI', 'DNI', 'DHI']].isnull().sum())

print("\nTogo Dataset - Missing Values:")
print(togo_df[['GHI', 'DNI', 'DHI']].isnull().sum())
Data Cleaning
Handled missing values and outliers by imputing values or removing rows based on defined criteria.
python
Copy code
# Example: Impute missing values with mean
benin_df['GHI'].fillna(benin_df['GHI'].mean(), inplace=True)
sierra_leone_df['GHI'].fillna(sierra_leone_df['GHI'].mean(), inplace=True)
togo_df['GHI'].fillna(togo_df['GHI'].mean(), inplace=True)

# Example: Remove outliers using IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_clean = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df_clean

# Clean datasets by removing outliers in 'GHI' column
benin_df_clean = remove_outliers(benin_df, 'GHI')
sierra_leone_df_clean = remove_outliers(sierra_leone_df, 'GHI')
togo_df_clean = remove_outliers(togo_df, 'GHI')
Visualization
Generated visualizations (histograms, scatter plots, box plots) to explore relationships and patterns in the data.
python
Copy code
# Example: Create scatter plot for GHI vs. Tamb
plt.figure(figsize=(8, 6))
sns.scatterplot(x='GHI', y='Tamb', data=benin_df_clean, label='Benin', color='blue', alpha=0.7)
sns.scatterplot(x='GHI', y='Tamb', data=sierra_leone_df_clean, label='Sierra Leone', color='green', alpha=0.7)
sns.scatterplot(x='GHI', y='Tamb', data=togo_df_clean, label='Togo', color='red', alpha=0.7)
plt.title('GHI vs. Tamb')
plt.xlabel('Global Horizontal Irradiance (GHI)')
plt.ylabel('Ambient Temperature (Tamb)')
plt.legend()
plt.show()
Conclusion
This README file documents the Exploratory Data Analysis (EDA) performed on solar radiation and environmental measurement datasets for Benin, Sierra Leone, and Togo. The analysis includes data loading, cleaning, and visualization steps using Python with Anaconda Notebook. The findings from this analysis can inform strategic decision-making for renewable energy investments in these locations.