# -*- coding: utf-8 -*-
import os


class Config(object):
    # 密码 string
    SECRET_KEY = 'hellokitty'
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # 主机IP string
    HOST = '0.0.0.0'
    # 端口 string
    PORT = '8078'
    # 用户 dict
    USER = {'kakou': 'pingworker'}

class Develop(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False
