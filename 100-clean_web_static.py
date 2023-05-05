#!/usr/bin/python3
""" Deletes out-of-date archives"""
import os.path
import os
from fabric.api import *
from fabric.operations import run, put, sudo
import time
env.hosts = ['35.174.209.230', '54.157.184.171']


def do_clean(number=0):
    """ Deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    files = sorted(os.listdir("versions"))
    [files.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(j) for j in files)]

    with cd("data/web_static/releases"):
        files = run("ls -tr").split()
        files = [j for j in files if "web_static_" in j]
        [files.pop() for i in range(number)]
        [run("sudo rm -rf ./{}".format(j)) for j in files]
