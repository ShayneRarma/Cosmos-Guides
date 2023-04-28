cls

$addresses = @(
"juno10a29hu7chl55ar4wsyjueqxc7smudpvrs3rjam"
"juno14vgvwqadrluenyepcn7lhv6e8lq507rare6s3a"
"juno18qw9ydpewh405w4lvmuhlg9gtaep79vy2gmtr2"
"juno1eck27qefttt5twxsg38gsr0q0hr4e3vvyxm2q4"
"juno1v5ft27rre0m3th7etfvm5c8vhw462vh6uystkh"
"juno1x0geq60tewsqhcf53u7e9gw68y95ud5xe428h0"
"juno1xdulfs7wvka5vuntuzz4kmrtds3cdtfvmn2y6d"
"juno137p2qrs3qw00c28679pwu4a76md48q8zwsq9qg"
"juno1fn0h75ee5rudwfnuc47nrkqes5pftp373xvrgj"
"juno1hmda69ykt8rzsrxanrxm2r837edln3pjev0dpw"
"juno1n5yr7uxk9eza6m29ew7zvrc0zkd5nvwemax73f"
"juno1ssfrydv7qs6qfnx28q7kmkuvuyea724l3qg2xl"
"juno1xuwl7x8htyl26t7pe3l0x6auj3j9jwd25ywx2e"
"juno10q4dtmakqcghyxx7cdku92m7ws6fsj3ttjzhwa"
"juno10ujj0xx8fcqwsnrfkprjnhvu4g2x230uvvj8u6"
"juno160wdvp32nwrj8nqvdyvgn84vq8mvd8dvkca99n"
"juno1663yhw0rre70egdwez3sw2e0ery94vgnn5elza"
"juno16ja5akn8pmcc44z09ahtd06zqd8lwrmlfjvtmf"

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
            collectionAddress = "juno1tghpl95wdgusnax4xrn2vjdv7zmusneek6h0a5t3z87mzzls6ulsj5grx9"
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
