import pandas as pd
import pytest
from app.dashboard import load_benin_data, load_sierra_leone_data, load_togo_data,fill_missing_values,remove_outliers

def test_load_benin_data():
    # Test that the function returns a DataFrame
    df = load_benin_data()
    assert isinstance(df, pd.DataFrame)

    # Test specific columns expected in the DataFrame
    expected_columns = [
        'Timestamp', 'GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 
        'RH', 'WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev', 'BP', 
        'Cleaning', 'Precipitation', 'TModA', 'TModB', 'Comments'
    ]
    assert df.columns.tolist() == expected_columns

        

def test_load_sierra_leone_data():
    # Test that the function returns a DataFrame
    df = load_sierra_leone_data()
    assert isinstance(df, pd.DataFrame)

    # Test specific columns expected in the DataFrame
    expected_columns = [
        'Timestamp', 'GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 
        'RH', 'WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev', 'BP', 
        'Cleaning', 'Precipitation', 'TModA', 'TModB', 'Comments'
    ]
    assert df.columns.tolist() == expected_columns

        
    
def test_load_togo_data():
    # Test that the function returns a DataFrame
    df = load_togo_data()
    assert isinstance(df, pd.DataFrame)

    # Test specific columns expected in the DataFrame
    expected_columns = [
        'Timestamp', 'GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 
        'RH', 'WS', 'WSgust', 'WSstdev', 'WD', 'WDstdev', 'BP', 
        'Cleaning', 'Precipitation', 'TModA', 'TModB', 'Comments'
    ]
    assert df.columns.tolist() == expected_columns

        
@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'GHI': [100, 200, 300, None, 500],
        'Comments': ['Good', 'Missing', 'OK', None, 'Excellent']
    })

def test_fill_missing_values(sample_data):
    filled_df = fill_missing_values(sample_data)
    assert filled_df['Comments'].isna().sum() == 0
    assert filled_df['Comments'].iloc[1] == 'Missing'  # Check specific value filled

def test_remove_outliers(sample_data):
    cleaned_df = remove_outliers(sample_data, 'GHI')
    assert cleaned_df['GHI'].max() <= 500
    assert cleaned_df['GHI'].min() >= 100
    
