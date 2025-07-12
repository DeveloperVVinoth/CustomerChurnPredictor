# Step 1: Import necessary libraries
import streamlit as st               # For building the app UI
import joblib                        # For loading the saved model
import numpy as np                   # For working with numeric arrays

# Step 2: Load the saved model
model = joblib.load("churn_model.pkl")

# Step 3: Set the title of the app
st.set_page_config(page_title="Customer Churn Predictor")
st.title("📞 Customer Churn Predictor")
st.write("Fill the details below to predict if the customer will **Churn** or **Stay**.")

# Step 4: Create a form for user inputs
with st.form("churn_form"):
    # Input fields
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["Yes", "No"])
    partner = st.selectbox("Has Partner", ["Yes", "No"])
    tenure = st.slider("Tenure (in months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

    # Submit button
    submitted = st.form_submit_button("Predict")

# Step 5: When user clicks the button
if submitted:
    # Convert categorical values to numeric
    gender_num = 1 if gender == "Male" else 0
    senior_num = 1 if senior == "Yes" else 0
    partner_num = 1 if partner == "Yes" else 0

    # Make a feature array with the input
    input_data = np.array([[gender_num, senior_num, partner_num, tenure, monthly_charges]])

    # Use the trained model to predict
    prediction = model.predict(input_data)[0]

    # Show the result
    if prediction == 1:
        st.error("❌ Prediction: Customer is likely to **Churn**.")
    else:
        st.success("✅ Prediction: Customer is likely to **Stay**.")