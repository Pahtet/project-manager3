#!python3 
# -*- coding: utf-8 -*-

from managers.filemanager import FileManager
from managers.cliexecutor import CmdLineExecutor
from domain.fileentry import JavaFileEntry
import os.path
import datetime

class ProjectsMerger:
	keys=["RHQ460","RHQ490","rhq-RHQ_4_6_0"]
	cli_executor = CmdLineExecutor()
	file_manager = FileManager()
	
	def __init__(self,base_project,target_project,logs_path):
		self.__base_project=base_project
		self.__target_project = target_project
		now=datetime.datetime.now()
		logfilename="merge_%d_%d_%d_%d_%d_%d.log"%(now.year,now.month,now.day,now.hour,now.minute,now.second)
		self.__log_file=open(logs_path+logfilename,"a")

	def __del__(self):
		self.__log_file.close()

	def close_log(self):
		self.__log_file.close()

	def merge_javaentry(self,java_entry):
		for entry in java_entry.child_imports:
			if entry.status == "NEW":
				self.merge_new_javaentry(entry)			
			if entry.status == "MODIFIED" :
				self.merge_modified_java_entry(entry)
			entry.status = "MERGED"

	def merge_new_javaentry(self,java_entry):
		file_in_target=self.__get_base_path(self.__target_project)+self.__get_paths(java_entry.path)[1]
		if os.path.isfile(file_in_target):
			return
		self.__log_file.write("+ "+java_entry.name+'\n')
		ProjectsMerger.file_manager.copyfile(java_entry.path,file_in_target)
		ProjectsMerger.cli_executor.git_add(file_in_target)
		ProjectsMerger.cli_executor.git_commit(java_entry.name)

	def merge_modified_java_entry(self,java_entry):
		self.__log_file.write("m "+java_entry.name+'\n')
		file_in_base=self.__get_base_path(self.__base_project)+self.__get_paths(java_entry.path)[1]
		file_in_target=self.__get_base_path(self.__target_project)+self.__get_paths(java_entry.path)[1]
		ProjectsMerger.cli_executor.merge(file_in_base,java_entry.path,file_in_target)
		ProjectsMerger.cli_executor.git_commit(java_entry.name)
		
	def get_merge_cmd_line(java_entry):
		pass

	def __get_base_path(self,dir):
		for key in self.keys:
                	paths = self.__split_path(dir,key)
                	if len(paths)==2:
                		return paths[0]+key+"\\"
	def __get_paths(self, current_file):
                for key in self.keys:
                	paths = self.__split_path(current_file,key)
                	if len(paths)==2:
                		return paths[0],paths[1]

	def __split_path(self,path,key):
		return path.split(key)
