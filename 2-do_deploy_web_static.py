#!/usr/bin/python3
'''fabfile tar packaging'''
from fabric.api import local, run, env, put
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['35.237.95.74', '35.185.23.42']


def do_pack():
    '''Packes web_static in tgz format'''
    n = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(n.year, n.month,
                                                n.day, n.hour,
                                                n.minute, n.second)
    local('mkdir -p versions')
    local("tar -cvzf versions/{} web_static".format(name))
    size = os.stat("versions/{}".format(name)).st_size
    print("web_static packed: versions/{} -> {}".format(name, size))


def do_deploy(archive_path):
    """ distributes an archive to your web servers, using the function """
    if not archive_path:
        return (False)
    name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}".format(name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, name))
        run("sudo rm /tmp/{}".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name, name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed")
        return (True)
    except BaseException:
        return (False)
