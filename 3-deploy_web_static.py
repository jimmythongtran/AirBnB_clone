#!/usr/bin/python3
"""this creates and distributes an archive to your web servers
using the function 'deploy'"""

from datetime import datetime
from fabric.api import *
from os.path import isfile


env.hosts = ['54.91.75.76', '52.207.18.140']


def do_pack():
    file = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    local('tar -cvzf versions/web_static_%s.tgz web_static' % file)
    archive_path = 'versions/web_static_%s.tgz' % file
    return(archive_path)


def do_deploy(archive_path):
    try:
        isfile(archive_path)
        put(archive_path, "/tmp")
        filename = archive_path.split("/")[-1]
        dirname = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("sudo mkdir -p {}".format(dirname))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, dirname))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv {}/web_static/* {}".format(dirname, dirname))
        run("sudo rm -rf {}/web_static".format(dirname))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(dirname))
        return True
    except Exception:
        return False


def deploy():
    archive = do_pack()
    if not archive:
        return False
    deployment = do_deploy(archive)
    return (deployment)
