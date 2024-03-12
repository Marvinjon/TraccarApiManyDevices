import csv
import requests
import json
from requests.auth import HTTPBasicAuth

# Traccar server details
TRACCAR_URL = input("enter the traccar server URL: ")
USERNAME = input("Enter email adress: ")
PASSWORD = input("Enter password: ")
DevicePath = input("Enter device path(with .csv): ")

# Path to the CSV file 
csv_file_path = DevicePath

def create_device(row):
    url = f"https://{TRACCAR_URL}/api/devices"
    headers = {'Content-Type': 'application/json'}
       
    try:
        attributes = json.loads(row.get("attributes", "{}"))
    except:
        attributes = {}
    
    # Prepare the data payload
    data = {
        "name": row.get("name"),
        "uniqueId": row.get("uniqueId"),
        "status": row.get("status"),
        "disabled": row.get("disabled").lower() in ['true', '1', 't', 'y', 'yes'],
        "lastUpdate": row.get("lastUpdate"),  # Ensure this is in ISO 8601 format or converted appropriately
        "positionId": int(row.get("positionId")) if row.get("positionId") else None,
        "groupId": int(row.get("groupId")) if row.get("groupId") else None,
        "phone": row.get("phone"),
        "model": row.get("model"),
        "contact": row.get("contact"),
        "category": row.get("category"),
    }

    
    response = requests.post(url, json=data, headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    #print(response.status_code, response.json()) !remove comment for debugging!
    return response

# Read devices from CSV and create them in Traccar
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        response = create_device(row)
        if response.status_code == 200:
            print(f"Device {row['name']} created successfully.")
        else:
            print(f"Failed to create device {row['name']}. Status code: {response.status_code}, Response: {response.text}")

