# -*- coding: utf-8 -*-

import os
import time
import logging

from flask import g, request
from flask_restful import reqparse, abort, Resource

from app import app, api, auth, logger
from ping_ip import ping


@auth.verify_password
def verify_password(username, password):
    return app.config['USER'].get(username,'') == password


class Index(Resource):

    def get(self):
        return {'ping_v1_url': 'http://localhost/v1/ping{/addr}'}


class PingApiV1(Resource):

    @auth.login_required
    def get(self, addr):
        result = ping(addr)
        try:
            logger.info('ping %s %s' % (addr, str(result)))
        except Exception as e:
            raise
        return {'addr': addr, 'connect': result}, 200


api.add_resource(Index, '/')
api.add_resource(PingApiV1, '/v1/ping/<string:addr>')
