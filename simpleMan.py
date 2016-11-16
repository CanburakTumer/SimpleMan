#!/usr/bin/python
import ConfigParser
import urllib2
import requests

# Config File Read
cfg = ConfigParser.ConfigParser()
cfg.read("./config.conf")

# Host settings
remoteHost = cfg.get("REMOTE","ping")
remoteMail = cfg.get("REMOTE","mail")
toAddress = cfg.get("REMOTE","to")

# Dyndns settings
dyndnsUsername = cfg.get("DYNDNS", "user")
dyndnsPassword = cfg.get("DYNDNS", "password")
dyndnsHostname = cfg.get("DYNDNS", "hostname")

# Local parameters
mode = cfg.get("LOCAL", "mode")

# Get new IP from remote and old IP from local
ip = urllib2.urlopen(remoteHost).read().strip("\n")
f = open("ip","r+")
oldIP = f.read()
f.close()

# Compare IP s and process
if ip != oldIP:
	f = open("ip","w+")
	f.write(ip)
	f.close()
	url = "http://"+dyndnsUsername+":"+dyndnsPassword+"@members.dyndns.org/nic/update?hostname="+dyndnsHostname+"&myip="+ip+"&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG"
	if(mode == "MAIL"):
		urllib2.urlopen(remoteMail+"?to="+toAddress)
	elif(mode == "DYNDNS"):
		retCode = requests.get(url)
	elif(mode == "BOTH"):
                retCode = requests.get(url)
		urllib2.urlopen(remoteMail+"?to="+toAddress)
	else:
		print "Erronous work mode."


# Old school debug
#ip = "127.0.0.1"
#print oldIP
#print "Working mode " + mode
#print remoteHost
#print remoteMail
#print url+retCode.text

