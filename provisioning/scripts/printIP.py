#file: printIP.py
# Written By: Saed Alavinia (saedalav@gmail.com)

import sys
import urllib2
import datetime
import re

# The target Url that we are reading the IP from
targetUrl = "http://checkip.dyndns.org"		#target URL where IP address is read from
req_version = (2,7)							#minimum required version in case it is not known
cur_version = sys.version_info				#the version that the target system is running 
verbose = False								#if verbose should be printed (set to True when vagrantfile's verbose is true)
output_file = "/opt/pythonscripts/output.txt" #output file 

#This variable is part of the extended solution (branched from master)
html_root = "/var/www/html/newroot/index.html"



# Since the target machine's python version is known in advance,
# this piece of code is redundant. However, it is still a good idea to 
# check python --version so that the file is more generic
if req_version >= cur_version:
	if verbose:
   		print "The Python interpreter is old. Things might not go as smoothly"
   	#quit()

# Checking for potential responses from urllib2.request and urlopen
try:
	req = urllib2.Request(targetUrl)
	resp = urllib2.urlopen(req)
except urllib2.HTTPError as e:
	if e.code == 404: # Reaching Server, but not a valid resource #paranoia
		if verbose:
			print "Received %d from %s" %(e.code,targetUrl)
			quit()
	else: # Problem with server such as 500s, etc
		if verbose:
			print "Received %s"  %e.code
			quit()
except urllib2.URLError as e: 
	if verbose:
		print "Check your connection and/or url again."
		quit()

else: #200

	#Here, the response has been received. using regular expression
	# it attempts to extract IP address
	body = resp.read()
	pattern = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', body)
	timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) #servertimestamp
	try:
		ip = pattern[0]
		if verbose:
			print("%s | %s" %(timestamp,ip))

		# Append the output to a file in the following format:
		# <datetimestamp> | <script output>
		file = open(output_file, 'w')
		file.write("%s | %s" %(timestamp,ip))
		file.close()
	except IndexError as e: #In case IP address pattern is not available
		print "The expected IPv4 pattern was not found in the output of the provided website"
		quit()

	# This part of the scrip is just to integrate with apache 
	# and make sure everything is working
	# Otherwise creating an html document with python (or any script) 
	# is not a good idea at all!  
	file = open(html_root, 'w')
	file.write("<!DOCTYPE html>")
	file.write("<html>")
	file.write("<head><title>My Page</title></head>")
	file.write("<body>")
	file.write("%s | %s" %(timestamp,ip))
	file.write("<br /><br />Consider hiring me if you see this page :)")
	file.write("</body>")
	file.write("</html>")
	file.close()



