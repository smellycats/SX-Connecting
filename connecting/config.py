# -*- coding: utf-8 -*-


class Config(object):
    # 密码 string
    SECRET_KEY = 'hellokitty'
    # 用户 dict
    USER = {'kakou': 'pingworker'}
    # response header Server
    HEADER_SERVER = 'SX-Connecting'


class Develop(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


class Testing(Config):
    TESTING = True
