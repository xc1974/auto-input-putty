@@ -0,0 +1,61 @@
import os
import requests
import time

# URL of the GitHub file
github_url = 'https://raw.githubusercontent.com/username/repo_name/main/file_name.py'

# Local file path
local_path = 'file_name.py'

if os.path.isfile(local_path):
    # Get the modification time of the local file
    local_mod_time = os.path.getmtime(local_path)

    # Get the content of the GitHub file
    response = requests.get(github_url)
    github_code = response.content.decode('utf-8')

    # Get the modification time of the GitHub file
    github_mod_time = time.mktime(time.strptime(response.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z'))

    # Check if the content of the local file is the same as the content of the GitHub file
    with open(local_path, 'r') as f:
        local_code = f.read()

    if local_code != github_code:
        # Calculate the time difference in seconds
        time_diff = time.time() - local_mod_time

        # Print the time difference in seconds
        print(f'The local file is different from the GitHub file. Time difference: {time_diff} seconds.')

        # Write the content of the GitHub file to the local file
        with open(local_path, 'w') as f:
            f.write(github_code)

    # Run the updated code
    exec(github_code)
else:
    # Get the content of the GitHub file
    response = requests.get(github_url)
    github_code = response.content.decode('utf-8')

    # Write the content of the GitHub file to the local file
    with open(local_path, 'w') as f:
        f.write(github_code)

    # Run the code
    exec(github_code)

# Check if input file exists
if os.path.isfile('input.txt'):
    # Read input value from file
    with open('input.txt', 'r') as f:
        ipaddress = f.readline().strip()
else:
    # Ask user for input value
    ipaddress = input("Please enter the IO address: ")

# Run Putty.exe with SSH address, username, and password
os.system(f'putty.exe -ssh {ipaddress} -l pi -pw lkkcict306')
