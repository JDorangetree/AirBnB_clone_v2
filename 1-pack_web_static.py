#!/usr/bin/python3
"""Compress before sending"""

from datetime import datetime
from fabric.api import local hide


def do_pack():

    try:
        now = datetime.now()
        now_format = now.strftime("%Y%m%d%H%M%S")
        output = "versions/web_static_{}.tgz".format(now_format)
        print("Packing web_static to {}".format(output))

        with hide('running'):
            local("mkdir -p versions")

        local("tar -cvzf {} web_static".format(output))

        with hide('running'):
            size = local('stat -c %s {}'.format(output), capture=True)

        print("web_static packed: {} -> {}Bytes".format(output, size))

        return output

    except:
        return None
