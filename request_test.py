# -*- coding: utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth

def send_get(url,headers = {'content-type': 'application/json'}):
    """POST请求"""
    r = requests.get(url, headers=headers,
                      auth=HTTPBasicAuth('kakou', 'pingworker'))

    return r
  
if __name__ == '__main__':  # pragma nocover
    #TestHttpPost()
    urlstr = 'http://127.0.0.1:8078/v1/ping/127.0.0.1'
    #json_data = json.dumps(['http://localhost/imgareaselect/imgs/1.jpg','http://localhost/imgareaselect/imgs/2.jpg'])
    r = send_get(urlstr)
    print r.status_code
    print r.text
