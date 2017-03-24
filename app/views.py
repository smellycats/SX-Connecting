# -*- coding: utf-8 -*-
import arrow
from flask import g, request, jsonify
#from flask_restful import reqparse, abort, Resource

from . import app, auth, logger, access_logger
import helper_ping


@app.route('/')
#@limiter.limit("600/minute")
#@auth.login_required
def index_get():
    result = {
        u'ping_url': '%sping{/ip}' % (request.url_root)
    }
    header = {'Cache-Control': 'public, max-age=60, s-maxage=60'}
    return jsonify(result), 200, header


@app.route('/ping/<string:ip>', methods=['GET'])
#@limiter.limit("600/minute")
#@auth.login_required
def ping_get(ip):
    result = helper_ping.ping(ip)
    return jsonify({'ip': ip, 'connect': result}), 200


@app.route('/server/<string:ip>/<int:port>', methods=['GET'])
#@limiter.limit("600/minute")
#@auth.login_required
def server_get(ip, port):
    result = helper_ping.check_server(ip, port)
    return jsonify({'ip': ip, 'port': port, 'status': result}), 200
