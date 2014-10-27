#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# File Name : 7niu.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1413938859
# Last Modified :
# Release By : Doom.zhou
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
    r = requests.get(url) 
    path = home + "/tmp/bash_history"
    f = open(path, "w+")
    f.write(r.content);
    f.close()
def download1():
    url = "http://doombash.qiniudn.com/bash_history"
    path = home + "/tmp/1.t"
    urllib.urlretrieve(url, path)

import qiniu.rs
import qiniu.io
policy = qiniu.rs.PutPolicy("doombash:bash_history")
uptoken = policy.token()




def upload():
    localfile = "%s%s" % (home, "/.bash_history")
    ret, err = qiniu.io.put_file(uptoken, "bash_history", localfile)
    if err is not None:
        sys.stderr.write('error: %s ' % err)

if __name__ == '__main__':
    while True:
        print """
        Please choose
        1--->download
        2--->upload
        3--->quit"""
        choose = input("Input:")
        if choose == 3:
            exit()
        elif choose == 1:
            download()
        else:
            upload()
