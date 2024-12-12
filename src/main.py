# src/main.py
import os
import requests
import json
import logging
from config import SERVER_URL, API_TOKEN

# Ensure the logs directory exists
if not os.path.exists('../logs'):
    os.makedirs('../logs')

# Configure logging
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Mock data (e.g., device ID and system information)
device_data = {
    "device_id": "12345",
    "device_name": "Android Virtual Device",
    "os_version": "Android 11",
    "manufacturer": "Google",
    "model": "Pixel 4"
}

# Add authentication token and other necessary headers
headers = {
    'Authorization': f'Bearer {API_TOKEN}',  # Authorization token (Bearer token)
    'Content-Type': 'application/json'
}

# Function to send data to the backend server
def send_data_to_server(data):
    try:
        # Send the POST request to the server with mock data and headers
        response = requests.post(SERVER_URL, json=data, headers=headers)
        
        # Log the server response
        if response.status_code == 200:
            logging.info(f"Data successfully sent to the server. Response: {response.json()}")
            print("Data successfully sent to the server.")
        else:
            logging.error(f"Failed to send data. Status Code: {response.status_code}")
            print(f"Failed to send data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Call the function to send data
send_data_to_server(device_data)
