import pyfiglet
import sys
import socket
import threading
from datetime import datetime

# Print the banner for the script
ascii_banner = pyfiglet.figlet_format("VERN TOOL")
print(ascii_banner)

# Function to scan a single port
def scan_port(port):
    try:
        socketRange = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = socketRange.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        socketRange.close()
    except KeyboardInterrupt:
        print("\n Exiting Program..")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved..")
        sys.exit()
    except socket.error:
        print("\n Server is not responding..")
        sys.exit()

# Function for regular scanning
def regular_scan():
    try:
        for port in range(1, 65535):
            scan_port(port)
    except KeyboardInterrupt:
        print("\n Exiting Program..")
        sys.exit()

# Function for turbo threading scanning
def turbo_threading():
    threads = []
    try:
        for port in range(1, 65535):
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n Exiting Program..")
        sys.exit()

# Read if the user is providing enough commands for the tool
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    scan_mode = "regular"
elif len(sys.argv) == 3 and sys.argv[2] == "-turbo":
    target = socket.gethostbyname(sys.argv[1])
    scan_mode = "turbo"
else:
    print("Invalid amount of Arguments")
    sys.exit()

# Get the current time
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: ", dt_string)
print("Scan Type: " + scan_mode)
print("-" * 50)

# Invoke the appropriate scanning function
if scan_mode == "regular":
    regular_scan()
elif scan_mode == "turbo":
    turbo_threading()
