from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model(X, y):
    # Create model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Train model
    model.fit(X, y)
    
    # Save model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")
    
    return model