# -*- mode: python -*-
a = Analysis(['C:\\Users\\wen\\Documents\\GitHub\\SX-Connecting\\run.py'],
             pathex=['C:\\Users\\wen\\Documents\\GitHub\\SX-Connecting\\app'],
             hiddenimports=["flask",
    					 "flask.views",
    					 "flask.signals",
    					 "flask.helpers",
               "flask_limiter",
               "flask_limiter.errors",
               "flask_limiter.extension",
               "flask_limiter._version",
               "flask_limiter.util",

							],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Connecting.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , version='C:\\Users\\wen\\Documents\\GitHub\\SX-Connecting\\docs\\file_version_info.txt', icon='C:\\Users\\wen\\Documents\\GitHub\\SX-Connecting\\icons\\logo.ico')
