# -*- coding: utf-8 -*-
import arrow
from flask import g, request, jsonify
from flask_restful import reqparse, abort, Resource

from connecting import app, api, auth, logger, access_logger
import helper_ping


@auth.get_password
def get_pw(username):
    if username in app.config['USER']:
        return app.config['USER'].get(username)
    return None


class Index(Resource):

    def get(self):
        return {
            'ping_url': 'http://%s:%s/ping/:ip' % (request.remote_addr, app.config['PORT'])
        }, 200, {'Cache-Control': 'public, max-age=60, s-maxage=60'}


class PingApi(Resource):

    @auth.login_required
    def get(self, ip):
        result = helper_ping.ping(ip)
        return {'ip': ip, 'connect': result}, 200


api.add_resource(Index, '/')
api.add_resource(PingApi, '/ping/<string:ip>')
