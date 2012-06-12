# -*- coding: utf-8 -*-
import os
import sys
import traceback

from flask import Flask
from flask import render_template
from flask.helpers import send_from_directory
from version import VERSION
from jinja2 import FileSystemLoader

app = Flask(__name__)

@app.teardown_request
def teardown_request(exception):
    if exception is not None:
        traceback.print_exc()

@app.route('/')
def hello():
    app.jinja_loader = FileSystemLoader(os.path.join(app.root_path, 'templates'))
    return render_template('index.html', sys_version=sys.version, version=VERSION)

@app.route('/synhighhelper')
def synhighhelper():
    app.jinja_loader = FileSystemLoader(os.path.join(app.root_path, 'synhighhelper/templates'))
    return render_template('synhighhelper.html', sys_version=sys.version, version=VERSION)

@app.route('/synhighhelper/static/<path:filename>')
def synhighhelper_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'synhighhelper/static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
