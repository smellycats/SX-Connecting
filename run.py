from connecting import app, views
from connecting import debug_logging, online_logging

if __name__ == '__main__':
    online_logging('log\connecting.log')
    app.run(port=8078, threaded=True)
