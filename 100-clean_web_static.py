#!/usr/bin/python3
"""
deletes out-of-date archives
"""
from fabric.api import *
import os

env.hosts = ['3.83.238.99', '54.236.16.109']
env.user = 'ubuntu'


def do_clean(number=0):
    """
    deletes out-of-date archives
    """

    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1
    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    pth = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(pth, number))
