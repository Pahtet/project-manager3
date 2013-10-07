#!python3 
# -*- coding: utf-8 -*-

from projectcompare.projectscomparator import ProjectsComparator
from domain.fileentry import JavaFileEntry
from managers.filemanager import FileManager

xmldir = 'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\merge-analysis\\'
asmspath = 'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\RHQ460\\modules\\'
rhq46path = 'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\RHQ_4_6_0\\modules\\'
rhq49path =     'D:\\ipimenov_ASMS_V4.0.0\\kcc_appserver_ms\\RHQ_4_9_0\\modules\\'
alertmodule = "enterprise\\server\\jar\\src\\main\\java\\org\\rhq\enterprise\\server\\alert\\"


def get_new(all_diffs):
        pass

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
        diffs = comparator.get_diffs(asmspath+'\\'+alertmodule,rhq46path+'\\'+alertmodule+'\\', diffs)
        modified = get_modified(diffs)
        roots = comparator.get_root_imports(modified[1],asmspath,rhq46path,roots)
        for r in roots:
                file_manager.writetoxmlfile(xmldir+r.name+'.xml', r.xmlprint('<?xml version="1.0"?>\n')