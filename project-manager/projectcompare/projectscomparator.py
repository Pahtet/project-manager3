#!python3
# -*- coding: utf-8 -*-
import os
import os.path
import codecs
from domain.fileentry import JavaFileEntry 
 
class ProjectsComparator(object):
    
    def get_diffs(self,base_project,target_project, diffs):
        base_list=os.listdir(base_project)
        for project_entry in base_list:
            base_file = base_project+project_entry
            if os.path.isfile(base_file) and project_entry.endswith(".java"):
                target_file = target_project+project_entry
                diff_entry = self.get_diff_javaentry(base_file,target_file,project_entry)
                if diff_entry != None:
                    diffs[len(diffs):] = [diff_entry]            
            elif os.path.isdir(base_project+project_entry):
                self.get_diffs(base_project+'\\'+project_entry+'\\',target_project+'\\'+project_entry+'\\',diffs)
        return diffs   
   
    def get_diff_javaentry(self,base,target,entry):
        javafile = JavaFileEntry(self.getpackage(base)+"."+self.get_classname(entry),base,'NEW')
        if os.path.exists(target):
            if not self.isequal(base,target):
                javafile.status = "MODIFIED"        
                return javafile
            return None
        return javafile

    def isequal(self,source,destination):
        if os.path.getsize(source)==os.path.getsize(destination):
                return True
        return False
                
    def getpackage(self,classfile):
        with codecs.open(classfile,"r","utf-8") as file:
            for line in file:
                packageIndex=line.find("package")
                if packageIndex !=-1:
                    packageName=line[packageIndex+len("package")+1:line.find(";")]
                    return packageName   

    
    def get_root_imports(self,javaentry,base_project,target_project,roots):
        for project_entry in os.listdir(base_project):
            if os.path.isfile(base_project+project_entry) and project_entry.endswith(".java"):
                if self.is_root(javaentry,base_project+project_entry,target_project+project_entry):
                    roots = self.update_roots(javaentry,base_project+project_entry,roots)                                       
            elif os.path.isdir(base_project+project_entry):
                self.get_root_imports(javaentry,base_project+'\\'+project_entry+'\\',target_project+'\\'+project_entry+'\\',roots)   
        return roots          

    def is_root(self,javaentry, baseclassfile,targetclassfile):
        if not os.path.exists(targetclassfile):
            return False
        if not self.isequal(baseclassfile,targetclassfile): 
            return False
        with codecs.open(baseclassfile,"r") as f:
            try:
                for line in f:         
                    if line.find(javaentry.name)!=-1:
                        return True
                    if line.find(self.get_classname(javaentry.name))!=-1:
                        return True        
            except UnicodeDecodeError as ude:
                # print("WARNING UnicodeDecodeError")
                # print(baseclassfile)
                return False    
      
    def update_roots(self,javaentry, root_file, roots):
        root_name = self.get_classname_frompath(root_file)
        for root in roots:
            if root.name == root_name:
                root.add_import(javaentry)
                return roots
        new_root = JavaFileEntry(root_name,root_file, "ROOT")          
        new_root.add_import(javaentry)
        roots.append(new_root) 
        return roots


    def get_classname(self,file):
        return file[:file.find("java")-1]

    def get_classname_frompath(self,path):
        package = self.getpackage(path)
        file_name = os.path.split(path)[1]
        return package +'.'+ file_name[:file_name.find("java")-1]


if __name__=="__main__":

    asmspath = 'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\RHQ460'
    rhq46path = 'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\RHQ_4_6_0'
    rhq49path = 'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\RHQ_4_9_0'
    alertmodule = "modules\\enterprise\\server\\jar\\src\\main\\java\\org\\rhq\enterprise\\server\\alert\\"
    comparator = ProjectsComparator()
    diffs = []
    #comparator.get_diffs(asmspath+'\\'+alertmodule+'\\' , rhq46path+'\\'+alertmodule+'\\' , diffs)
    entry = JavaFileEntry("test","test", "test")
    diffs.append(entry)
	

