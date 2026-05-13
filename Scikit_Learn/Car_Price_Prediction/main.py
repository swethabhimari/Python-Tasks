#=====================================================================
# Project Title: Car Price Prediction using Machine Learning
#=====================================================================

#=====================================================================
# Import Libraries
#=====================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

#=====================================================================
# Load Dataset
#=====================================================================

df = pd.read_csv("cardata.csv")

# Display dataset information
print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

#=====================================================================
# Basic Data Cleaning
#=====================================================================

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing values
df['Selling_Price'] = df['Selling_Price'].fillna(df['Selling_Price'].mean())
df['Present_Price'] = df['Present_Price'].fillna(df['Present_Price'].mean())
df['Kms_Driven'] = df['Kms_Driven'].fillna(df['Kms_Driven'].mean())

# Fill categorical missing values
df['Fuel_Type'] = df['Fuel_Type'].fillna(df['Fuel_Type'].mode()[0])

# Convert numeric columns
num_cols = ['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven']

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

#=====================================================================
# NumPy Analysis
#=====================================================================

selling_array = df['Selling_Price'].to_numpy()

print("\nSelling Price Analysis")
print("Minimum Selling Price :", np.min(selling_array))
print("Maximum Selling Price :", np.max(selling_array))
print("Average Selling Price :", np.mean(selling_array))

#=====================================================================
# Feature Engineering
#=====================================================================

# Create Car Age column
current_year = 2026

df['Car_Age'] = current_year - df['Year']

# Create Price Difference column
df['Price_Difference'] = df['Present_Price'] - df['Selling_Price']

#=====================================================================
# Encode Categorical Columns
#=====================================================================

encoder = LabelEncoder()

categorical_cols = [
    'Car_Name',
    'Fuel_Type',
    'Seller_Type',
    'Transmission'
]

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

#=====================================================================
# Feature Selection
#=====================================================================

# X = df.drop('Selling_Price', axis=1)
X = df.drop(['Selling_Price', 'Price_Difference'], axis=1)

y = df['Selling_Price']

print("\nFeature Columns")
print(X.columns)

#=====================================================================
# Split Dataset
#=====================================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

#=====================================================================
# Algorithm 1 : Linear Regression
#=====================================================================

print("\n===================================")
print("LINEAR REGRESSION")
print("===================================")

# Create model
lr_model = LinearRegression()

# Train model
lr_model.fit(X_train, y_train)

# Predictions
lr_predictions = lr_model.predict(X_test)

# Evaluation
lr_mae = mean_absolute_error(y_test, lr_predictions)
lr_mse = mean_squared_error(y_test, lr_predictions)
lr_rmse = np.sqrt(lr_mse)
lr_r2 = r2_score(y_test, lr_predictions)

# Print Results
print("MAE  :", lr_mae)
print("MSE  :", lr_mse)
print("RMSE :", lr_rmse)
print("R2 Score (Accuracy) :", lr_r2)

#=====================================================================
# Algorithm 2 : Random Forest Regressor
#=====================================================================

print("\n===================================")
print("RANDOM FOREST REGRESSOR")
print("===================================")

# Create model
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
rf_model.fit(X_train, y_train)

# Predictions
rf_predictions = rf_model.predict(X_test)

# Evaluation
rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_mse = mean_squared_error(y_test, rf_predictions)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_predictions)

# Print Results
print("MAE  :", rf_mae)
print("MSE  :", rf_mse)
print("RMSE :", rf_rmse)
print("R2 Score (Accuracy) :", rf_r2)

#=====================================================================
# Compare Models
#=====================================================================

print("\n===================================")
print("MODEL COMPARISON")
print("===================================")

print("Linear Regression Accuracy :", lr_r2)
print("Random Forest Accuracy     :", rf_r2)

if rf_r2 > lr_r2:
    print("\nBest Model : Random Forest Regressor")
else:
    print("\nBest Model : Linear Regression")

#=====================================================================
# Actual vs Predicted Graph
#=====================================================================

plt.figure(figsize=(8,6))

plt.scatter(
    y_test,
    rf_predictions,
    color='blue'
)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")

plt.title("Actual vs Predicted Selling Price")

plt.grid(True)

plt.tight_layout()

# plt.savefig("actual_vs_predicted.png")

plt.show()

#=====================================================================
# Feature Importance Graph
#=====================================================================

importance = rf_model.feature_importances_

feature_names = X.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
})

importance_df = importance_df.sort_values(
    by='Importance',
    ascending=False
)

print("\nFeature Importance")
print(importance_df)

# Plot graph
plt.figure(figsize=(10,6))

plt.barh(
    importance_df['Feature'],
    importance_df['Importance'],
    color='green'
)

plt.xlabel("Importance")
plt.ylabel("Features")

plt.title("Feature Importance - Random Forest")

plt.gca().invert_yaxis()

plt.tight_layout()

# plt.savefig("feature_importance.png")

plt.show()

#=====================================================================
# Selling Price Distribution Histogram
#=====================================================================

plt.figure(figsize=(8,5))

plt.hist(
    df['Selling_Price'],
    bins=20,
    color='orange',
    edgecolor='black'
)

plt.title("Selling Price Distribution")

plt.xlabel("Selling Price")
plt.ylabel("Frequency")

plt.tight_layout()

# plt.savefig("selling_price_histogram.png")

plt.show()

#=====================================================================
# Fuel Type vs Average Selling Price
#=====================================================================

fuel_avg = df.groupby('Fuel_Type')['Selling_Price'].mean()

plt.figure(figsize=(8,5))

fuel_avg.plot(
    kind='bar',
    color='purple'
)

plt.title("Average Selling Price by Fuel Type")

plt.xlabel("Fuel Type")
plt.ylabel("Average Selling Price")

plt.tight_layout()

# plt.savefig("fuel_type_avg_price.png")

plt.show()

#=====================================================================
# Predict New Car Price
#=====================================================================

print("\n===================================")
print("CAR PRICE PREDICTION")
print("===================================")

# Take one sample row
sample_car = X.iloc[0:1]

# Predict using Random Forest
predicted_price = rf_model.predict(sample_car)

print("Predicted Selling Price :", predicted_price[0])

#=====================================================================
# Final Insights
#=====================================================================

print("\n===================================")
print("FINAL INSIGHTS")
print("===================================")

print("1. Random Forest usually provides better accuracy.")
print("2. Present Price highly affects Selling Price.")
print("3. Older cars generally have lower prices.")
print("4. Cars with lower kilometers driven often have higher value.")
print("5. Fuel type and transmission also influence car price.")

print("\nProject Completed Successfully.")