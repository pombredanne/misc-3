# -*- coding: utf-8 -*-
#
# Usage:
# > fab -f www/wsgiapp/tools/fabfile.py -u <username> -H <hostname> main
# in repository top directory

import os
import datetime

from fabric.api import *

TAR = "tar"
NOW = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
if os.environ['OS'] == 'Windows_NT' and os.name == 'nt':
    env.key_filename = ["d:\\kawasaki_takeshi\\mydoc\\Downloads\\al64.pem"]
    TAR = "c:\\cygwin\\bin\\tar.exe"

def export():
    local('git checkout-index -a --prefix=archive-%s/' % NOW)
    local('%s czvf archive-%s.tgz archive-%s' % (TAR, NOW, NOW))

def modify():
    pass

def prepare_deploy():
    export()
    modify()

def deploy():
    put("archive-%s.tgz" % NOW, "/home/ec2-user")
    with cd("/home/ec2-user"):
        run('tar xvzf archive-%s.tgz' % NOW)
        run('rm -rf www/')
        run('mv archive-%s/www www' % NOW)
        run('rm -rf archive-%s' % NOW)
        run('touch www/wsgiapp/flaskapp/flaskapp.wsgi')

def clean():
    local('rm -rf archive-*' % NOW)

def main():
    prepare_deploy()
    deploy()
    clean()
