#########################################################################
# IOS XE and RESTCONF
# Makes API call using RESTCONF and prints hostname and serial number
# Pulls ip, username and password from csv file
#########################################################################


#!/usr/bin/env python

import csv
import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

device_info = {}
dev_list = []

#--------------------------------------------------

def read_from_csv(myfile):

    csvfile = open(myfile, 'r')
    csv_in = csv.reader(csvfile)
    for dev in csv_in:
        dev_list.append(dev)
    return dev_list
    csvfile.close()	


def get_hostname():
    
    """get hostname using restconf"""
    
    auth = HTTPBasicAuth(device_info_list[1],device_info_list[2])
    headers = {'Accept': 'application/vnd.yang.data+json','Content-Type': 'application/vnd.yang.data+json'}
    url = 'http://' + device_info_list[0] + '/restconf/api/config/native/hostname'
    #url = 'http://172.16.30.23/restconf/api/config/native/hostname'
    response = requests.get(url, verify=False, headers=headers, auth=auth)
    
    #print 'Status Code: ' + str(response.status_code)
    parse = json.loads(response.text)
    hostname = parse['ned:hostname']
    
    print ''
    print 'Hostname: ', hostname

def get_serial():

    """get serial using restconf"""

    auth = HTTPBasicAuth(device_info_list[1],device_info_list[2])
    headers = {'Accept': 'application/vnd.yang.data+json', 'Content-Type': 'application/vnd.yang.data+json'}

    url = 'http://' + device_info_list[0] + '/restconf/api/config/native/license/udi'
    response = requests.get(url, verify=False, headers=headers, auth=auth)

    #print 'Status Code: ' + str(response.status_code)
    parse = json.loads(response.text)
    sn = parse['ned:udi']['sn']
	
    print 'Serial: ', sn


if __name__ == "__main__":

    read_from_csv('xe_device_list.csv')	
    for line in dev_list: #for each line in  put into the list
        device_info_list = line
		
        # call functions
        get_hostname()
        get_serial()
        print '-------------------'
 
	
