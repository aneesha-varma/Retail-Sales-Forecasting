import pandas as pd
from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.model import train_model
from src.inventory import inventory_calc

df = load_data("data/retail_data.csv")
df = clean_data(df)
df = create_features(df)

X = df[['lag_1','lag_7','rolling_mean','day']]
y = df['sales']

model = train_model(X, y)

forecast = model.predict(X)

std = y.std()
ss, rop = inventory_calc(forecast, std, lead_time=7)

print("Safety Stock:", ss)
print("Reorder Point:", rop)