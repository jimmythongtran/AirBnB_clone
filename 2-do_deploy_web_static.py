#!/usr/bin/python3
"""
deploys a server
"""


from fabric.api import *
from os.path import isfile


env.hosts = ['54.91.75.76', '52.207.18.140']


def do_deploy(archive_path):
    try:
        isfile(archive_path)
        filename = archive_path.split("/")[-1]
        dirname = "/data/web_static/releases/{}".format(filename.split(".")[0])
        put(archive_path, "/tmp/")
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
