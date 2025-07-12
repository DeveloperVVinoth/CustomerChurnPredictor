import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load preprocessed data
df = pd.read_csv("cleaned_telco.csv")

# Split features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)
print("✅ Model trained\n")
print("📊 Evaluation Report:\n")
print(report)

# Save model
joblib.dump(model, "churn_model.pkl")
print("\n💾 Model saved as churn_model.pkl")