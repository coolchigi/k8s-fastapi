import requests
import json

# Define the base URL
base_url = "http://localhost:8000"

# Endpoint URL for creating an item
create_item_url = f"{base_url}/items/"

# Define the item data as a dictionary
item_data = {"id": 1001, "name": "New Item", "price": 9.99}

# Convert the item data to JSON
payload = json.dumps(item_data)

# Set the request headers (optional)
headers = {"Content-Type": "application/json"}

# Send the POST request
response = requests.post(create_item_url, data=payload, headers=headers)

# Check the response status code
if response.status_code == 200:
  # Successful request
  new_item = response.json()
  print("Item created successfully:")
  print(new_item)
else:
  # Request failed
  print("Error creating item. Status code:", response.status_code)
  print("Response content:", response.text)

# uvicorn main:app --reload --host=0.0.0.0 --port=8000
