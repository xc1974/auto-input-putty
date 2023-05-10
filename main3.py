import subprocess
import os.path
import os
import requests
import time
import subprocess
import os.path

# URL of the GitHub file
github_url = 'https://raw.githubusercontent.com/xc1974/auto-input-putty/main/main3.py'
# Local file path
local_path = 'main3.py'
x=0

if x == 0:

    if os.path.isfile(local_path):
    # Get the modification time of the local file
        local_mod_time = os.path.getmtime(local_path)
    # Get the content of the GitHub file
        response = requests.get(github_url)
        github_code = response.content.decode('utf-8')
    # Check if the content of the local file is the same as the content of the GitHub file
        with open(local_path, 'r') as f:
            local_code = f.read()
        if local_code != github_code:
        # Write the content of the GitHub file to the local file
            with open(local_path, 'w') as f:
                f.write(github_code)
                x = x+1
    # Run the updated code
        exec(github_code)

# Check if the ip_address.txt file exists

if os.path.isfile("ip_address.txt"):

    with open("ip_address.txt", "r") as f:

        ip_address = f.read().strip()

else:

    # Get the content of the GitHub file

    response = requests.get(github_url)

    github_code = response.content.decode('utf-8')

    # Ask user for the IP address if the file does not exist

    ip_address = input("Please enter the IP address: ")



    # Write the content of the GitHub file to the local file

    with open(local_path, 'w') as f:

        f.write(github_code)



    # Run the code

    exec(github_code)



# Check if the ip_address.txt file exists

if os.path.isfile("ip_address.txt"):

    with open("ip_address.txt", "r") as f:

        ip_address = f.read().strip()

else:

    # Ask user for the IP address if the file does not exist

    ip_address = input("Please enter the IP address: ")



# Run the command with the given IP address

command = f"putty.exe -ssh {ip_address} -l pi -pw lkkcict306"

subprocess.run(command, shell=True)



# Save the IP address into a file for future use

with open("ip_address.txt", "w") as f:

    f.write(ip_address)
