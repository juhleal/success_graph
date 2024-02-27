# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Prompt user for data input
data = []
for i in range(6):
    month = input("Enter month: ")
    income = float(input("Enter income for {}: ".format(month)))
    services = int(input("Enter number of services for {}: ".format(month)))
    social_media_posts = int(input("Enter number of social media posts for {}: ".format(month)))
    data.append({'Month': month, 'Income': income, 'Services': services, 'Social_Media_Posts': social_media_posts})

# Convert data to DataFrame
df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df.drop(['Month', 'Income'], axis=1)
y = df['Income']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Plot actual vs. predicted income
plt.plot(df['Month'], df['Income'], label='Actual Income')
plt.plot(df['Month'], model.predict(X), label='Predicted Income')
plt.xlabel('Month')
plt.ylabel('Income')
plt.title('Actual vs. Predicted Income')
plt.legend()
plt.show()

# Display feature importance
feature_importance = pd.Series(model.coef_, index=X.columns)
print("Feature Importance:")
print(feature_importance)
