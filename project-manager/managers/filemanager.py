#!python3
# -*- coding: utf-8 -*-
import os
import os.path


class FileManager:

	def copyfile(source,destination):
		pass
	
	def writetoxmlfile(self,path,content):
		file_object = open(path,'w+')
		file_object.write(content)
		file_object.close()
