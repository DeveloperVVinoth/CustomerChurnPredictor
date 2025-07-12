import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import os

# Load model
model = joblib.load("churn_model.pkl")

st.set_page_config(page_title="Customer Churn Predictor")
st.title("💼 Customer Churn Predictor")
st.write("Enter customer details to predict whether they are likely to **Churn** or **Stay**.")

# Input form
with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Has Partner", ["No", "Yes"])
    dependents = st.selectbox("Has Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone = st.selectbox("Phone Service", ["No", "Yes"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    monthly = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
    total = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=1000.0)
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    submit = st.form_submit_button("Predict")

# On submit
if submit:
    # Encode input into a single row DataFrame
    input_dict = {
        "gender": [gender],
        "SeniorCitizen": [1 if senior == "Yes" else 0],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone],
        "InternetService": [internet],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total],
    }

    input_df = pd.DataFrame(input_dict)

    # One-hot encode and align with training columns
    df_encoded = pd.get_dummies(input_df)
    model_columns = model.feature_names_in_
    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[model_columns]

    # Make prediction
    pred = model.predict(df_encoded)[0]
    result = "🚨 Churn" if pred == 1 else "✅ Stay"

    st.success(f"🎯 Prediction: **{result}**")

    # Log prediction
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tenure": tenure,
        "monthly": monthly,
        "total": total,
        "prediction": result
    }

    log_file = "churn_logs.csv"
    if not os.path.exists(log_file):
        pd.DataFrame([log]).to_csv(log_file, index=False)
    else:
        pd.DataFrame([log]).to_csv(log_file, mode="a", index=False, header=False)
