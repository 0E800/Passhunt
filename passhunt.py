#!/usr/bin/python
'''
This tool allows you to search for 
Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar
'''
import os, sys
import urllib.request
import io
import bs4 as bs
	
def logo():
	logo = '''
  ____               _   _             _   
 |  _ \ __ _ ___ ___| | | |_   _ _ __ | |_ 
 | |_) / _` / __/ __| |_| | | | | '_ \| __|
 |  __/ (_| \__ \__ \  _  | |_| | | | | |_ 
 |_|   \__,_|___/___/_| |_|\__,_|_| |_|\__|
 ░░░░  ███████ ]▄▄▄▄▄▄▄▄          
█▄█████████████▄█          	      Author: Viral Maniar
[████████████████████].   	      Twitter: @ManiarViral
 ..◥ ▲ ▲ ▲ ▲ ▲ ▲ ◤..      	     Description: This tool is to search default credentials for routers, network devices, web applications and more. 
								                   ***523 vendors, 2084 passwords***
 '''
	return logo

OPTIONS = '''
1. List supported vendors
2. Search Default Password
3. Exit
'''

def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkInternetConnection():
		try:
			urllib.request.urlopen('https://cirt.net/')
		except:
			print('[!] No internet connection...Please connect to the Internet')
		else:
			print('[+] Checking Internet connection...')
						

def cmd_vendorSearch():

	vendor = input('Enter Vendor Name:').lower()
	urlenc = urllib.parse.quote(vendor)
	url = "https://cirt.net/passwords?vendor=" + urlenc
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	#response = urllib.quote(request)
	#print (response.read().decode('utf-8'))
	soup = bs.BeautifulSoup(response, "html.parser")
	#print(soup.find_all('a'))
	for links in soup.find_all('table'):
		print(links.text)
		

def cmd_openFile():	
	path = './vendors.txt'
	vendors_file = open(path,'r')
	vendors = vendors_file.read()
	print(vendors)
	
cmds = {
	"1" : cmd_openFile,
	"2"	: cmd_vendorSearch,
	"3"	: lambda: sys.exit(0)
}

		
def main():
	print (logo())
	checkInternetConnection()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
