## **1. Introduction**

The **Daily Australian Stock Price Prediction** is an application designed to predict daily stock prices using historical data. The data fetched from YH Finance API hosted in Rapidapi api market place. 

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

