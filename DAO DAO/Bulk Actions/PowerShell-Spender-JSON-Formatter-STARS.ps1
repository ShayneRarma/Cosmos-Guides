cls

#STARS Addresses to receive tokens
$addresses = @(
"stars12hurjn35he797n3fx0dfhjv6lmc39sgfvr4exh",
"stars12hurjn35he797n3fx0dfhjv6lmc39sgfvr4exh",
"stars12hurjn35he797n3fx0dfhjv6lmc39sgfvr4exh",
"stars12hurjn35he797n3fx0dfhjv6lmc39sgfvr4exh",
"stars12hurjn35he797n3fx0dfhjv6lmc39sgfvr4exh"

)

$Amount = "200"
$Token = "stars"

# Initialize an empty array 'actions' to store spending actions for each address
$actions = @()

# Loop through each address in the 'addresses' list
foreach ($address in $addresses) {

    # Create a hashtable containing the spending action details for the current address
    $action = @{
        key = "spend"
        data = @{
            to = $address
            amount = $Amount
            denom = "u" + $Token
        }
    }

    # Append the action hashtable to the 'actions' array
    $actions += $action
}

# Create a hashtable containing the list of actions
$jsonData = @{
    actions = $actions
}

# Define the output JSON file name
$jsonFile = "MassSpender.json"

# Convert the hashtable jsonData to JSON format, set the depth to 5, and write the result to the specified JSON file
$jsonData | ConvertTo-Json -Depth 5 | Set-Content -Path $jsonFile
