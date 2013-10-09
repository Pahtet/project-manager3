#!python3 
# -*- coding: utf-8 -*-

class GenericFileEntry:

	def __init__(self, name, path, status):
		self.__name = name
		self.__path = path
		self.__status = status
	
	@property
	def name(self):
		return self.__name
		
	@property
	def path(self):
		return self.__path
			
	@property 
	def status(self):	
		return self.__status
		
	@status.setter
	def status(self, new_status):
		self.__status = new_status
			
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
		
		
		