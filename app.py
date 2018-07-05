#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return '{ "value": 101 }'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port='80')
