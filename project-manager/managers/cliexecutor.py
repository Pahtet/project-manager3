#!python3 
# -*- coding: utf-8 -*-

import os
import subprocess

class CmdLineExecutor(object):
	git_repo="D:\\GitHub\\atlas\\"
	def __init__(self):
		self.__kdiff_path=os.environ.get('KDIFF3_HOME')+"\\kdiff3.exe"
		#self.__git_path=os.environ.get('GIT_HOME')+"\\bin\\git.exe"

	def execute(self,command):
		print(command)
		os.chdir(CmdLineExecutor.git_repo)
		returncode=subprocess.call(command.split(),shell = True)
		print(returncode)
	def merge(self,file1,file2,file3):
		self.execute(self.__kdiff_path+" "+file1+" "+file2+" "+file3+" -m -o "+file3+" --auto")

	def git_add(self,file):
		self.execute("git add "+file)

	def git_commit(self,class_name):
		self.execute('git commit -a -m "'+class_name+'"')
		#self.execute("git push")