# Automated Model-Testing Pipeline

## 🚀 Project Overview
This project demonstrates a professional Software Engineering approach to Machine Learning. Instead of just training a model, it includes a full **automated testing suite** to ensure data integrity and model reliability.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, Scikit-Learn, Joblib
- **Testing:** Pytest

## 📂 Project Structure
- `data/`: Contains the raw dataset used for training.
- `models/`: Stores the trained `.pkl` model files.
- `src/`: Core logic for data preprocessing and model training.
- `tests/`: Automated test scripts to verify data and model health.

## 🚦 How to Run
1. **Install Dependencies:**
   `pip install -r requirements.txt`

2. **Train the Model:**
   `python src/train.py`

3. **Run Automated Tests:**
   `pytest`

## ✅ Quality Control
The project includes tests that check:
- If the dataset exists and has the correct columns.
- If the model can successfully make predictions on new data.