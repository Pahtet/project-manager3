#!python3
# -*- coding: utf-8 -*-

from managers.cliexecutor import  CmdLineExecutor 

class SystemVarsManager(object):
	def __init__(self):
		self.__cmdexecutor
	
	def setvar(self, varname, varvalue):
		#self.__cmdexecutor("D:\\",'set '+ varname + '' + varvalue)	
		pass
		
	def unset(self, varname):
		pass

if __name__=="__main__":		
	print("here")	