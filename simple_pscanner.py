#!/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host = input("-"*25+"Enter IP address: "+ "-" * 25+ "\n")
port = 443

def portscanner(port):
	if sock.connect_ex((host,port)):
		return False
	else:
		return True
for i in range(1001):
	if portscanner(i):
		print("port " + str(i) + " is open")

