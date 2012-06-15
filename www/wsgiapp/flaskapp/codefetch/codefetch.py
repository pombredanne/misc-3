# -*- coding: utf-8 -*-
import os
import sys

from flask import render_template
from flask.helpers import send_from_directory
from jinja2 import FileSystemLoader

from flaskapp.version import VERSION
from flaskapp.flaskapp import app

@app.route('/codefetch')
def codefetch():
    app.jinja_loader = FileSystemLoader(os.path.join(app.root_path, 'codefetch/templates'))
    return render_template('codefetch.html', sys_version=sys.version, version=VERSION)

@app.route('/codefetch/static/<path:filename>')
def codefetch_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'codefetch/static'), filename)
