import os.path
import codecs

#Keys
javaKey=".java"
packageKey="package"
importKey="import"
fileEncoding="utf-8"
#/Keys

folder1="D:\\kcc_appserver_ms\\RHQ460\\modules\\"
folder2="D:\\rhq-RHQ_4_6_0\\modules\\"

filesToAdd=0 #Number of added files
filesToEdit=0 #Number of changed files
warningCount=0 #Number of undecoded lines 
#folder1="D:\\dev\\pytest\\1\\"
#folder2="D:\\dev\\pytest\\2\\"

def isEqual(file1,file2):
        size1=os.path.getsize(file1)
        size2=os.path.getsize(file2)
        if size1==size2:
                return True
        else:
                return False

def folderCompare(path1,path2):
        list1=os.listdir(path1)
        for file in list1:
                filename1=path1+file
                if os.path.isfile(filename1):
                        if file.endswith(javaKey):
                                package=findPackage(filename1)
                                filename2=path2+file
                                if os.path.exists(filename2):
                                        if not isEqual(filename1,filename2):
                                                print("? "+package+'.'+file)
                                                if len(package) >0:
                                                        imports=findImport(folder1,package)
                                                        if len(imports)>0:
                                                                #print("imported in")
                                                                print(imports)
                                                global filesToEdit
                                                filesToEdit=filesToEdit+1
                                else:
                                        print("+ "+package+file)
                                        global filesToAdd
                                        filesToAdd=filesToAdd+1
                if os.path.isdir(filename1):
                                file='\\'+file+'\\'
                                folderCompare(path1+file,path2+file)   
        return



def findPackage(file):
                with codecs.open(file,"r",fileEncoding) as f:
                        for line in f:
                                packageIndex=line.find(packageKey)
                                if packageIndex !=-1:
                                        packageName=line[packageIndex+len(packageKey)+1:line.find(";")]
                                        return packageName
                return "no package"


def findImport(folder,package):
        found=[]
        for file in os.listdir(folder):
                objectName=folder+file
                if os.path.isfile(objectName) and file.endswith(javaKey):
                        if isImported(objectName,package):
                                found.append(file)
                if os.path.isdir(objectName):
                        r=findImport(folder+"\\"+file+"\\",package)
                        if len(r)>0:
                                for foundFile in r:
                                        found.append(foundFile)
        return found            
                        

def isImported(file,package):
        targetString=importKey+" "+package
        with codecs.open(file,"r",fileEncoding) as f:
                try:
                        for line in f:         
                                if line.find(targetString)!=-1:
                                        return True
                except UnicodeDecodeError as ude:
                        global warningCount
                        warningCount=warningCount+1
                        #print("WARNING UnicodeDecodeError")
        return False

folderCompare(folder1,folder2)
print("End of comparation")
print("Changed %d Added %d"%(filesToEdit,filesToAdd))
print("Warnings %d"%warningCount)
