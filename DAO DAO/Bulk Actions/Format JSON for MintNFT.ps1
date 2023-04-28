cls

$addresses = @(
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"
"REDACTED_ADDRESS"

)

# Initialize the tokenIdCounter variable to 1
$tokenIdCounter = 1

# Initialize an empty array 'actions' to store minting actions for each address
$actions = @()

# Loop through each address in the 'addresses' list
foreach ($address in $addresses) {
    # Create a zero-padded 4-digit token ID using the tokenIdCounter
    $token_id = "{0:D4}" -f $tokenIdCounter

    # Create a hashtable containing the minting action details for the current address
    $action = @{
        key = "mintNft"
        data = @{
            contractChosen = $true
            collectionAddress = "REDACTED_ADDRESS"
            mintMsg = @{
                owner = $address
                token_id = $token_id
                token_uri = "ipfs://bafyreihysvncqkkix2jx4n5kqfl5ptr3vjnd6o7rwtwke2pxww5a6dzrk4/metadata.json"
            }
        }
    }

    # Append the action hashtable to the 'actions' array
    $actions += $action

    # Increment the tokenIdCounter
    $tokenIdCounter++
}

$jsonData = @{
    actions = $actions
}

$jsonFile = "MassMinter.json"
$jsonData | ConvertTo-Json -Depth 5 | Set-Content -Path $jsonFile
