import subprocess
import os.path

# Check if the ip_address.txt file exists
if os.path.isfile("ip_address.autoinput"):
    with open("ip_address.autoinput", "r") as f:
        ip_address = f.read().strip()
else:
    # Ask user for the IP address if the file does not exist
    ip_address = input("Please enter the IP address: ")

# Run the command with the given IP address
command = f"putty.exe -ssh {ip_address} -l pi -pw lkkcict306"
subprocess.run(command, shell=True)

# Save the IP address into a file for future use
with open("ip_address.autoinput", "w") as f:
    f.write(ip_address)
