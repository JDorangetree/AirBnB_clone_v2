#!/usr/bin/python3
"""creates and distributes an archive to your web servers"""

from fabric.api import *
from os import path
from datetime import datetime
env.hosts = ['35.185.29.20', '54.173.52.5']


def deploy():
    """deploy it on your servers"""

    my_path = do_pack()
    if my_path is None:
        return False
    return do_deploy(my_path)


def do_pack():

    try:
        now = datetime.now()
        now_format = now.strftime("%Y%m%d%H%M%S")
        output = "versions/web_static_{}.tgz".format(now_format)
        print("Packing web_static to {}".format(output))

        with hide('running', 'stdout', 'stderr'):
            local("mkdir -p versions")

        local("tar -cvzf {} web_static".format(output))

        with hide('running', 'stdout', 'stderr'):
            size = local('stat -c %s {}'.format(output), capture=True)

        print("web_static packed: {} -> {}Bytes".format(output, size))

        return output

    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an directory to a web server
    """
    if not path.exists(archive_path):
        return False
    zipped_file = archive_path.split("/", 1)[1]
    unzipped_file = zipped_file.split(".", 1)[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(unzipped_file))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(zipped_file, unzipped_file))
        run("sudo rm /tmp/{}".format(zipped_file))
        run("sudo rm -r /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}/web_static \
            /data/web_static/current".format(unzipped_file))
        print("New version deployed!")
        return True
    except:
        return False
