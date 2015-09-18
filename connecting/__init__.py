# -*- coding: utf-8 -*-
import logging

from flask import Flask
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
