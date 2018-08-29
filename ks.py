#!/usr/bin/python
# -*- encoding: utf-8 -*-

import argparse
import os

import biz.churen.ks.init as init
import biz.churen.util.util as util

__doc__ = """
-1, 这是一个存在循环依赖的计划

0, 确定是 Win7+ 系统, 安装 Python 2.7.x 和 Git 2.17+ , 下面的 __soft__ 变量里面有下载地址 
1, 在 <当前用户目录>, 生成SSH公钥 ssh-keygen -t rsa -C "orange.lihai@foxmail.com"
   将生成的公钥 <当前用户目录>/.ssh/id_rsa.pub 添加到 github.com 和 gitee.com 和 kancloud.cn
   测试 ssh -T git@gitee.com
       ssh -T git@github.com
       ssh -T git@git.kancloud.cn
              
2, 初始化执行 ks.py --task init
3, [可选], 去目录 <__dir__>/__dependency__/ 目录下安装可能会有用的一些软件
4, [必选], 下载安装 JetBrains 相关系列 和 看云客户端(kancloud.cn)
x, 如果忘记了密码, 执行 ks.py --task k 
y, 如果要补充新的项目, 添加到 __git__ 变量里面
"""

__project_dir__ = os.path.dirname(__file__)
__conf_dir__ = __project_dir__ + "/conf/"
__soft__ = [
    # "https://npm.taobao.org/mirrors/git-for-windows/v2.17.0.windows.1/Git-2.17.0-64-bit.exe",
    # "https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi",
    # "https://www.python.org/ftp/python/2.7.15/python-2.7.15.amd64.msi"
]
__dir__ = "D:/dump/git/"
__git__ = [
    "git@gitee.com:churen/ks.git",
    "git@git.kancloud.cn:churen/docs-db.git",
    "git@git.kancloud.cn:churen/docs-base.git",
    "git@git.kancloud.cn:churen/docs-pl.git"
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
    main()
    # util.rsa_key_gen(__conf_dir__ + "/k")
    # util.rsa_encode(__conf_dir__ + "/k/", "k.dat")
    # util.rsa_decode(__conf_dir__ + "/k/", "k.dat.r")
    pass

