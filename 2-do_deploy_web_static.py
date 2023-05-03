#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ["35.174.209.230", "54.157.184.171"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arch = archive_path.split("/")
        uncomp = arc[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(uncomp))
        new = "/data/web_static/releases/{}".format(uncomp)
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], new))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(new, new))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(new))
        return True
    except:
        return False
