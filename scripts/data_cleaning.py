import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):

    df = df.drop_duplicates()
    df=df.fillna(0)
    return df

def save_data(df, path):
    df.to_csv(path, index=False)
