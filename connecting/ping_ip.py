# -*- coding: cp936 -*-
import platform
import sys
import os
import time


def get_os():
    '''
    get os ����
    '''
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"
     
def ping(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()
     
    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >=0:
            flag = True
            break
    return flag


