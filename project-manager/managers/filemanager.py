#!python3
# -*- coding: utf-8 -*-
import os
import os.path
import shutil

class FileManager:

	def copyfile(self,source,destination):
		folder=destination[0:destination.rfind('\\')]+"\\"
		if not os.path.exists(folder):
			print("Creating new folder "+folder)
			os.makedirs(folder)
		shutil.copyfile(source,destination)
	
	def writetoxmlfile(self,path,content):
		file_object = open(path,'w+')
		file_object.write(content)
		file_object.close()
