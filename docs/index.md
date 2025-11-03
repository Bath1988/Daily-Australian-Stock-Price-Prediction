# Daily Australian Stock Price Prediction

Welcome to the project documentation and results summary for the Daily Australian Stock Price Prediction web application.

---

## Project Overview

This project predicts daily closing prices for major Australian stocks (banks, miners, and energy companies) using historical data from the Yahoo Finance API. The workflow covers data collection, preprocessing, feature engineering, model training, and evaluation. Results are presented for each company, with a focus on comparing machine learning models to naive baselines.

### Companies Included
- Major Australian Banks: CBA, NAB, WBC, ANZ
- Major Miners: BHP, RIO, FMG
- Energy: Origin (ORG), AGL (AGL)

---

## Data Science Workflow
1. **Data Collection**: Automated fetching of daily closing prices for all companies, saved in a single pivoted CSV file (`output_all_companies.csv`).
2. **Data Preprocessing**: Cleaning and preparing the data for analysis.
3. **Feature Engineering**: Creating features such as lagged prices, rolling statistics, and date-based features.
4. **Model Training**: Training and evaluating models (Linear Regression, XGBoost, Prophet) for each company.
5. **Model Evaluation**: Comparing models using MAE and RMSE, with walk-forward validation.
6. **Deployment**: Web frontend for interactive predictions (see `src/Frontend/`).

---

## Key Results
- **Naive Baseline Models**: Simple approaches (e.g., last value, mean) provide a reference for model performance.
- **Machine Learning Models**: Linear Regression, XGBoost, and Prophet generally outperform naive baselines, especially for banks and miners.
- **Walk-Forward Validation**: Ensures robust evaluation by simulating real-world prediction scenarios.

---

## How to Use This Project
- All analysis scripts and notebooks allow you to select a company for modeling.
- Data is loaded from the combined CSV (`Data/output_all_companies.csv`).
- See the `/Analysis` folder for EDA, feature engineering, and modeling scripts/notebooks.
- The web frontend is in `src/Frontend/`.

---

## Example Visualizations


### Example Feature-Engineered Table (CBA.AX)

Below are the first 6 rows of the feature-engineered data for CBA.AX:

| date       | closing_price | clolag_1 | price_diff | prilag_1 | prilag_2 | prilag_3 | prilag_4 | prilag_5 |
|------------|---------------|----------|------------|----------|----------|----------|----------|----------|
| 2023-05-11 | 98.35         | 97.85    | 0.5        | 0.51     | 0.22     | 0.99     | 0.37     | -2.53    |
| 2023-05-12 | 98.96         | 98.35    | 0.61       | 0.5      | 0.51     | 0.22     | 0.99     | 0.37     |
| 2023-05-15 | 98.5          | 98.96    | -0.46      | 0.61     | 0.5      | 0.51     | 0.22     | 0.99     |
| 2023-05-16 | 97.59         | 98.5     | -0.91      | -0.46    | 0.61     | 0.5      | 0.51     | 0.22     |
| 2023-05-17 | 97.14         | 97.59    | -0.45      | -0.91    | -0.46    | 0.61     | 0.5      | 0.51     |
| 2023-05-18 | 98.0          | 97.14    | 0.86       | -0.45    | -0.91    | -0.46    | 0.61     | 0.5      |


---

## About & License

This project is open-source under the MIT License. Contributions and suggestions are welcome!

---

## Original README

<details>
<summary>Click to expand</summary>

## **1. Introduction**

The **Daily Australian Stock Price Prediction** is a web application designed to predict daily stock prices using historical data. The data fetched from YH Finance API hosted in Rapidapi api market place. 

The prediction model predicts the closing stock price for the next business day. Different predictive models will be used to compare the predictive performance.

### **Data Science Workflow**
The project follows a standard data science workflow, which includes:
1. **Data Collection**: Fetching historical stock data from the Yahoo Finance API. Daily closing stock price data from CommonWealth Bank of Australia for     past two years was taken for the analysis.
2. **Data Preprocessing**: Cleaning and preparing the data for analysis.
3. **Feature Engineering**: Extracting meaningful features from the raw data.
4. **Model Training**: Training machine learning models to predict stock prices.
5. **Model Evaluation**: Assessing the performance of the models using metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
6. **Deployment**: Deploying the trained model as a web application for real-time predictions.

This project uses machine learning algorithms such as linear regression, xgboost and prophet to predict stock prices. These models were compaired against three baseline naive models for their prediction accuracy.

### **Challenges of the stock market value prediction**
The project addresses several challenges in stock market prediction:
- **Data Quality**: Ensuring the uptodate historical stock data.
- **Model Complexity**: Balancing model training time and prediction accuracy.
- **Scalability**: Handling large volumes of data and ensuring the application can scale with increasing demand.
- **Real-Time Predictions**: Providing up-to-date predictions using the latest market data.

### **Project Goals**
The primary goals of the project are:
- **Predict next day closing stock price**
- **Naive models**: Compaire different naive models 
- **Machine learning for time series forcasting**: Impliment different machine learning models and compare them with naive models.
- **Model Validation**: Machine learning models were validated using walk forward validation.

## **Contributing**
Since this project is not for commercial purposes and aimed for gaining knowledge, contributions and suggestions are highly regarded!

## **License**
This project is open-source and available under the **MIT License**.

</details>
