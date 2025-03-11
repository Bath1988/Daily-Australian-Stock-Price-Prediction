## **1. Introduction**

The **Daily Australian Stock Price Prediction** is a web application designed to predict daily stock prices using historical data. The data fetched from YH Finance API hosted in Rapidapi api market place. The data fetched was limited to several major ASX stocks due to the limited resources using in the project to stay within the free tier. 

The prediction model utilised in the application will predict the closing stock price for the next business day. XGBOOST model is used as the prediction model for the application. Some other prediction models also compared with each other for training time and prediction accuracy.

The application is accessible through interactive web application which hosted in Oracle cloud. Cloud infrustructure is controlled by code in CLI and code used is also available in the repository.

The project combines **data science**, **machine learning**, and **cloud computing** to create a scalable and efficient solution for stock market analysis. By leveraging daily stock data from the **Yahoo Finance API**, the application trains machine learning models to generate predictions, which are then made accessible through a user-friendly web interface.

### **1.4. Cloud Integration**
To address scalability and deployment challenges, the project leverages **Oracle Cloud Infrastructure (OCI)** for:
- **Data Storage**: Storing raw and processed data in OCI Object Storage.
- **Compute Resources**: Hosting the application on OCI Compute Instances.
- **Automation**: Using Terraform for infrastructure provisioning and Docker for containerization.

### **1.1. Data Science Workflow**
The project follows a standard data science workflow, which includes:
1. **Data Collection**: Fetching historical stock data from the Yahoo Finance API.
2. **Data Preprocessing**: Cleaning and preparing the data for analysis.
3. **Feature Engineering**: Extracting meaningful features from the raw data.
4. **Model Training**: Training machine learning models to predict stock prices.
5. **Model Evaluation**: Assessing the performance of the models using metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
6. **Deployment**: Deploying the trained model as a web application for real-time predictions.


This project uses machine learning algorithms (e.g., LSTM, ARIMA) to predict stock prices, providing users with actionable insights for investment decisions.

### **1.3. Challenges Addressed**
The project addresses several challenges in stock market prediction:
- **Data Quality**: Ensuring the uptodate historical stock data.
- **Model Complexity**: Balancing model training time and prediction accuracy.
- **Scalability**: Handling large volumes of data and ensuring the application can scale with increasing demand.
- **Real-Time Predictions**: Providing up-to-date predictions using the latest market data.


### **1.5. Project Goals**
The primary goals of the project are:
- **Automation**: Automate the process of data fetching, model training, and prediction.
- **Accessibility**: Provide a user-friendly web interface for accessing predictions.
- **Scalability**: Ensure the application can handle increasing amounts of data and users (This is in production).
- **Reproducibility**: Use containerization and infrastructure-as-code to ensure consistent deployment across environments.

```
my-oci-project/
├── Dockerfile              # Dockerfile for containerization
├── .venv/                  # Python virtual environment (optional)
├── .oci/                   # OCI CLI configuration and keys
│   ├── config              # OCI CLI configuration file
│   ├── oci_api_key.pem     # Private key file
│   └── oci_api_key_public.pem # Public key file
├── scripts/                # Automation scripts
│   ├── deploy.sh           # Deployment script
│   ├── fetch_data.sh       # Script to fetch stock data
│   ├── train_model.sh      # Model training script
│   └── cleanup.sh          # Cleanup script
├── infrastructure/         # Infrastructure-as-Code (Terraform/Ansible)
│   ├── main.tf             # Terraform configuration
│   ├── variables.tf        # Terraform variables
│   └── outputs.tf          # Terraform outputs
├── src/                    # Application source code
│   ├── app.py              # Main application (Flask/FastAPI)
│   ├── models/             # ML models
│   │   ├── train.py        # Training script
│   │   └── predict.py      # Prediction script
│   ├── routes/             # API routes
│   │   └── stock_routes.py # Stock prediction API
│   ├── utils/              # Helper utilities
│   │   ├── data_fetcher.py # Fetch stock data
│   │   ├── data_loader.py  # Load data from OCI Storage
│   │   ├── db_utils.py     # Database utilities
│   │   └── oci_utils.py    # OCI interaction utilities
├── data/                   # Data storage
│   ├── raw/                # Raw stock data
│   └── processed/          # Processed predictions
├── logs/                   # Log files
│   ├── app.log             # Application logs
│   ├── fetch_data.log      # Data fetching logs
│   └── train_model.log     # Model training logs
├── tests/                  # Unit and integration tests
│   ├── test_data_fetcher.py # Test data fetching
│   ├── test_routes.py      # Test API routes
│   └── test_models.py      # Test ML models
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── .gitignore              # Ignore unnecessary files
```

## **Setup Instructions**

### **1. Prerequisites**
Ensure you have the following installed:
- Python (3.8 or later)
- Oracle Cloud Infrastructure (OCI) CLI
- Terraform (for infrastructure automation)
- Docker (optional, for containerization)


## **Future Enhancements**
- Enhance the scalability for peaktime using auto scaling and load balancing. 
- Deploy model on OCI AI services.
- Explore online machine learning models to reduce the computational cost in training.
- Add more stocks to the application

## **Contributing**
Since this is an **educational project**, contributions and suggestions are welcome!

## **License**
This project is open-source and available under the **MIT License**.

---
_Developed as a portfolio project to enhance my skills in **cloud computing, data science, and machine learning**._ 🚀
