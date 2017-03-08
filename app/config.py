# -*- coding: utf-8 -*-


class Config(object):
    # 密码 string
    SECRET_KEY = 'hellokitty'
    # 服务器名称
    HEADER_SERVER = 'SX-Connecting'
    # 用户 dict
    USER = {'kakou': 'pingworker'}


class Develop(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


class Testing(Config):
    TESTING = True
