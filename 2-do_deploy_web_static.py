#!/usr/bin/python3
"""distributes an archive to web servers"""

from fabric.api import *
from os import path
env.hosts = ['35.185.29.20', '54.173.52.5']


def do_deploy(archive_path):
    """
    Distributes an directory to a web server
    """
    zipped_file = archive_path.split("/", 1)[1]
    unzipped_file = zipped_file.split(".", 1)[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(unzipped_file))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(zipped_file, unzipped_file))
        run("sudo rm /tmp/{}".format(zipped_file))
        run("sudo rm -r /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}/ \
            /data/web_static/current".format(unzipped_file))
        return True
    except:
        return False
