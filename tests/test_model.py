import joblib
import pandas as pd

def test_model_prediction():
    # Load the model we trained
    model = joblib.load("models/model_v1.pkl")
    
    # Create one fake 'flower' to test (4 measurements)
   # This version includes the column names so the model doesn't complain
    cols = ['sepal_length_(cm)', 'sepal_width_(cm)', 'petal_length_(cm)', 'petal_width_(cm)']
    fake_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=cols)
    prediction = model.predict(fake_data)
    
    # Check if it gives us a result (0, 1, or 2)
    assert len(prediction) == 1