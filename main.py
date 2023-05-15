import subprocess
import os.path
import time

# Check if the ip_address.txt file exists
if os.path.isfile("ip_address.youcantopenithehe"):
    with open("ip_address.youcantopenithehe", "r") as f:
        ip_address = f.read().strip()
else:
    # Ask user for the IP address if the file does not exist
    ip_address = input("Please enter the IP address: ")

# Run the command with the given IP address
command = f"putty.exe -ssh 192.158.1.{ip_address} -l pi -pw lkkcict306"
subprocess.run(command, shell=True)
print("debug:"+ip_address)
print("if you see this message, you need to redownload it or you should contact me!")

# Save the IP address into a file for future use
with open("ip_address.youcantopenithehe", "w") as f:
    f.write(ip_address)
time.sleep(1)
