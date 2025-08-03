import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("employee_data.csv")

# Encode categorical columns
le_overtime = LabelEncoder()
df['OverTime'] = le_overtime.fit_transform(df['OverTime'])

le_attrition = LabelEncoder()
df['Attrition'] = le_attrition.fit_transform(df['Attrition'])  # Yes=1, No=0

# Features & target
X = df[['Age', 'JobSatisfaction', 'MonthlyIncome', 'YearsAtCompany', 'WorkLifeBalance', 'OverTime']]
y = df['Attrition']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
