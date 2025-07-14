# 📉 Customer Churn Predictor

This project predicts whether a telecom customer is likely to **churn (leave the service)** based on their usage data and account information. It uses a Logistic Regression model and a Streamlit web app for interactive predictions.

---

## 🗂️ Folder Structure

CustomerChurnPredictor/
│
├── app.py # (Optional/older version of Streamlit app)
├── churn_app.py # ✅ Streamlit app for live predictions
├── churn_logs.csv # CSV log of user predictions
├── churn_model.pkl # Trained ML model file
├── cleaned_telco.csv # Cleaned dataset after preprocessing
├── load_data.py # Script to load and preview raw dataset
├── preprocess_data.py # Cleans and prepares dataset
├── telco_churn.csv # 📦 Original dataset
├── train_model.py # Trains the churn prediction model
├── README.md # 📄 Project documentation (this file)

## 📊 Dataset Summary

- **Rows:** 7043  
- **Columns:** 21  
- **Target Variable:** `Churn` (Yes/No)

The dataset contains features like:

- Gender, SeniorCitizen, Tenure  
- Internet & Streaming services  
- Payment method, Contract type  
- Monthly & Total charges

---

## 🧠 Model Details

- **Model Used:** Logistic Regression  
- **Accuracy:** ~79%  
- **Precision (Churn):** 62%  
- **Recall (Churn):** 52%  
- **Trained On:** Balanced, cleaned dataset  
- **Saved As:** `churn_model.pkl`

---

## 🚀 How to Use

### 1. Install Requirements
pip install streamlit scikit-learn pandas

2. Run the Web App
streamlit run churn_app.py

4. Use the Interface
Enter customer details (age, charges, contract type, etc.)

Click Predict

Get the result: 🎯 Prediction: Will Churn / Won't Churn

All predictions are logged in churn_logs.csv

📈 Example Output
Age: 35
Monthly Charges: 60.50
Contract: Month-to-month
🎯 Prediction: ❌ Will Churn
🙋 Why This Project?
This project helps telecom companies:

Predict churn before it happens

Understand factors leading to customer loss

Take action (like offers, support) to retain users

👨‍💻 Author
Vinoth Viveki
🔗 GitHub Profile

📜 License
This project is licensed under the MIT License.
