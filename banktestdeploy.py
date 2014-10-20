#-*- coding: utf-8 -*-
__author__ = 'Administrator'
#!/usr/bin/env python

import os,sys,re,threading

import datetime , subprocess , shlex
class AutoDeploy(object):
    '''自动部署银监会测试环境'''
    def __init__(self,zidian,BASE_DIR,DIRLIST,LOCK1,LOCK2):
        self.zidian = {"192.168.0.30":"/home/apache-tomcat-7.0.55",\
				    "192.168.0.35":"/root/apache-tomcat-7.0.55",\
				    "192.168.0.39":"/root/apache-tomcat-7.0.55"}
        self.BASE_DIR = sys.path.abspath(sys.path.dirname(__file__))
        self.DIRLIST = sys.path.listdir(BASE_DIR)
        self.LOCK1 = threading.Lock()
        self.LOCK2 = threading.Lock()
    def copyToServer(self):

        print("执行远程拷贝")
        list1 = []
        for i in self.DIRLIST:
            self.LOCK1.acquire()
            list1.append(re.match("[sql|war]$",i))
            for k,v in self.zidian.items():
                try:
                    P = subprocess.Popen("scp BASE_DIR/* root@k:v",shell=True)
                    P.wait()
                except IOError, e:
                    print "远程拷贝失败"

                finally:
                    self.LOCK1.release()


    def changeDb(self):
        SQL = raw_input("请按sql脚本的执行顺序依次输入，文件以空格分隔:\n").split()
        print ("修改数据库")
        for i in SQL:
                self.LOCK2.acquire()
                try:
                    P=subprocess.Popen("ssh -p root@self.t2 'mysql -uroot -p111111 < i")
                    P.wait()
                except  IOError, e:
                    print "操作数据库失败"
                finally:
                    self.LOCK2.release()

    def manageService(self):


if "__name__" == "__main__":
    serv = AutoDeploy()
    t = threading.Thread( target = serv.copyToServer, name = 'copy file to remote server' )
    t.start()
    t.join()
    p = threading.Thread( target = serv.changeDb,name = 'configure mysql')
    p.start()
    p.join()