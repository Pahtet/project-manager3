#!python3 
# -*- coding: utf-8 -*-

import os
import subprocess

class CmdLineExecutor(object):
	def __init__(self):
		pass

	def execute(self,command):
		#os.chdir(path)
		subprocess.call(command.split(),shell = True)
 
