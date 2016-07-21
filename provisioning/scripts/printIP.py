#file: printIP.py
# Written By: Saed Alavinia (saedalav@gmail.com)

import sys
import urllib2
import datetime
import re

# The target Url that we are reading the IP from
targetUrl = "http://checkip.dyndns.org"
req_version = (2,7)
cur_version = sys.version_info
verbose = False


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
	else: # Problem with server such as 500s, etc
		if verbose:
			print "Received %s"  %e.code
except urllib2.URLError as e: 
	if verbose:
		print "Check your connection and/or url again."

else: #200
	if verbose:
		print("Hello Python")