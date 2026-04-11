import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def train():
    # Load the data we just created
    df = pd.read_csv("data/raw_data.csv")
    X = df.drop("target", axis=1)
    y = df["target"]
    
    # Train a simple Random Forest model
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)
    
    # Create models folder if missing
    if not os.path.exists('models'):
        os.makedirs('models')
        
    # Save the model
    joblib.dump(model, "models/model_v1.pkl")
    print("✅ Success: Model saved to models/model_v1.pkl")

if __name__ == "__main__":
    train()