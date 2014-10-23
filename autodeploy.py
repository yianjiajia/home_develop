#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys, os
import subprocess
import re
import shlex
filename=sys.argv[0]
DICT= {'192.168.0.30':'/home/apache-tomcat-7.0.55',
                  '192.168.0.35':'/root/apache-tomcat-7.0.55',
                  '192.168.0.39":"/root/apache-tomIcat-7.0.55'
                 }
#执行远程拷贝

def copytosever():   #形式参数file为需要传递的文件；形式参数server为远端服务器IP；形式参数dir为tomcat服务器的目录
	print '#*20\n'
	line = raw_input("依次输入拷贝文件、server的IP，保存目录，名称以空格分隔:\n").split()
	command_line = ['ssh',line[0],'root@'+line[1]+':'+line[2]]
	args = shlex.split(command_line)
	try:
		P = subprocess.Popen(args)
		p.wait()
	except IOError, e:
		print e
def changeDB(*args):
	print '#*20\n'
	sql =  raw_input("请按sql脚本的执行顺序依次输入，文件以空格分隔:\n").split()
	cmd = ['mysql -uroot -p111111 < sqlfile' for sqlfile in args] 
	args = shlex.split(cmd)
	try:
		for x in cmd:
			P = subprocess.Popen(args)
			p.wait()
	except IOError, e:
		print e
def manger_tomcat():
	opt = raw_input("请输入远端服务器ip及脚本名,以空格分开\n").split()
	command_line = ['ssh','root@'+line[0],DICT[line[0]]+'/'+line[1]]
	args = shlex.split(command_line)
	try:
		P = subprocess.Popen(args)
		p.wait()
	except IOError, e:
		print e

if __name__ == '__main__':
	if len(sys.argv) < 2:
    		print '请输入运行参数'
    		sys.exit()

	if sys.argv[1].startswith('--'):
   		option = sys.argv[1][2:]
    		if  option == 'version':
     			print 'Version 1.0'
   		elif option == 'help':
     			print '''
           
			@author：Gaga.yan 
			
			           自动化部署银监会测试环境
			
			usage:
			**********************************************
			*执行远程拷贝：	
			* python %s copytoserver  
			*
			*修改数据库
			* python %s changeDB 
			*
			*tomcat服务管理
			* python %s manger_tomcat start|stop|restart  
			*
			**********************************************
			'''%(filename,filename,filename)
   			sys.exit()
		else:
       			print 'Unknown option.'
       		sys.exit()
	ope = sys.argv[1]
	if ope == 'copytoserver':
		copytosever()
	elif ope == 'changeDB':
		changeDB()
	elif ope == 'manger_tomcat':
		manger_tomcat()
	else:
		print 'Unknown option.'

		

	
				
