import pandas as pd
import numpy as np

dates = pd.date_range(start='2022-01-01', periods=365)
data = pd.DataFrame({
    'date': dates,
    'sales': np.random.randint(20, 100, size=365)
})

data.to_csv("data/retail_data.csv", index=False)
print("Dataset created successfully!")