#!/usr/bin/env python

import unittest
import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

username = 'admin'
password = 'P@ssw0rd'
hostname = '172.16.30.23'

class TestDeviceConfiguration(unittest.TestCase):

    def test_snmp_ro(self):
        """Validate snmp RO string name
        """
        auth = HTTPBasicAuth(username, password)
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://172.16.30.23/restconf/api/config/native/snmp-server?deep'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        community_list = parse['ned:snmp-server']['community']
        expected = {'name': 'public', 'RO': [None]}
        is_there = expected in community_list
        self.assertTrue(is_there)


    def test_user(self):
        """Validate user exists
        """

        auth = HTTPBasicAuth(username,password)
        headers = { 'Accept': 'application/vnd.yang.data+json'}
        url = 'http://172.16.30.23/restconf/api/config/native'
        response = requests.get(url, verify=False, headers=headers, auth=auth)

        parse = json.loads(response.text)
        user_list = parse['ned:native']['username']
        expected = {'name': 'test'}
        is_there = expected in user_list
        self.assertTrue(is_there)


if __name__ == "__main__":
    unittest.main()