import sys

from flask import Flask
from flask import render_template
from version import VERSION

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', sys_version=sys.version, version=VERSION)

if __name__ == '__main__':
    app.run(debug=True)
