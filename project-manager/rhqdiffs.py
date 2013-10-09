#!python3 
# -*- coding: utf-8 -*-

from projectcompare.projectscomparator import ProjectsComparator
from domain.fileentry import JavaFileEntry
from managers.filemanager import FileManager
from merger.merger import ProjectsMerger

xmldir = 'D:\\merge-analysis\\'
asmspath = "D:\\GitHub\\atlas\\kcc_appserver_ms\\RHQ460\\modules\\core\\client-api\\"
rhq46path = "D:\\GitHub\\atlas\\kcc_appserver_ms\\rhq-RHQ_4_6_0\\modules\\core\\client-api\\"
rhq49path =  "D:\\GitHub\\atlas\\kcc_appserver_ms\\RHQ490\\modules\\core\\client-api\\"
logs_path = "D:\\merge-analysis\\logs\\"

inPath=asmspath 
outPath=rhq49path

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
	merge=ProjectsMerger(rhq46path,outPath,logs_path)
	diffs = []
	roots = []
	diffs = comparator.get_diffs(inPath,outPath, diffs)
	modified = get_modified(diffs)

	print(len(diffs)) 
	print("diffs founded\n")
	
	print(len(modified)) 
	print("modified diffs founded\n")	
		
	for mod in modified: 
		roots = comparator.get_root_imports(mod,inPath,outPath,roots)
	
	for root in roots:
		file_manager.writetoxmlfile(xmldir+root.name+'.xml', root.xmlprint('<?xml version="1.0"?>\n'))
	print(len(roots))
	root = roots[0]
	merge.merge_javaentry(root,rhq49path)
