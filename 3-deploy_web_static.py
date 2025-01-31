#!/usr/bin/python3
"""
Fabric script that distributes and archive
"""
from fabric.api import *
from datetime import datetime
import shlex
import os

env.hosts = ["100.26.121.3", "100.26.159.29"]
env.user = 'ubuntu'


def do_pack():
    """ a function that generates .tgz from content
    of a folder"""

    try:
        if not os.path.exists("versions"):
            local("mkdir versions")

        time = datetime.now()
        fm = "%Y%m%d%H%M%S"
        path = 'versions/web_static_{}.tgz'.format(time.strftime(fm))
        result = local('tar -cvzf {} web_static'.format(path))
        if result.succeeded:
            size = os.stat(path).st_size
            print("web_static packed: {} -> {}Bytes".format(path, size))
            return path
        else:
            return None
    except Exception:
        return None


def do_deploy(archive_path):
    """ Deploying the archive """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        put(archive_path, "/tmp/{}".format(name))
        run("mkdir -p /data/web_static/releases/{}"
            .format(wname))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(name, wname))
        run("rm -rf /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(wname, wname))
        run("rm -rf /data/web_static/releases/{}/web_static".format(wname))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} \
                /data/web_static/current".format(wname))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    creates and distributes an archive to web server
    """
    arc = do_pack()
    if arc is None:
        return False
    else:
        return do_deploy(arc)
