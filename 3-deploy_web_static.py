#!/usr/bin/python3
"""creates and distributes an archive to web servers"""
import os.path
import time
from fabric.operations import run, put, sudo
from fabric.api import *
env.hosts = ['35.174.209.230', '54.157.184.171']


def do_pack():
    """creates archive to web servers"""
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        nconfig = archive_path.split("/")[-1]
        ndir = ("/data/web_static/releases/" + nconfig.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(ndir))
        run("sudo tar -xzf /tmp/{} -C {}".format(nconfig, ndir))
        run("sudo rm /tmp/{}".format(nconfig))
        run("sudo mv {}/web_static/* {}/".format(ndir, ndir))
        run("sudo rm -rf {}/web_static".format(ndir))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(ndir))
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to web servers"""
    try:
        archive_address = do_pack()
        val = do_deploy(archive_address)
        return val
    except Exception:
        return False
