# -*- coding: utf-8 -*-
import arrow
from flask import g, request
from flask_restful import reqparse, abort, Resource

from connecting import app, api, auth, logger, access_logger
import helper_ping


@app.after_request
def after_request(response):
    """访问信息写入日志"""
    access_logger.info('%s - - [%s] "%s %s HTTP/1.1" %s %s'
                       % (request.remote_addr,
                          arrow.now().format('DD/MMM/YYYY:HH:mm:ss ZZ'),
                          request.method, request.path, response.status_code,
                          response.content_length))
    return response

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
