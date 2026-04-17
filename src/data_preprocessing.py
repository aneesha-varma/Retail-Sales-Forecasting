import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def clean_data(df):
    df = df.dropna()
    df = df[df['sales'] >= 0]
    return df