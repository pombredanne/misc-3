# -*- coding: utf-8 -*-
import os
import sys

from flask import render_template
from flask.helpers import send_from_directory
from jinja2 import FileSystemLoader

from flaskapp.version import VERSION
from flaskapp.flaskapp import app

@app.route('/synhighhelper')
def synhighhelper():
    app.jinja_loader = FileSystemLoader(os.path.join(app.root_path, 'synhighhelper/templates'))
    return render_template('synhighhelper.html', sys_version=sys.version, version=VERSION)

@app.route('/synhighhelper/static/<path:filename>')
def synhighhelper_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'synhighhelper/static'), filename)
