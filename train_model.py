"""
train_model.py
Trains a simple RandomForest classifier on Crop_recommendation.csv
and saves it as model.pkl so app.py can load it and make predictions.

Run this once before starting the Flask app:
    python train_model.py
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# 1. Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# 2. Features (X) and target (y)
FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
X = df[FEATURES]
y = df["label"]

# 3. Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Train a simple RandomForest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 5. Check accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model trained. Test accuracy: {acc * 100:.2f}%")

# 6. Save the trained model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Saved trained model to model.pkl")
