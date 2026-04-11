import pandas as pd
import os

def test_csv_exists():
    # Check if the file was actually created
    assert os.path.exists("data/raw_data.csv")

def test_column_names():
    df = pd.read_csv("data/raw_data.csv")
    # If 'target' is missing, this test will FAIL
    assert "target" in df.columns