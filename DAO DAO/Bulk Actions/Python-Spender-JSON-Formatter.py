import json

# Define the 'addresses' list variable
addresses = [
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS",
    "REDACTED_ADDRESS"
]

# Initialize an empty list 'actions' to store spending actions for each address
actions = []

# Loop through each address in the 'addresses' list
for address in addresses:
    # Create a dictionary containing the spending action details for the current address
    action = {
        "key": "spend",
        "data": {
            "to": address,
            "amount": "1",
            "denom": "ujuno"
        }
    }

    # Append the action dictionary to the 'actions' list
    actions.append(action)

# Create a dictionary containing the list of actions
json_data = {
    "actions": actions
}

# Define the output JSON file name
json_file = "MassSpender.json"

# Open the output JSON file and write the json_data with 2 spaces indentation
with open(json_file, "w") as output_file:
    json.dump(json_data, output_file, indent=2)
