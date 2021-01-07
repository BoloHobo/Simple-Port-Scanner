#!/bin/python3
import socket

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		#print(banner)
		#socket.close()
		return banner
	except:
		
		return

def main():
	
	ip = input("Enter IP address: ")
	for i in range(1,1000):
		#port = input("enter port number: ")
		ban = retBanner(ip,int(i))
		#print(str(ban))
		if ban:
			print("[+]" + ip + ": " + str(i) + " " + str(ban))
main()
	

