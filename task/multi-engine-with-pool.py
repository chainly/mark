"""
Every 0.1s: ps -ef|grep 'python3' && netstat -ntp 2>&1|grep 'python3'                                                                                Fri Jun  1 11:04:06 2018

xxx     541 17426  0 11:04 pts/237  00:00:00 sh -c ps -ef|grep 'python3' && netstat -ntp 2>&1|grep 'python3'
xxx     547   541  0 11:04 pts/237  00:00:00 grep python3
xxx   17426  5663  2 May31 pts/237  00:16:44 watch -n 0.1 ps -ef|grep 'python3' && netstat -ntp 2>&1|grep 'python3'
xxx   32600 15008  8 11:03 pts/137  00:00:01 python3 t1.py
xxx   32638 32600  0 11:03 pts/137  00:00:00 python3 t1.py
xxx   32643 32600  0 11:03 pts/137  00:00:00 python3 t1.py
xxx   32644 32600  0 11:03 pts/137  00:00:00 python3 t1.py
tcp        0     11 10.165.121.200:37040        100.99.17.55:3306           ESTABLISHED 32643/python3
tcp        0     11 10.165.121.200:37041        100.99.17.55:3306           ESTABLISHED 32644/python3

"""

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/5/29 上午10:59
# @Author   : xxx
# @File     : multi-engine.py
# @Software : SocialPeta
# @Function :


import os
import sys
# ad project path to sys.path
# @TODO: is there better method or any file spider must load?
project_path = os.path.abspath(os.path.join(__file__, '../..'))
if project_path not in sys.path:
    print(project_path)
    sys.path.append(project_path)

import multiprocessing
from multiprocessing import reduction
from pymysql import connections
connections.DEBUG = False


import time
from scrapy.cmdline import execute
from scrapy.utils.project import inside_project, get_project_settings
settings = get_project_settings()

from playhouse.pool import PooledMySQLDatabase
from peewee import MySQLDatabase, Model
from peewee import IntegerField, CharField, DateTimeField
import socket
import errno

#线下机器环境
HOST = XXX
USER = XXX
PASSWORD = XXX
PORT = 3306

# # sock already do something: eg, serverinfo, auth , but we can't skip it
# # so we just make sock here
#
# def get_database(database):
#     # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#PooledDatabase
#     return PooledMySQLDatabase(host=HOST, user=USER, passwd=PASSWORD, port=PORT, database=database,
#                                max_connections=3, stale_timeout=180, timeout=None)
#
# sp_raw_database = get_database('sp_raw')
# vp_user_database = get_database('vp_user')




sys.argv = sys.argv[:1] + ["crawl", "ad"]


def e(argv, settings=settings):
    execute(argv=argv, settings=settings)
    time.sleep(60)

from api.models.vp_user.proxy import Proxy

def t(i, l, q):
    pid = os.getpid()
    ppid = os.getppid()
    f, args = q.get()
    s = f(*args)
    print(pid, ppid, i, s)
    time.sleep(2)

    Proxy._meta.database.connect_params.update({"defer_connect":True})
    c = Proxy._meta.database._connect()
    #c._sock = s
    c.connect(sock=s)
    print(pid, ppid, i, s, c, c._sock)
    time.sleep(10)

    Proxy._meta.database._state.set_connection(c)
    print(pid, ppid, i, Proxy._meta.database._state.conn._sock)

    r = Proxy.select().limit(1).get()
    print(i, r.__data__, Proxy._meta.database.__dict__, Proxy._meta.database._state.__dict__)
    time.sleep(10)


n=2

#e(sys.argv)
manager = multiprocessing.Manager()
q = manager.Queue()

p = multiprocessing.Pool(n)

pp = []

for i in range(n):
    # #p.map(e, [sys.argv]*5)
    # s = vp_user_database._connect()
    # # Proxy._meta.database._state.set_connection(s)
    # print(Proxy._meta.database.__dict__, Proxy._meta.database._state.__dict__)
    # #
    # # c = Proxy.select().limit(1)
    # # print(c, Proxy._meta.database.__dict__, Proxy._meta.database._state.__dict__)
    #
    # # @TODO: why s = vp_user_database._connect()._sock is closed!

    # q.put(reduction._reduce_socket(s._sock))

    kwargs = {}
    # if self.bind_address is not None:
    #     kwargs['source_address'] = (self.bind_address, 0)
    db = Proxy._meta.database
    while True:
        try:
            sock = socket.create_connection(
                (db.connect_params["host"], db.connect_params["port"]),
                db.connect_params.get("connect_timeout", 10),
                **kwargs)
            break
        except (OSError, IOError) as e:
            if e.errno == errno.EINTR:
                continue
            raise
    # self.host_info = "socket %s:%d" % (self.host, self.port)
    # if DEBUG: print('connected using socket')
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.settimeout(None)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    # socket at ppid
    #pp.append(sock)
    print(pp, sock)
    q.put(reduction._reduce_socket(sock))
    # socket at pid
    del sock
    p.apply_async(t, (i, sys.argv, q), error_callback=lambda r: print(r))

p.close()
p.join()
