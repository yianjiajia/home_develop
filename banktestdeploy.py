#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os,time,re,sys,threading
import datetime,subprocess,shlex
class AutoDeploy(object):
	BASE_DIR=os.path.abspath(os.path.dirname(__file__))
    DIRLIST=os.path.listdir(BASE_DIR)
    def __init__(self,zidian):
		self.zidian={"192.168.0.30":"/home/apache-tomcat-7.0.55",\
				"192.168.0.35":"/root/apache-tomcat-7.0.55",\
				"192.168.0.39":"/root/apache-tomcat-7.0.55"}
                
      
    def copytoserver(self):
        print("执行远程拷贝")
        list1=[]
        for i in DIRLIST:
			list1.append(re.match("[sql|war]$",i))
			for k,v in self.zidian.items():
				try:    
                    P=subprocess.Popen("scp BASE_DIR/* root@k:v",shell=True)
					P.wait()
                except IOError, e:
                    print "远程拷贝失败" 

                else:   
                    break   
    def changeDB(self):
        SQL=raw_input("请按sql脚本的执行顺序依次输入，文件以空格分隔:\n").split()
		print ("修改数据库")
		for i in SQL:
                try:
                    P=subprocess.Popen("ssh -p root@self.t2 'mysql -uroot -p111111 < i")
					P.wait()
                except except IOError, e:
                    print "操作数据库失败"
	
					
if "__name__" == "__main__":
	
