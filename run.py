from connecting import app, views
from connecting import debug_logging, online_logging

if __name__ == '__main__':
    online_logging(u'logs/connecting.log')
    app.run(host='0.0.0.0', port=8078, threaded=True)
