import pandas as pd

# Load the data
df = pd.read_csv("telco_churn.csv")

# Remove empty spaces in TotalCharges and convert to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"].replace(" ", pd.NA), errors='coerce')

# Drop rows where TotalCharges is still missing
df = df.dropna()

# Drop customerID column (not useful for prediction)
df = df.drop("customerID", axis=1)

# Convert target column 'Churn' to numeric: Yes = 1, No = 0
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# One-hot encode categorical features
df = pd.get_dummies(df, drop_first=True)

# Preview
print("✅ Preprocessing complete!")
print("\n🔢 Shape after encoding:", df.shape)
print("\n📊 First 5 rows:")
print(df.head())

# Save to CSV
df.to_csv("cleaned_telco.csv", index=False)
print("\n💾 Saved as cleaned_telco.csv")