# -*- coding: utf-8 -*-

import os
import time
import logging

from flask import g, request
from flask_restful import reqparse, abort, Resource

from app import app, api, auth, logger
from ping_ip import ping


@auth.get_password
def verify_password(username):
    if username in app.config['USER']:
        return app.config['USER'].get(username)
    return None


class Index(Resource):

    def get(self):
        return {'ping_v1_url': 'http://localhost/v1/ping{/addr}'}, 200,
        {'Cache-Control': 'public, max-age=60, s-maxage=60'}


class PingApiV1(Resource):

    @auth.login_required
    def get(self, addr):
        result = ping(addr)
        logger.info('ping %s %s' % (addr, str(result)))
        return {'addr': addr, 'connect': result}, 200


api.add_resource(Index, '/')
api.add_resource(PingApiV1, '/v1/ping/<string:addr>')
