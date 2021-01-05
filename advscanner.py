#!/bin/python3
from socket import *
import optparse
from threading import *

def connScan(host, port):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((host, port))
		print("[+] %d/tcp is Open" %port)
	except:
		print("[-] %d/tcp is Closed" %port)
	finally: 
		sock.close()

def portScan(host, port):
	try:
		tgtIP = gethostbyname(host)
	except:
		print("Unkown Host %s " %host)
	try: 
		tgtName = gethostbyaddr(tgtIP)
		print("[+] Scan results for: " + host[0])
	except:
		print('[+] Scan Results for: ')
	setdefaulttimeout(1)
	for p in port:
		t = Thread(target=connScan, args=(host, int(p)))
		t.start()
	
		

def main():
	
	parser = optparse.OptionParser('Usage of Program: ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host', default=None)
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port', default=None)
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = str(options.tgtPort).split(',')
	
	if (tgtHost == None) | (tgtPort[0] == 'None'):
		
		print(parser.usage)
		exit(0)
	portScan(tgtHost, tgtPort)

if __name__ == '__main__':
	main()


		
