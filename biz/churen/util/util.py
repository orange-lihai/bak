#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

requests.packages.urllib3.disable_warnings()


def download(_dir, _url):
    if not os.path.exists(_dir): os.mkdir(_dir)
    _file_name = os.path.basename(_url)
    r = requests.get(_url, stream=True, verify=False)

    total_size = int(r.headers['Content-Length'])
    temp_size = 0

    with open(_dir + _file_name, "w") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                done = int(50 * temp_size / total_size)
                sys.stdout.write("\r[%s%s] %d%%" % ('=' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print()


def rsa_key_gen(_dir=None):
    if not os.path.exists(_dir): os.mkdir(_dir)
    random_generator = Random.new().read
    # 单次加密串的长度最大为 (key_size/8)-11
    rsa = RSA.generate(1024, random_generator)
    private_pem = rsa.exportKey()
    with open(_dir + '/ghost-private.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open(_dir + '/ghost-public.pem', 'wb') as f:
        f.write(public_pem)


def rsa_encode(_dir=None, _file=None, length=100):
    cipher_text = []
    with open(_dir + "/" + _file, "r") as f:
        message = f.read()

    with open(_dir + '/ghost-public.pem', "r") as f:
        key = f.read()
        rsa_key = RSA.importKey(key)
        cipher = PKCS1_v1_5.new(rsa_key)  # 生成对象
        for i in range(0, len(message), length):
            _m = message[i:i + length]
            cipher_text.append(cipher.encrypt(_m))

    with open(_dir + _file + ".r", "w") as f:
        f.write(base64.b64encode("".join(cipher_text)))
        f.flush()


def rsa_decode(_dir=None, _file=None, length=128, _out_file=None):
    plain_text = []
    with open(_dir + "/" + _file, "r") as f:
        message = f.read()

    message = base64.b64decode(message)
    with open(_dir + '/ghost-private.pem') as f:
        key = f.read()
        rsa_key = RSA.importKey(key)
        cipher = PKCS1_v1_5.new(rsa_key)
        for i in range(0, len(message), length):
            _m = message[i:i + length]
            plain_text.append(cipher.decrypt(_m, "ERROR"))

    if _out_file is not None and os.path.exists(_out_file):
        with open(_out_file, "w") as f:
            f.write("".join(plain_text))
            f.flush()
    else:
        print "".join(plain_text)
    pass


if __name__ == '__main__':
    # link = r'https://npm.taobao.org/mirrors/git-for-windows/v2.17.0.windows.1/Git-2.17.0-64-bit.exe'
    # download(".", link)
    pass
