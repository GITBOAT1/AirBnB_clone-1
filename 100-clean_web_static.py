#!/usr/bin/python3
'''fabfile tar packaging'''
from fabric.api import local, run, env, put, cd
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.237.3.197', '54.152.230.84']


def do_pack():
    """ Packes web_static in tgz format
    """

    n = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(
        n.year, n.month, n.day, n.hour, n.minute, n.second)
    local('mkdir -p versions')
    local("tar -cvzf versions/{} web_static".format(name))
    size = os.stat("versions/{}".format(name)).st_size
    print("web_static packed: versions/{} -> {}".format(name, size))
    path = "versions/{}".format(name)
    return (path)


def do_deploy(archive_path):
    """ Deploy Archeve """

    if not archive_path:
        return (False)
    name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run(" sudo mkdir -p /data/web_static/releases/{}".format(name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, name))
        run("sudo rm /tmp/{}".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name, name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed")
        return (True)
    except BaseException:
        return (False)


def deploy():
    """ Deploy achive """
    try:
        path = do_pack()
    except BaseException:
        return (False)
    do_deploy(path)


def do_clean(number=0):
    """ deletes out-of-date archives, using the function
    """

    if number == 0 or number == 1:
        with cd.local('./versions/'):
            run('ls -t | tail -n +2 | xargs rm --')
        with cd.local('/data/web_static/releases/'):
            run('ls -t | tail -n +2 | xargs rm --')
    else:
        with cd.local('./versions/'):
            run('ls -t | tail -n +2 | xargs rm --')
        with cd.local('/data/web_static/releases/'):
            run('ls -t | tail -n +2 | xargs rm --')
