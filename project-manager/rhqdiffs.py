#!python3 
# -*- coding: utf-8 -*-

from projectcompare.projectscomparator import ProjectsComparator
from domain.fileentry import JavaFileEntry
from managers.filemanager import FileManager
from merger.merger import ProjectsMerger

xmldir = 'D:\\merge-analysis\\'
asmspath = "D:\\kcc_appserver_ms\\RHQ460\\modules\\core\\"
rhq46path = "D:\\rhq-RHQ_4_6_0\\modules\\core\\"
rhq49path =  "D:\\rhq-RHQ_4_9_0\\modules\\core\\"
logs_path="D:\\merge-analysis\\logs\\"
kdiff_path=os.environ.get('KDIFF3_HOME')+"kdiff3.exe" 

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
	merge=ProjectsMerger(outPath,logs_path,kdiff_path)
	diffs = []
	roots = []
	diffs = comparator.get_diffs(inPath,outPath, diffs,"")
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
