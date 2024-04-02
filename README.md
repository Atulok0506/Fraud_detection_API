# Fraud_detection_API

![Fraud_Detection_API](https://github.com/Atulok0506/Fraud_detection_API/blob/main/Screenshot%202024-04-02%20143854.png)

![Programming Language](https://img.shields.io/badge/Python-3.10-orange)
![Framework](https://img.shields.io/badge/Framework-FastAPI-red)
![Cloud](https://img.shields.io/badge/AWS-fcba03)

## Dataset

The dataset used for this project can be found [here](https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection).



## Overview
The Fraud Detection API employs machine learning algorithms to predict fraudulent transactions, ensuring the security and integrity of financial systems. It offers a streamlined and efficient solution for identifying potential fraud, providing real-time insights into transaction authenticity. With its user-friendly interface and high accuracy, it enhances fraud detection capabilities, enabling businesses to safeguard against financial risks effectively. The API's seamless integration and robust performance make it an invaluable tool for organizations seeking to protect their assets and maintain trust in their financial operations.

## About the Project
The Fraud Detection API utilizes machine learning to predict fraudulent transactions in financial systems. It offers real-time insights into transaction authenticity, enhancing security and trust. With its user-friendly interface and high accuracy, it provides businesses with an efficient tool for fraud detection. The API's seamless integration and robust performance make it invaluable for organizations seeking to safeguard their assets. By leveraging advanced algorithms, it identifies potential fraud patterns, reducing financial risks and maintaining the integrity of transactions. Overall, the Fraud Detection API is a vital solution for enhancing security and trust in financial operations.

## Getting started 
1. Clone the repository: `git clone https://github.com/Atulok0506/Fraud_detection_API.git`.
2. Navigate to the project directory: `cd Fraud_detection_API`.
3. Set up a virtual environment: `python -m venv venv`.
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`.
   - On macOS/Linux: `source venv/bin/activate`.
5. Install the required dependencies: `pip install -r requirements.txt`.
6. Run the FastAPI server: `uvicorn main:app --reload`.
7. Once the server is running, you can access the API endpoints:
   - For prediction: `http://127.0.0.1:8000/predict`.
8. Test the API by sending a POST request with sample input data.
   
## API Testing

```python
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "step": 1.0,
    "amount": 1000.0,
    "oldbalanceOrg": 5000.0,
    "newbalanceOrig": 4000.0,
    "oldbalanceDest": 0.0,
    "newbalanceDest": 0.0,
    "isFlaggedFraud": 0,
    "type_CASH_IN": 0,
    "type_CASH_OUT": 1,
    "type_DEBIT": 0,
    "type_PAYMENT": 0,
    "type_TRANSFER": 0
}

# Send a POST request to the API endpoint with JSON data
response = requests.post(url, json=data)

# Print the response
print(response.json())

