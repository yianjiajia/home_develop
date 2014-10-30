#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import subprocess
import re
import shlex
import time
filename = sys.argv[0]
ABSDIR = os.path.abspath(os.path.dirname(__file__))
DICT = {'192.168.0.30': '/home/apache-tomcat-7.0.55',
        '192.168.0.35': '/root/apache-tomcat-7.0.55',
        '192.168.0.39': '/root/apache-tomcat-7.0.55'
        }
# copytoserver执行远程拷贝,将sql文件拷贝至35的/root/test目录并执行、war文件拷贝至DICT字典所指定的目录，
def copytoserver():
    filelist = [i for i in os.listdir(ABSDIR) if i.endswith('sql') or i.endswith('war')]
    try:
        for s in filelist:
            if s.endswith('war'):
                for k, v in DICT.items():
                    print "\n\n拷贝%s到%s的%s/webapps/目录......"%(s,k,v)
		    command_line1 = ['ssh', 'root@'+k, 'rm -rf ', v+'/webapps'+'/bankriskcontrol' ]
                    command_line2 = ['scp', s, 'root@'+k+':'+v]
                    p1 = subprocess.Popen(command_line1)
                    p1.wait()
                    p2 = subprocess.Popen(command_line2)
                    p2.wait()
		    print "\n\n"
            else:
                print "\n\n拷贝%s到192.168.0.35的/root/test目录......"%s
		command_line3 = ['scp', s, 'root@192.168.0.35:/root/test']
                p3 = subprocess.Popen(command_line3)
                p3.wait()
    except IOError, e:
        print e


#changeDB执行sql脚本
def changedb():
    sql = ['create_database.sql', 'init_database_data.sql', 'addtestdata.sql']
#    path = '/usr/local/mysql/bin/'
    try:
        print "\n\n创建数据库......\n\n"
	cmd1 = ['ssh', 'root@192.168.0.35', 'mysql', '-uroot', '-p111111', '<', '/root/test/'+sql[0]]
	p1 = subprocess.Popen(cmd1)
        p1.wait()
	print "\n\n初始化数据库......\n\n"
	cmd2 = ['ssh', 'root@192.168.0.35', 'mysql', '-uroot', '-p111111', '-Dbank_risk_control', '<', '/root/test/'+sql[1]]
        p2 = subprocess.Popen(cmd2)
        p2.wait()
	print "\n\n添加测试数据......\n\n"
	cmd3 = ['ssh', 'root@192.168.0.35', 'mysql', '-uroot', '-p111111', '-Dbank_risk_control', '<', '/root/test/'+sql[2]]
        p3 = subprocess.Popen(cmd3)
        p3.wait()
	
    except IOError, e:
        print e


#管理远端tomcat服务器
def restart_tomcat():
    try:
        for k, v in DICT.items():
            command_line4 = ['ssh', 'root@'+k, v+'/bin/shutdown.sh']
            command_line5 = ['ssh', 'root@'+k, v+'/bin/startup.sh']
            print "\n\n%s的tomcat服务正在重启.........\n\n"%k
            p1 = subprocess.Popen(command_line4)
            p1.wait()
            p2 = subprocess.Popen(command_line5)
            p2.wait()
	    print "\n\n============================================="
    except IOError, e:
        print e

if __name__ == '__main__':
    print '\033[1;31;40m'
    print '*'*40, '\n'
    copytoserver()
    print '\033[1;31;40m'
    print '*'*40, '\n'
    changedb()
    print '\033[1;31;40m'
    print '*'*40, '\n'
    restart_tomcat()
