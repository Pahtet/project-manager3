#!python3 
# -*- coding: utf-8 -*-

import os
import subprocess

class CmdLineExecutor(object):
	def __init__(self):
		self.__kdiff_path=os.environ.get('KDIFF3_HOME')+"\\kdiff3.exe"

	def execute(self,command):
		print(command)
		returncode=subprocess.call(command.split(),shell = True)
		#print(returncode)
	def merge(self,file1,file2,file3):
		self.execute(self.__kdiff_path+" "+file1+" "+file2+" "+file3+" -m -o "+file3+" --auto")
