import json

# Define the 'addresses' list variable
addresses = [
    "juno10a29hu7chl55ar4wsyjueqxc7smudpvrs3rjam",
    "juno14vgvwqadrluenyepcn7lhv6e8lq507rare6s3a",
    "juno18qw9ydpewh405w4lvmuhlg9gtaep79vy2gmtr2",
    "juno1eck27qefttt5twxsg38gsr0q0hr4e3vvyxm2q4",
    "juno1v5ft27rre0m3th7etfvm5c8vhw462vh6uystkh",
    "juno1x0geq60tewsqhcf53u7e9gw68y95ud5xe428h0",
    "juno1xdulfs7wvka5vuntuzz4kmrtds3cdtfvmn2y6d",
    "juno137p2qrs3qw00c28679pwu4a76md48q8zwsq9qg",
    "juno1fn0h75ee5rudwfnuc47nrkqes5pftp373xvrgj",
    "juno1hmda69ykt8rzsrxanrxm2r837edln3pjev0dpw",
    "juno1n5yr7uxk9eza6m29ew7zvrc0zkd5nvwemax73f",
    "juno1ssfrydv7qs6qfnx28q7kmkuvuyea724l3qg2xl",
    "juno1xuwl7x8htyl26t7pe3l0x6auj3j9jwd25ywx2e",
    "juno10q4dtmakqcghyxx7cdku92m7ws6fsj3ttjzhwa",
    "juno10ujj0xx8fcqwsnrfkprjnhvu4g2x230uvvj8u6",
    "juno160wdvp32nwrj8nqvdyvgn84vq8mvd8dvkca99n",
    "juno1663yhw0rre70egdwez3sw2e0ery94vgnn5elza",
    "juno16ja5akn8pmcc44z09ahtd06zqd8lwrmlfjvtmf",
    "juno18mmruat2mwt3uk6xdu95ayf0wpuwzuhx3jtkhg",
    "juno1932p8lwv65z7wyh2jnw7sqshuldhynm6zrqrs6",
    "juno1973qhhswmsf0y99h88t40v7ecgzqhs6rf8g473",
    "juno19ckvp2666xc5aaevrmufppyzjtggfhguzkh4lj",
    "juno1e09gqxzfegmtrjug3epna589umuylzvh6qsgwf"
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
