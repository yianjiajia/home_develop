#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys, os
import subprocess
import re
filename=sys.argv[0]
DICT= {"192.168.0.30":"/home/apache-tomcat-7.0.55",
                  "192.168.0.35":"/root/apache-tomcat-7.0.55",
                  "192.168.0.39":"/root/apache-tomIcat-7.0.55"
                 }
#执行远程拷贝

def copytosever(*args):   #形式参数file为需要传递的文件；形式参数server为远端服务器IP；形式参数dir为tomcat服务器的目录
	print '#*20\n'
	print '拷贝%s到%s的%s' %(file,server,dir)
	try:
		P=subprocess.popen('scp args[0] root@args[1]:args[2]')
		p.wait()
	except IOError, e:
		print e
def changeDB(*args):
	print '#*20\n'
	print '修改数据库' 
	cmd=['mysql -uroot -p111111 < sqlfile' for sqlfile in args] 
	try:
		for x in cmd:
			P=subprocess.popen("ssh -p root@192.168.0.35 x")
			p.wait()
	except IOError, e:
		print e
def manger_tomcat():
	opt=raw_input("请输入远端服务器ip及脚本名,以空格分开\n").split()
	try:
		P=subprocess.popen("ssh -p root@ops[0]:DICT[ops[0]]/bin/opt[1]")
		p.wait()
	except IOError, e:
		print e

if __name__ == '__main__':
	if len(sys.argv) < 2:
    		print '请输入运行参数'
    		sys.exit()

	if sys.argv[1].startswith('--'):
   		option = sys.argv[1][2:]
   # fetch sys.argv[1] but without the first two characters
    	if  option == 'version':
     		print 'Version 1.0'
   		elif option == 'help':
     		print '''
           
			@author： 
			自动化部署
			usage:
			**********************************************
			*执行远程拷贝：	
			* python %s copptoserver  
			*
			*修改数据库
			* python %s changeDB 
			*
			*tomcat服务管理
			* python%s manger_tomcat start|stop|restart  
			*
			**********************************************
			'''%(filename,filename,filename)
   		else:
       		print 'Unknown option.'
       		sys.exit()
	elif sys.argv[1] == 'copytosever':
		a = []
		a = raw_input("依次输入拷贝文件、server的IP，保存目录，名称以空格分隔:\n").split()
		copytosever(a)
	elif sys.argv[1] == 'changeDB':
		b = []
		b =  raw_input("请按sql脚本的执行顺序依次输入，文件以空格分隔:\n").split()
		changeDB(b)
	else len(sys.argv) > 2:
		manger_tomcat()

	
				
