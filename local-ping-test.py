# To run the script, enter:
# python3 local_ping_test.py clientlist.txt

import subprocess
from sys import argv

script, filename = argv

clients = open(filename)

print("-" * 20)
print("Performing ping test")
print("-" * 20 + "\n")

for host in clients:
	ping = subprocess.run(["ping" + " -c 3 -t 2 " + str(host)], shell=True, 
		stdout=subprocess.DEVNULL)
	returncode = ping.returncode
		
	if returncode == 0:
		print(host, "is UP \n")
	
	else:
		print(f"{host} is DOWN \n")
		
print("Ping test complete.")

clients.close()
