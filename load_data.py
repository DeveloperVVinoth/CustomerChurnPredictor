import pandas as pd

# Load the dataset
df = pd.read_csv("telco_churn.csv")

# Show shape and columns
print("✅ Dataset loaded successfully!")
print("\n🔢 Rows and Columns:", df.shape)

# Display first 5 rows
print("\n🧾 First 5 rows:")
print(df.head())

# Data types and missing values
print("\n📂 Data Types:")
print(df.dtypes)

print("\n❌ Missing Values:")
print(df.isnull().sum())