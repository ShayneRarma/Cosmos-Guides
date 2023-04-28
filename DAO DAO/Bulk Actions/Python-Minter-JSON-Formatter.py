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

# Initialize token_id_counter to start from 1
token_id_counter = 1

# Initialize an empty list 'actions' to store minting actions for each address
actions = []

# Loop through each address in the 'addresses' list
for address in addresses:
    # Format token_id by padding with leading zeros (up to 4 digits)
    token_id = f"{token_id_counter:04}"

    # Create a dictionary containing the minting action details for the current address
    action = {
        "key": "mintNft",
        "data": {
            "contractChosen": True,
            "collectionAddress": "REDACTED_ADDRESS",
            "mintMsg": {
                "owner": address,
                "token_id": token_id,
                "token_uri": "ipfs://bafyreih2m2gwnumiji4whhikncw4ahhabcf53cjbb5yi7tv2qapzmnhfqe/metadata.json",
            },
        },
    }

    # Append the action dictionary to the 'actions' list
    actions.append(action)
    # Increment the token_id_counter for the next iteration
    token_id_counter += 1

# Create a dictionary containing the list of actions
json_data = {
    "actions": actions
}

# Define the output JSON file name
json_file = "MassMinter.json"

# Open the output JSON file and write the json_data with 2 spaces indentation
with open(json_file, "w") as output_file:
    json.dump(json_data, output_file, indent=2)
