#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys, os
import subprocess
import re
import shlex
filename=sys.argv[0]
DICT= {'192.168.0.30':'/home/apache-tomcat-7.0.55',
                  '192.168.0.35':'/root/apache-tomcat-7.0.55',
                  '192.168.0.39':'/root/apache-tomIcat-7.0.55'
      }
#copytoserver执行远程拷贝

def copytosever():   #形式参数file为需要传递的文件；形式参数server为远端服务器IP；形式参数dir为tomcat服务器的目录
	line = raw_input("依次输入拷贝文件、server的IP，保存目录，名称以空格分隔:\n").split()
	command_line = ['scp',line[0],'root@'+line[1]+':'+line[2]]
	try:
		P = subprocess.Popen(command_line)
		P.wait()
	except IOError, e:
		print e

#changeDB执行sql脚本
def changeDB():
	print '#*20\n'
	sql =  raw_input("请输入你要执行的sql脚本名称:\n").split()
	cmd = ['ssh','root@'+DICT[line[1]],'mysql -uroot -p111111 <',sql[0]] 
	try:
		P = subprocess.Popen(cmd)
		P.wait()
			
	except IOError, e:
		print e
#管理远端tomcat服务器
def manger_tomcat():
	line = raw_input("请输入tomcat服务器IP地址,\n").split()
	command_line = ['ssh','root@'+line[0],DICT[line[0]]+'/bin/'+sys.argv[2]]
	try:
		P = subprocess.Popen(command_line)
		P.wait()
	except IOError, e:
		print e

if __name__ == '__main__':
	if len(sys.argv) < 2:
    		print '请输入运行参数,你可以执行python %s --help查看用法'%filename
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
			* python %s manger_tomcat startup.sh|shutdown.sh
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
		print '你可以执行python %s --help查看用法'%filename

		

	
				
