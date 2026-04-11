import pandas as pd
from sklearn.datasets import load_iris
import os

def get_and_clean_data():
    # We are using the 'Iris' dataset (classic flower classification)
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # Cleaning: lowercase and underscores for column names
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    return df

if __name__ == "__main__":
    # This creates the data folder if it got deleted
    if not os.path.exists('data'):
        os.makedirs('data')
        
    data = get_and_clean_data()
    data.to_csv("data/raw_data.csv", index=False)
    print("✅ Success: Created data/raw_data.csv")