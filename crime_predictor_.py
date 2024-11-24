# -*- coding: utf-8 -*-
"""crime predictor .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YL-1tnvKK2RmWaMOmZjjhPeyL8v2Ir3W
"""

from sklearn.preprocessing import LabelEncoder

# Initialize label encoders
le_crime_type = LabelEncoder()
le_area = LabelEncoder()

# Check and encode categorical columns
if 'Crime Type' in crime_data.columns:
    crime_data['Crime Type'] = le_crime_type.fit_transform(crime_data['Crime Type'])
if 'Area' in crime_data.columns:
    crime_data['Area'] = le_area.fit_transform(crime_data['Area'])

# Display the updated dataset
print(crime_data.head())

# Print unique values for categorical columns
print("Unique values in 'Crime Outcome':", crime_data['Crime Outcome'].unique() if 'Crime Outcome' in crime_data.columns else "Column not found.")
print("Unique values in 'Crime Type':", crime_data['Crime Type'].unique() if 'Crime Type' in crime_data.columns else "Column not found.")
print("Unique values in 'Area':", crime_data['Area'].unique() if 'Area' in crime_data.columns else "Column not found.")

from sklearn.model_selection import train_test_split

# Define your features (X) and target variable (y)
X = crime_data.drop("Crime Outcome", axis=1)  # All columns except 'Crime Outcome'
y = crime_data["Crime Outcome"]  # Target variable

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Show the sizes of the splits
print(f"Training data size: {X_train.shape}")
print(f"Test data size: {X_test.shape}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
crime_data = pd.read_csv("/content/drive/MyDrive/crime predictor/synthetic_crime_data_coimbatore.csv")

# Check for missing values and print column names
print("Columns in dataset:", crime_data.columns)
print("Missing values in dataset:")
print(crime_data.isnull().sum())

# Define your features (X) and target variable (y)
X = crime_data.drop("Crime Outcome", axis=1)  # All columns except 'Crime Outcome'
y = crime_data["Crime Outcome"]  # Target variable

# Initialize label encoders for categorical columns
le_crime_type = LabelEncoder()
le_area = LabelEncoder()

# Encode categorical variables
if 'Crime Type' in X.columns:
    X['Crime Type'] = le_crime_type.fit_transform(X['Crime Type'])
if 'Area' in X.columns:
    X['Area'] = le_area.fit_transform(X['Area'])

# Split the data: 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Show the sizes of the splits
print(f"Training data size: {X_train.shape}")
print(f"Test data size: {X_test.shape}")

# Combine X_train with y_train to save as a single CSV
train_data = pd.concat([X_train, y_train.reset_index(drop=True)], axis=1)
test_data = pd.concat([X_test, y_test.reset_index(drop=True)], axis=1)

# Save the training and testing data to CSV files
train_data.to_csv("crime_data_train.csv", index=False)
test_data.to_csv("crime_data_test.csv", index=False)

print("Training and testing data saved to 'crime_data_train.csv' and 'crime_data_test.csv'.")

import os
import pandas as pd

# Check if the file exists
print("Current Directory:", os.getcwd())
print("File Exists:", os.path.isfile("/content/drive/MyDrive/crime predictor/synthetic_crime_data_coimbatore.csv"))

# Load the dataset
crime_data = pd.read_csv("/content/drive/MyDrive/crime predictor/synthetic_crime_data_coimbatore.csv")

# Show basic info about the dataset
print(crime_data.info())

# Show the first few rows of the dataset
print(crime_data.head())

# Check the columns in the dataset
print("Columns in dataset:", crime_data.columns)

# Check for missing values
print("Missing values in dataset:")
print(crime_data.isnull().sum())

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Initialize the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
crime_data = pd.read_csv("/content/drive/MyDrive/crime predictor/synthetic_crime_data_coimbatore.csv")

# Check for missing values and print column names
print("Columns in dataset:", crime_data.columns)
print("Missing values in dataset:")
print(crime_data.isnull().sum())

# Define features (X) and target (y)
X = crime_data.drop("Crime Outcome", axis=1)  # Drop the target column from features
y = crime_data["Crime Outcome"]  # Target variable

# Initialize label encoders for categorical columns
le_crime_type = LabelEncoder()
le_area = LabelEncoder()

# Encode categorical variables (adjust based on actual column names)
if 'Crime Type' in X.columns:
    X['Crime Type'] = le_crime_type.fit_transform(X['Crime Type'])
if 'Area' in X.columns:
    X['Area'] = le_area.fit_transform(X['Area'])

# Split the data: 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Show the sizes of the splits
print(f"Training data size: {X_train.shape}")
print(f"Test data size: {X_test.shape}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Load the dataset
crime_data = pd.read_csv("/content/drive/MyDrive/crime predictor/synthetic_crime_data_coimbatore.csv")

# Display the first few rows of the dataset
print(crime_data.head())

# Data Preprocessing
# Convert 'Date and Time' to datetime format and extract features
crime_data['Date and Time'] = pd.to_datetime(crime_data['Date and Time'])
crime_data['Hour'] = crime_data['Date and Time'].dt.hour
crime_data['Day'] = crime_data['Date and Time'].dt.dayofweek  # 0=Monday, 6=Sunday

# Define the features and target variable
X = crime_data[['Latitude', 'Longitude', 'Severity', 'Victims', 'Hour', 'Day']]
y = crime_data['Crime Type']

# Feature Scaling
scaler = MinMaxScaler()
X[['Latitude', 'Longitude', 'Severity', 'Victims', 'Hour', 'Day']] = scaler.fit_transform(X[['Latitude', 'Longitude', 'Severity', 'Victims', 'Hour', 'Day']])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature Importance
importances = rf_model.feature_importances_
feature_names = X.columns
feature_importance = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

print("\nFeature Importance:")
print(feature_importance)

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

param_grid = {
    'n_estimators': [100, 200, 300],  # Number of trees in the forest
    'max_depth': [10, 20, 30, None],  # Maximum depth of the trees
    'min_samples_split': [2, 5, 10],  # Minimum number of samples required to split a node
    'min_samples_leaf': [1, 2, 4],    # Minimum number of samples required at a leaf node
    'bootstrap': [True, False]        # Whether bootstrap samples are used when building trees
}

rf_model = RandomForestClassifier(random_state=42)

# Set up GridSearchCV
grid_search = GridSearchCV(estimator=rf_model,
                           param_grid=param_grid,
                           cv=3,  # 3-fold cross-validation
                           n_jobs=-1,  # Use all available processors
                           verbose=2,  # Output progress
                           scoring='accuracy')  # You can use other metrics like f1-score if needed

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Assuming you have already loaded and preprocessed your dataset
# Split your data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and fit the Random Forest model using GridSearchCV
rf_model = RandomForestClassifier()

# Define the parameter grid
param_grid = {
    'n_estimators': [100],
    'max_depth': [None, 10],
    'min_samples_split': [2],
    'min_samples_leaf': [1]
}

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)

# Fit the grid search
grid_search.fit(X_train, y_train)

# Retrieve the best model from grid search
best_rf_model = grid_search.best_estimator_

from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Predict on the test set
y_pred = best_rf_model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Display confusion matrix as a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=sorted(set(y_test)), yticklabels=sorted(set(y_test)))
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.title('Confusion Matrix')
plt.show()

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

