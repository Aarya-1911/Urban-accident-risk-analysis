
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Add cleaning steps here if needed
    df = df.drop_duplicates()
    return df

def save_data(df, path):
    df.to_csv(path, index=False)
