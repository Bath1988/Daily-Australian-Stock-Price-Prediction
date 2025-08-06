## **1. Introduction**

The **Daily Australian Stock Price Prediction** is a web application designed to predict daily stock prices using historical data. The data fetched from YH Finance API hosted in Rapidapi api market place. 

The prediction model predicts the closing stock price for the next business day. Different predictive models will be used to compare the predictive performance.

Some components of the application will be deployed in aws cloud.
The application is accessible through interactive web application.

The development is starting with minimalist application and add more features in later stages. 

### **1.4. Cloud Integration**
To address scalability and deployment challenges, the project leverages in AWS lambda for:
- **Data Storage**: Storing raw and processed data in S3.
- **Compute Resources**: Hosting the application in AWS lambda.


### **1.1. Data Science Workflow**
The project follows a standard data science workflow, which includes:
1. **Data Collection**: Fetching historical stock data from the Yahoo Finance API.
2. **Data Preprocessing**: Cleaning and preparing the data for analysis.
3. **Feature Engineering**: Extracting meaningful features from the raw data.
4. **Model Training**: Training machine learning models to predict stock prices.
5. **Model Evaluation**: Assessing the performance of the models using metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
6. **Deployment**: Deploying the trained model as a web application for real-time predictions.


This project uses machine learning algorithms such as linear regression, xgboost and prophet to predict stock prices. These models were compaired against three baseline naive models for their prediction accuracy.

### **1.3. Challenges of the stock market value prediction**
The project addresses several challenges in stock market prediction:
- **Data Quality**: Ensuring the uptodate historical stock data.
- **Model Complexity**: Balancing model training time and prediction accuracy.
- **Scalability**: Handling large volumes of data and ensuring the application can scale with increasing demand.
- **Real-Time Predictions**: Providing up-to-date predictions using the latest market data.

### **1.5. Minimalist application **

Initially minimalist application will be developed. This aplication has the ability to fetch data, build model and do the prediction, and visualise the results in web application in batch wise.


### **1.5. Project Goals**
The primary goals of the project are:
- **Automation**: Automate the process of data fetching, model training, and prediction.
- **Accessibility**: Provide a user-friendly web interface for accessing predictions.
- **Scalability**: Ensure the application can handle increasing amounts of data and users.
- **Reproducibility**: Use containerization and infrastructure-as-code to ensure consistent deployment across environments.

## **Contributing**
Since this is an **educational project**, contributions and suggestions are welcome!

## **License**
This project is open-source and available under the **MIT License**.

---
_Developed as a portfolio project to enhance my skills in **cloud computing, data science, and machine learning**._ 🚀
