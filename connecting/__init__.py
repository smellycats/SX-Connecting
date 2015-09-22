# -*- coding: utf-8 -*-
import logging

import arrow
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth, HTTPDigestAuth
from peewee import SqliteDatabase

from config import Production
from my_logger import debug_logging, online_logging, access_logging


app = Flask(__name__)
app.config.from_object(Production())
api = Api(app)

debug_logging(u'logs/error.log')
access_logging(u'logs/access.log')

auth = HTTPBasicAuth()

logger = logging.getLogger('root')
access_logger = logging.getLogger('access')

import connecting.views

@app.after_request
def after_request(response):
    """访问信息写入日志"""
    access_logger.info('%s - - [%s] "%s %s HTTP/1.1" %s %s'
                       % (request.remote_addr,
                          arrow.now().format('DD/MMM/YYYY:HH:mm:ss ZZ'),
                          request.method, request.path, response.status_code,
                          response.content_length))
    response.headers['Server'] = 'SX-Connecting'
    return response

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'Not Found'}), 404, {'Content-Type': 'application/json; charset=utf-8'}

@app.errorhandler(500)
def inte_ser_error(error):
    return jsonify({'message': 'Internal Server Error'}), 500, {'Content-Type': 'application/json; charset=utf-8'}
