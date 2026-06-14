# Car Price Prediction

## About Project

This project predicts car selling prices using machine learning.

The main aim of this project is to understand how different car features affect the selling price and build models that can predict car prices accurately.

## Dataset

Dataset used: `car_data.csv`

The dataset contains details of cars such as present price, driven kilometers, fuel type, selling type, transmission type, owner count, and selling price.

## Columns Used

- Car_Name
- Year
- Selling_Price
- Present_Price
- Driven_kms
- Fuel_Type
- Selling_type
- Transmission
- Owner

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Work Done in This Project

- Loaded the dataset
- Checked dataset information
- Checked missing values
- Performed data visualization
- Analyzed relation between car features and selling price
- Removed extreme values from driven kilometers
- Encoded categorical columns
- Created car age feature
- Split data into training and testing sets
- Trained machine learning models
- Compared model performance
- Visualized actual vs predicted prices

## Main Analysis

### 1. Price Distribution

The selling price distribution was analyzed to understand the range of car prices in the dataset.

### 2. Feature Analysis

Different features were compared with selling price, such as:

- Present price
- Driven kilometers
- Fuel type
- Selling type
- Transmission
- Year

### 3. Data Preprocessing

Categorical columns were converted into numerical format using one-hot encoding.

A new feature called `Car_Age` was created from the `Year` column.

### 4. Models Used

Two machine learning models were trained:

- Linear Regression
- Random Forest Regressor

## Model Performance

### Linear Regression

- MAE: 1.29
- MSE: 3.77
- R2 Score: 0.8428

### Random Forest Regressor

- MAE: 0.63
- MSE: 0.88
- R2 Score: 0.9630

## Best Model

Random Forest Regressor performed better than Linear Regression.

It gave an R2 Score of **0.9630**, which means the model predicted car prices very accurately compared to Linear Regression.

## Final Observations

- Present price had a strong impact on selling price.
- Car age affected the selling price.
- Fuel type, selling type, and transmission also influenced the price.
- Random Forest worked better because the data was not fully linear.
- Linear Regression gave good results, but Random Forest captured patterns better.

## Conclusion

This project helped me understand how to build a machine learning regression project.

I learned how to clean data, visualize features, encode categorical data, train models, compare performance, and predict car prices using machine learning.