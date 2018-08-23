#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import traceback
import urlparse

import biz.churen.util.util as util


def mkdir(_dir=None):
    print "start mkdir => " + _dir
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def download(_soft=[], _down_load_dir=None):
    for u in _soft:
        print "start download => " + u
        res = urlparse.urlparse(u)
        _file_name = (res.path.split("/"))[-1]
        if os.path.exists(_down_load_dir + _file_name):
            continue
        util.download(_down_load_dir, u)


def git_cmd(_dir=None, _git=[], _mode="init"):
    print "start init ..."
    os.chdir(_dir)
    try:
        for g in _git:
            os.chdir(_dir)
            _git_name = ((g.split("/"))[-1])[0:-4]
            _git_cmd = []
            if not os.path.exists(_dir + _git_name):
                _git_cmd = ["git", "clone", g]
            elif _mode == "commit":
                os.chdir(_dir + _git_name)
                _git_cmd = ["git", "commit", "-am", "'commit all ...'"]
            elif _mode == "merge":
                os.chdir(_dir + _git_name)
                _git_cmd = ["git", "merge"]
            elif _mode == "push":
                os.chdir(_dir + _git_name)
                _git_cmd = ["git", "push"]
            else:
                print _git_name + " do nothing ..."
            print _git_cmd
            ps = subprocess.Popen(_git_cmd)
            ps.wait()
    except Exception as ex:
        print traceback.format_exc()
    print "git pull down ..."


def do_init(_soft=[], _dir=None, _git=[]):
    print "start init ..."
    mkdir(_dir)
    _down_load_dir = _dir + "__dependency__/"
    mkdir(_down_load_dir)
    download(_soft, _down_load_dir)
    git_cmd(_dir, _git, _mode="init")
    print "init done ..."


def do_save(_dir=None, _git=[]):
    print "saving init ..."
    git_cmd(_dir, _git, _mode="commit")
    # git_cmd(_dir, _git, _mode="merge")
    git_cmd(_dir, _git, _mode="push")
    print "saving done ..."


if __name__ == '__main__':
    pass
