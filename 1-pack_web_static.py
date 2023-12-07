#!/usr/bin/python3
"""
Fabric script that generates .tgz archive from the content of webstatic folder
"""
from fabric.api import local
from datetime import datetime
import os


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
    except:
        return None
