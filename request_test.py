# -*- coding: utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

def send_get(url,headers = {'content-type': 'application/json'}):
    """POST请求"""
    r = requests.get(url, headers=headers,
                     auth=HTTPDigestAuth('kakou', 'pingworker'))

    return r

def auth_test(url):
    headers = {'Authorization': 'Digest kakou="pingworker"',
               'content-type': 'application/json'}
    r = requests.get(url, headers=headers)

    return r

if __name__ == '__main__':  # pragma nocover
    #TestHttpPost()
    url = 'http://127.0.0.1:8078/v1/ping/127.0.0.1'
    #json_data = json.dumps(['http://localhost/imgareaselect/imgs/1.jpg','http://localhost/imgareaselect/imgs/2.jpg'])
    r = send_get(url)
    #r = auth_test(url)
    print r.status_code
    print r.text
