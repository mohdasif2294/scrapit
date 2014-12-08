#!/usr/bin/env python
import requests 
from bs4 import BeautifulSoup
import time
import sys
import array
import subprocess
import os
#from subprocess import CalledProcessError,check_output
#from subprocess import Popen, PIPE
import shlex

	
if(len(sys.argv)==1): #Checking Number of arguments
	print "\nEnter the url :"
	url=raw_input();

	if("http://" not in url): 	
		url="http://"+url

elif(len(sys.argv)>2):
	print "\nOnly One url is allowed at a time.........................................Try again\n"
	exit()

else:
	url=sys.argv[1];

	if("http://" not in url):
		url="http://"+sys.argv[1]

print "\nFetching the codes"

for i in range(25): #Loading dots
	sys.stdout.write("...") 
	sys.stdout.flush() 
	time.sleep(0.05)

try:
	response = requests.get(url,timeout=1.5) #parse the webpage

except:
	print "\n\nSession timed out: Server is not responding!\nPlease try again\n"
	exit()


if(response.status_code!=requests.codes.ok):
	print "\n404:Error Site Not Found..\nTry again with Valid Url\n"
	exit()

else:
	
	soup = BeautifulSoup(response.text) #convert the page into well documented html page
	soup.encode("ascii")
	
	titl=soup.title.text
	txt=soup.find_all('pre') #finding the code section in the html

	lst=[];
	
	count=0;

	for code in txt: #counting number of codes and taking them as array elements
		lst.append(code.text)
		count+=1
	
	x=min(count,3) #since only maximum of three codes are displayed!

	if(x==0):
		print "\nNo code found....!\nTry again with another URL\n"
		exit()


	else:
		
		fil_name=[]
		
		i=0

		for code in lst:
			if(i>=x):
				break	

			fil_name.append(titl+"%d.cpp"%(i+1)) #filename is created with cpp extension
			#fil_name[i]=[word.replace(" ","_") for word in fil_name[i]]
			fd=open(fil_name[i],'w')
			fd.write(code) #writing code in the file
			fd.close()
			
			print "\nProgram Number:%d Obtained."%(i+1);
			print "\n",fil_name[i]
			time.sleep(0.18)
			i+=1

		print "\n"

		app="gedit" #application to open code

		#codes=""
		
		#codes=", ".join(fil_name)
		#codes="gedit, "+codes
		#print codes,"\n"
		#print shlex.split(codes)
		#print codes.split(", "),"\n"

		if(x==1):
			subprocess.check_call([app,fil_name[0]]) #executing the code in codeblocks

		elif(x==2):
			subprocess.check_call([app,fil_name[0],fil_name[1]])

		else:
			try:
				subprocess.check_call([app,fil_name[0],fil_name[1],fil_name[2]])
			except OSError as e:
				#if(e.errno==2):
					#print "\n\t'Codeblocks' is not installed. For installation :\n\tsudo apt-get install codeblocks"
				if(e.errno==2):
					print "\n\t'gedit' is not installed. For installation :\n\tsudo apt-get install gedit"
				else:
					print (e)
					print "\n"
				


