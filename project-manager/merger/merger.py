#!python3 
# -*- coding: utf-8 -*-

from managers.filemanager import FileManager
from managers.cliexecutor import CmdLineExecutor
from domain.fileentry import JavaFileEntry 

class ProjectsMerger:
	cli_executor = CmdLineExecutor()
	file_manager = FileManager()
	
	def __init__(self,target_project):
		self.__target_project = target_project

	def merge_javaentry(self,java_entry,target_project):
		for entry in java_entry.child_imports:
			if entry.status == "NEW":
				self.merge_new_javaentry(entry)			
			if entry.status == "MODIFIED" :
				self.merge_modified_java_entry(entry)

	def merge_new_javaentry(java_entry):
		pass

	def merge_modified_java_entry(self,java_entry):
		#merge_command = get_
		file2=self.__target_project+java_entry.path_from_project+"\\"+java_entry.path[java_entry.path.rfind('\\')+1:]
		cmd="C:\\KDiff3\\kdiff3.exe "+java_entry.path+" "+file2+" -m -o "+file2+" --auto"
		print("merge_modified_java_entry")
		print(cmd)
		ProjectsMerger.cli_executor.execute(cmd)


	def get_merge_cmd_line(java_entry):
		pass
