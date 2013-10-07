#!python3 
# -*- coding: utf-8 -*-

class JavaFileEntry:

	status = {'NEW' : 'new', 'MODIFIED' : 'modified' , 'MERGED': 'merged'} 		
	
	def __init__(self, name, path, status):
		self.__name = name
		self.__path = path
		self.__status = status
		self.__child_imports = [] # list of imported java classes
		self.__path_from_project=""
	
	@property	
	def path_from_project(self):
		return self.__path_from_project

	def set_path_from_project(self,path_from):
		self.__path_from_project=path_from

	@property
	def name(self):
		return self.__name
		
	@property
	def path(self):
		return self.__path
			
	@property 
	def status(self):	
		return self.__status

	@property 
	def child_imports(self):	
		return self.__child_imports	
		
	@status.setter
	def status(self, new_status):
		self.__status = new_status
		
	def add_import(self,fileentry):
		self.__child_imports.append(fileentry)
			
	def xmlprint(self,xml_tree):
		xml_tree += self.xmlprintfile()
		if len(self.__child_imports) == 0:
			xml_tree += '/>'
		else:
			xml_tree += '>\n<imports> \n' 
			for classimport in self.__child_imports:
				xml_tree = classimport.xmlprint(xml_tree)		
				xml_tree += '\n'
			xml_tree += '</imports>\n' 
			xml_tree += '</file>'
		return xml_tree
	
	def xmlprintfile(self):
		xmlstring = '<file '
		xmlstring+='name='+'\''+self.__name+'\'' + ' '
		xmlstring+='status='+'\''+self.__status+'\''+ ' '
		return xmlstring	

if __name__=="__main__":
	classfile = JavaFileEntry("Class","D:\Class","new")
	importedfile1 = JavaFileEntry("Class2","D:\Class","new")
	importedfile2 = JavaFileEntry("Class2","D:\Class","new")
	importedfile1.add_import(importedfile2)
	classfile.add_import(importedfile1)
	classfile.add_import(importedfile2)
	tree = classfile.xmlprint('') 	
	print(tree)	
		
		
		