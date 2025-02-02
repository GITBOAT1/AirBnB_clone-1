#!/usr/bin/python3
'''fabfile tar packaging'''
from fabric.api import local, run, prefix, env
from datetime import datetime
import os
env.hosts = ['localhost']


def do_pack():
    """ do_pack must return the archive path if the archive has
    been correctly generated.
    """

    n = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month,
                                                n.day, n.hour,
                                                n.minute, n.second)
    local('sudo mkdir -p versions')
    local("sudo tar -cvzf versions/{} web_static --mode=664 ".format(name))
    size = os.stat("versions/{}".format(name)).st_size
    print("web_static packed: versions/{} -> {}Bytes".format(name, size))

    path = './versions/' + name
    if os.path.exists(path):
        return path
    else:
        return None
