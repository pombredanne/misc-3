# -*- coding: utf-8 -*-
#
# Usage:
# > fab -f www/wsgiapp/tools/fabfile.py -u <username> -H <hostname> main
# in repository top directory(ec2 directory)

import os
import datetime
import traceback

from fabric.api import *

TAR = "tar"
NOW = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

if os.environ['OS'] == 'Windows_NT' and os.name == 'nt':
    env.key_filename = ["%s\\.ssh\\ec2\\al64.pem" % os.environ["USERPROFILE"]]
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
    local('rm -rf archive-*')

def test():
    run("uname -a")

def main():
    prepare_deploy()
    try:
        deploy()
    except:
        traceback.print_exc()
    finally:
        clean()
