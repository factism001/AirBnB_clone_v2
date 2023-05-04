#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""

from fabric.api import local
import time


def do_pack():
    time_display = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_display))
        return ("versions/web_static_{}.tgz".format(time_display))
    except Exception:
        return None
