# 📉 Customer Churn Prediction
This project uses machine learning to predict whether a customer is likely to **churn** (leave the service). It is based on a telecom dataset and uses logistic regression for classification.

## 📁 Project Structure
CustomerChurnPredictor/

├── load_data.py # Loads and previews the dataset
├── train_model.py # Trains and evaluates the ML model
├── churn_model.pkl # Saved trained model
├── churn_app.py # Streamlit web app for predictions
├── churn_logs.csv # Logs user inputs and predictions
├── README.md # Project documentation

## 📊 Dataset
The dataset contains customer info such as:

- Gender, Age, Tenure
- Internet Service, Streaming TV/Movie
- Monthly & Total Charges
- Churn (target variable)

📦 Rows: 7043
📦 Features: 21

## ✅ Features

- Cleaned and preprocessed data
- Trained a Logistic Regression classifier
- Evaluation report includes accuracy, precision, recall, and f1-score
- Streamlit web app for live predictions
- User input logs saved in `churn_logs.csv`

## 🚀 How to Run the App

1. Install required packages:
pip install -r requirements.txt
Run the Streamlit app:

streamlit run churn_app.py

🧠 Model Performance
Accuracy: 79%
Precision (Yes): 62%
Recall (Yes): 52%

🗂️ Example Prediction
Age: 40
Monthly Charges: 70
Contract: Month-to-Month
Prediction: ❌ Customer will churn

📌 Author
Vinoth Viveki
GitHub Profile

📜 License
This project is open-source under the MIT License.

Let me know once you've added it and committed/pushed to GitHub. Then I’ll mark **Day 25 complete** and start **Day 2