misclassified = X_test[y_test != y_pred]
print("Misclassified examples:")
print(misclassified)

from sklearn.model_selection import cross_val_score

scores = cross_val_score(rf_model, X, y, cv=5)
print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())

from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display confusion matrix with labels from y_test
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(set(y_test)))

# Plot the confusion matrix
disp.plot(cmap=plt.cm.Blues)

plt.title('Confusion Matrix')
plt.show()

from sklearn.metrics import classification_report

print("Classification Report:")
print(classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

# Assuming X_train and y_train are your training data and labels
rf_model = RandomForestClassifier(random_state=42)  # You can add hyperparameters as needed
rf_model.fit(X_train, y_train)  # Fit the model
0

importances = rf_model.feature_importances_
feature_names = X.columns

# Create a DataFrame for feature importances
feature_importances = pd.DataFrame(importances, index=feature_names, columns=["Importance"])
feature_importances = feature_importances.sort_values(by="Importance", ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances.Importance, y=feature_importances.index)
plt.title('Feature Importance')
plt.show()

from sklearn.model_selection import GridSearchCV

# Define a minimal parameter grid
param_grid = {
    'n_estimators': [100],  # Use only one value for quicker testing
    'max_depth': [None, 10],  # Fewer depth options
    'min_samples_split': [2],  # One value for quicker tuning
    'min_samples_leaf': [1]   # One value for quicker tuning
}

# Create the GridSearchCV object with reduced parameters
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best parameters found: ", grid_search.best_params_)

import joblib

joblib.dump(rf_model, 'random_forest_model.pkl')

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = pd.DataFrame(data, index=[0])  # Convert to DataFrame
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)

import pickle

# Load the saved model from the .pkl file
with open('/content/random_forest_model.pkl', 'rb') as file:
    best_rf_model = pickle.load(file)

import joblib  # Import joblib

# Load the saved model from the .pkl file using joblib
best_rf_model = joblib.load('/content/random_forest_model.pkl')

# Now that the model is correctly loaded, use it to predict
y_pred = best_rf_model.predict(X_test)

# Confusion Matrix and Classification Report
from sklearn.metrics import confusion_matrix, classification_report

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

import pandas as pd
importances = best_rf_model.feature_importances_
feature_names = X.columns

# Create a DataFrame for feature importances
feature_importances = pd.DataFrame(importances, index=feature_names, columns=["Importance"]).sort_values(by="Importance", ascending=False)

# Plot the feature importances
feature_importances.plot(kind='bar', figsize=(10,6))
plt.title("Feature Importance")
plt.show()

import pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

import pandas as pd

# Example: Creating a single new instance with the same columns
new_data = pd.DataFrame({
    'Crime Type': ['Murder'],
    'Latitude': [11.015],
    'Longitude': [76.955],
    'Date and Time': ['2024-10-23 12:45:00'],
    'Severity': [2],
    'Area': ['Kuniyamuthur'],
    'Victims': [1],
    'Weather': ['Clear'],
    # Add other necessary columns
})

# Make sure that you apply the same preprocessing steps (encoding, scaling) to the new data

#import pandas as pd

# Creating new instances for prediction
new_data = pd.DataFrame({
    'Crime Type': ['Rape', 'Theft', 'Burglary'],
    'Latitude': [11.015, 10.992, 11.005],
    'Longitude': [76.955, 77.005, 77.040],
    'Date and Time': ['2024-10-23 12:45:00', '2024-09-19 15:30:00', '2024-11-12 09:00:00'],
    'Severity': [7, 3, 5],
    'Area': ['Gandhipuram', 'Podanur', 'Peelamedu'],
    'Victims': [5, 2, 3],
    'Weather': ['Cloudy', 'Cloudy', 'Clear'],
})

print(new_data)

# Apply same encoding
new_data_encoded = pd.get_dummies(new_data, columns=['Area'], drop_first=True)

# Ensure the order of columns matches the training set
new_data_encoded = new_data_encoded.reindex(columns=X.columns, fill_value=0)

# Now make predictions
predictions = model.predict(new_data_encoded)

# Now proceed with predictions
predictions = model.predict(new_data_encoded)

# Output predictions
print(predictions)