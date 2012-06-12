# -*- coding: utf-8 -*-
import os
import sys
import traceback

from flask import Flask
from flask import render_template
from jinja2 import FileSystemLoader

from version import VERSION

app = Flask(__name__)

@app.teardown_request
def teardown_request(exception):
    if exception is not None:
        traceback.print_exc()

@app.route('/')
def hello():
    app.jinja_loader = FileSystemLoader(os.path.join(app.root_path, 'templates'))
    return render_template('index.html', sys_version=sys.version, version=VERSION)

from synhighhelper import synhighhelper

if __name__ == '__main__':
    app.run(debug=True)
