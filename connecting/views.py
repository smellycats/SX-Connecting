# -*- coding: utf-8 -*-

from flask import g, request
from flask_restful import reqparse, abort, Resource

from app import app, api, auth, logger
from ping_ip import ping


@auth.get_password
def get_pw(username):
    if username in app.config['USER']:
        return app.config['USER'].get(username)
    return None


class Index(Resource):

    def get(self):
        return {'ping_url': 'http://127.0.0.1:%s/v1/ping/:ip' %
                app.config['PORT']}, 200,
        {'Cache-Control': 'public, max-age=60, s-maxage=60'}


class PingApi(Resource):

    @auth.login_required
    def get(self, ip):
        result = ping(ip)
        logger.info('ping %s %s' % (ip, str(result)))
        return {'ip': ip, 'connect': result}, 200


api.add_resource(Index, '/')
api.add_resource(PingApi, '/ping/<string:ip>')
