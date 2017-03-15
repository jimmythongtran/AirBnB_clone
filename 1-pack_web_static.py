#!/usr/bin/python3
"""
this generates .tgz archive from contents of web_static folder
"""


from datetime import datetime
from fabric.api import local


def do_pack():
    file = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    local('tar -cvzf versions/web_static_%s.tgz" web_static' % file)
