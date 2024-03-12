Traccar Device Importer

This Python script automates the process of adding multiple devices to a Traccar server by reading device details from a CSV file and using the Traccar API to create each device.
Overview

The script allows bulk importing of devices into Traccar, saving time and reducing the potential for manual entry errors. It supports setting various device properties, including unique identifiers, status, group associations, and custom attributes.
Setup
Requirements

    Python 3.x


Installation

    Ensure Python 3.x is installed on your system.
    Install the requests library using pip:

pip install requests
or
pip3 install requests


    Download the script traccar_device_importer.py to your desired location.

CSV File Structure

The CSV file should contain the following headers:

    name: The name of the device.
    uniqueId: A unique identifier for the device, typically the IMEI number.
    status: The status of the device (optional).
    disabled: Set to true if the device is disabled; otherwise, false.
    lastUpdate: The last update time of the device in ISO 8601 format (optional).
    positionId: The ID of the last known position (optional).
    groupId: The ID of the group the device belongs to (optional).
    phone: The phone number associated with the device (optional).
    model: The model of the device (optional).
    contact: The contact information for the device (optional).
    category: The category of the device (optional).
    attributes: JSON string of additional attributes (optional).

Example CSV content:

name,uniqueId,disabled,groupId,phone,model,contact,category,attributes
id,name,uniqueId,status,disabled,lastUpdate,positionId,groupId,phone,model,contact,category,attributes
0,Vehicle 1,123456789,online,false,2024-03-12T10:15:22Z,0,8,1234567,discovery,johhny,car,
0,Vehicle 2,12345678,offline,true,2024-03-12T10:15:22Z,0,9,12234567,lambo,1234567,car,
0,Vehicle 3,1234567,online,false,2024-03-12T10:15:22Z,0,8,1134567,fiat,14,car,
0,Vehicle 4,123456,offline,false,2024-03-12T10:15:22Z,0,8,2234567,subaru,Me,car,

Ensure there are no leading or trailing spaces around column headers or values unless they are intentional.

Usage

    Open a terminal or command prompt.
    Navigate to the directory where the script is located.
    Run the script by executing:

python traccar_device_importer.py
or 
python3 traccar_device_importer.py

    When prompted, enter your Traccar server URL, email address, password and file location with the .csv in the end of the file

Troubleshooting

    Invalid groupId: Ensure that the groupId corresponds to an existing group in your Traccar server. Non-existent groupIds will be ignored or cause errors.
    Data type issues: Verify that numeric fields (like groupId and positionId) contain valid numbers or are left empty if optional.
    Attribute JSON parsing: Ensure that the attributes column, if used, contains valid JSON strings. Invalid JSON will cause the script to skip setting custom attributes for that device.

For further assistance, consult the Traccar API documentation.
