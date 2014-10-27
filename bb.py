#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import qiniu.conf
import StringIO
import sys
import os
import requests
import urllib

home = os.environ['HOME']
qiniu.conf.ACCESS_KEY = "VEB6sy7zPt-YjmmN3d6mnNaXEqLSCBR5Jh3ZwcYZ"
qiniu.conf.SECRET_KEY = "TS5AeUpSLEVSHKYk0yImw933f531Y8ybZ_WeH4PL"

def download():
    url = "http://doombash.qiniudn.com/bash_history"
    url1 = "http://doombash.qiniudn.com/.bashrc"
    path = home + "/.bash_history"
    urllib.urlretrieve(url, path)
    path1 = home + "/.bashrc"
    urllib.urlretrieve(url1, path1)
    path2 = home + "/.bash_profile"
    f = open(path2, "w+")
    f.write("""if [ -f ~/.bashrc ]; then 
        . ~/.bashrc
    fi
    """)
    f.close()

import qiniu.rs
import qiniu.io

def upload():
    policy = qiniu.rs.PutPolicy("doombash:bash_history")
    uptoken = policy.token()
    localfile = "%s%s" % (home, "/.bash_history")
    ret, err = qiniu.io.put_file(uptoken, "bash_history", localfile)
    if err is not None:
        sys.stderr.write('error: %s ' % err)
    policy = qiniu.rs.PutPolicy("doombash:.bashrc")
    uptoken = policy.token()
    localfile = "%s%s" % (home, "/.bashrc")
    ret, err = qiniu.io.put_file(uptoken, ".bashrc", localfile)
    if err is not None:
        sys.stderr.write('error: %s ' % err)

if __name__ == '__main__':
    while True:
        print """
        Please choose
        1--->download
        2--->upload
        3--->quit
        """
        choose = input("Input:")
        if choose == 3:
            exit()
        elif choose == 1:
            download()
        else:
            upload()
