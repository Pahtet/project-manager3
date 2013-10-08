#!python3
# -*- coding: utf-8 -*-
import os
import os.path
import shutil

class FileManager:

	def copyfile(source,destination):
		shutil.copyfile(source,destination)
	
	def writetoxmlfile(self,path,content):
		file_object = open(path,'w+')
		file_object.write(content)
		file_object.close()
