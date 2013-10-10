#!python3 
# -*- coding: utf-8 -*-

from projectcompare.projectscomparator import ProjectsComparator
from domain.fileentry import JavaFileEntry
from managers.filemanager import FileManager
from merger.merger import ProjectsMerger

xmldir = 'D:\\merge-analysis\\'
asmspath = "D:\\GitHub\\atlas\\kcc_appserver_ms\\RHQ460\\modules\\core\\"
rhq46path = "D:\\GitHub\\atlas\\kcc_appserver_ms\\rhq-RHQ_4_6_0\\modules\\core\\"
rhq49path =  "D:\\GitHub\\atlas\\kcc_appserver_ms\\RHQ490\\modules\\core\\"
logs_path = "D:\\merge-analysis\\logs\\"

inPath=asmspath 
outPath=rhq46path

def get_new(all_diffs):
	new = []
	for diff in all_diffs:
		if diff.status == "NEW":
			new.append(diff)
	return new

def get_modified(all_diffs):		
	modified = []
	for diff in all_diffs:
		if diff.status == "MODIFIED":
			modified.append(diff)
	return modified

if __name__=='__main__':	
	file_manager = FileManager()
	comparator = ProjectsComparator()
	diffs = []
	roots = []
	diffs = comparator.get_diffs(True,inPath,outPath, diffs)
	print("%d diffs founded\n"%len(diffs)) 	
	modified = get_modified(diffs)
	print("%d modified diffs founded\n"%len(modified))	
	new_files=get_new(diffs)
	print("%d new files founded\n"%len(new_files))	

	for mod in modified: 
		roots = comparator.get_root_imports(mod,inPath,outPath,roots)
	
	for root in roots:
		file_manager.writetoxmlfile(xmldir+root.name+'.xml', root.xmlprint('<?xml version="1.0"?>\n'))
	print("%d roots\n"%len(roots)) 

	merge=ProjectsMerger(rhq46path,rhq49path,logs_path)
	
	new_root = JavaFileEntry("root_for_new_files","", "ROOT")          
        
	for newfile in new_files:
		new_root.add_import(newfile)

	merge.merge_javaentry(new_root)

	for root in roots:
		merge.merge_javaentry(root)
	
	merge.close_log()
