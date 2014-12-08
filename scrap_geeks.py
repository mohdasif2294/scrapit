#!/usr/bin/env python

import requests 
from bs4 import BeautifulSoup
import time
import sys
import array
import subprocess
import os

	
if(len(sys.argv)==1): #Checking Number of arguments
	print "\nEnter the url :"
	url=raw_input();

	if("http://" not in url): 	
		url="http://"+url

elif(len(sys.argv)>2):
	print "\nOnly One url at a time.\nTry again\n"
	exit()

else:
	url=sys.argv[1];

	if("http://" not in url):
		url="http://"+sys.argv[1]

try:
	response = requests.get(url,timeout=2.0) #parse the webpage

except:
	print "\nSession timed out: Server is not responding!\nIs your url correct ? Please Try again\n"
	exit()

if(response.status_code!=requests.codes.ok):
	print "\nError 404: Site Not Found.\nTry again with Valid Url\n"
	exit()

else:
	print "\nFetching the codes"

	for i in range(25): #Loading dots
		sys.stdout.write("...") 
		sys.stdout.flush() 
		time.sleep(0.05)
	
	soup = BeautifulSoup(response.text) #convert the page into well documented html page
	soup.encode("ascii")
	
	titl=soup.title.text
	txt=soup.find_all('pre') #finding the code section in the html

	lst=[];
	
	count=0;

	for code in txt: #counting number of codes and taking them as array elements
		lst.append(code.text)
		count+=1
	
	x=min(count,3) #Maximum number of codes to be scrapped and displayed (max:3)

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
			fd=open(fil_name[i],'w')
			fd.write(code) #writing code in the file
			fd.close()
			
			print "\nProgram Number:%d Obtained."%(i+1);
			time.sleep(0.19)
			i+=1

		app="gedit" #application to open code, It can be any other editor or IDE also (codeblocks,subl,emacs)

		if(x==1):
			try:
				subprocess.check_call([app,fil_name[0]]) #executing the code in application
			except OSError as e:
				if(e.errno==2):
					print "\n\t%s is not installed. For installation :\n\tsudo apt-get install %s" %(app,app)
				else:
					print (e)
					print "\n"

		elif(x==2):
			try:
				subprocess.check_call([app,fil_name[0],fil_name[1]])
			except OSError as e:
				if(e.errno==2):
					print "\n\t%s is not installed. For installation :\n\tsudo apt-get install %s" %(app,app)
				else:
					print (e)
					print "\n"

		else:
			try:
				subprocess.check_call([app,fil_name[0],fil_name[1],fil_name[2]])
			except OSError as e:
				if(e.errno==2):
					print "\n\t%s is not installed. For installation :\n\tsudo apt-get install %s" %(app,app)
				else:
					print (e)
					print "\n"
				


