#!python3 
# -*- coding: utf-8 -*-

from managers.filemanager import FileManager
from managers.cliexecutor import CmdLineExecutor
from domain.fileentry import JavaFileEntry 
import datetime

class ProjectsMerger:
	cli_executor = CmdLineExecutor()
	file_manager = FileManager()
	
	def __init__(self,target_project,logs_path):
		self.__target_project = target_project
		now=datetime.datetime.now()
		logfilename="merge_%d_%d_%d_%d_%d_%d.log"%(now.year,now.month,now.day,now.hour,now.minute,now.second)
		self.__log_file=open(logs_path+logfilename,"a")

	def __del__(self):
		self.__log_file.close()

	def close_log(self):
		self.__log_file.close()

	def merge_javaentry(self,java_entry,target_project):
		for entry in java_entry.child_imports:
			if entry.status == "NEW":
				self.merge_new_javaentry(entry)			
			if entry.status == "MODIFIED" :
				self.merge_modified_java_entry(entry)

	def merge_new_javaentry(self,java_entry):
		self.__log_file.write("+ "+java_entry.name+'\n')
		file_manager.copyfile(java_entry.path,self.get_file_name_in_target_project(java_entry))

	def merge_modified_java_entry(self,java_entry):
		self.__log_file.write("m "+java_entry.name+'\n')
		file2=self.get_file_name_in_target_project(java_entry)
		ProjectsMerger.cli_executor.merge(java_entry.path,file2,file2)

	def get_file_name_in_target_project(self,java_entry):
		return self.__target_project+java_entry.path_from_project+"\\"+java_entry.path[java_entry.path.rfind('\\')+1:]
	def get_merge_cmd_line(java_entry):
		pass
