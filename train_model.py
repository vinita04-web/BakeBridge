import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv('bakery/dataset/orders.csv')

# Features
X = df[['price', 'quantity']]

# Target
y = df['category']

# Convert text to numbers
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy * 100)

# Save model
joblib.dump(model, 'bakery/model.pkl')
joblib.dump(encoder, 'bakery/encoder.pkl')

print("Model Trained Successfully")