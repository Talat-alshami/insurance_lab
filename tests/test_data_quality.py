import pandas as pd
from pathlib import Path
import pytest

clean_data_path = Path('data/processed/insurance_clean.csv')

@pytest.fixture
def clean_df():
    assert clean_data_path.exists()
    return pd.read_csv(clean_data_path) 

def test_no_duplicated(clean_df):
    assert clean_df.duplicated().sum() == 0
    
def test_no_missing_value(clean_df):
    assert clean_df.isna().sum().sum() == 0
    
def test_valid_ranges(clean_df):
    assert (clean_df['age'] >= 18).all()
    assert (clean_df['bmi'] > 0).all()
    assert (clean_df['charges'] > 0).all()
    
def test_correct_shape(clean_df):
    assert clean_df.shape[0] == 1337

