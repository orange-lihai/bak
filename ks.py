#!/usr/bin/python
# -*- encoding: utf-8 -*-

import argparse
import os

import biz.churen.ks.init as init
import biz.churen.util.util as util

__project_dir__ = os.path.dirname(__file__)
__conf_dir__ = __project_dir__ + "/conf/"
__soft__ = [
    "https://npm.taobao.org/mirrors/git-for-windows/v2.17.0.windows.1/Git-2.17.0-64-bit.exe"
]
__dir__ = "D:/dump/git/"
__git__ = [
    "git@gitee.com:churen/ks.git"
]


def main():
    parser = argparse.ArgumentParser(description='ks script ...')
    parser.add_argument('--task', default='UnKnow-Task')
    args = parser.parse_args()
    # print args.task
    task = args.task
    if task == 'init':
        init.do_init(__soft__, __dir__, __git__)
    elif task == 'k':
        util.rsa_decode(__conf_dir__ + "/k/", "k.dat.r")
    elif task == 'save':
        init.do_save(__dir__, __git__)
    else:
        print 'UnKnow --task ' + task


if __name__ == '__main__':
    # main()
    # util.rsa_key_gen(__conf_dir__ + "/k")
    # util.rsa_encode(__conf_dir__ + "/k/", "k.dat")
    # util.rsa_decode(__conf_dir__ + "/k/", "k.dat.r")
    pass

