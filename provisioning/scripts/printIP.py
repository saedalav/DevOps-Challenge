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

# Since the target machine's python version is known in advance,
# this piece of code is redundant. However, it is still a good idea to 
# check python --version so that the file is more generic
if req_version >= cur_version:
   print "The Python interpreter is old. Things might not go as smoothly"
   #quit()


try:
	req = urllib2.Request(targetUrl)
	resp = urllib2.urlopen(req)
except urllib2.HTTPError as e:
	if e.code == 404: # Reaching Server, but not a valid resource #paranoia
		print "Received %d from %s" %(e.code,targetUrl)
	else: # Problem with server such as 500s, etc
		print "Received %s"  %e.code
except urllib2.URLError as e: 
	print "Check your connection and/or url again."

else: #200
	print("Hello Python")