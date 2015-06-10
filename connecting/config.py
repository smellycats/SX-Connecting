# -*- coding: utf-8 -*-
import os


class Config(object):
    DEBUG = True
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # 主机IP
    HOST = '0.0.0.0'
    # 端口
    PORT = '8078'
    # 用户
    USER = {'kakou': 'pingworker'}

class Develop(Config):
    pass

class Production(Config):
    DEBUG = False
