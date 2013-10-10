import os
import re
import gtk

from globals import *

numIsos = 0
class Iso:
    def __init__(self):
        self.displayname = ''
        self.category = ''
        self.description = ''
        self.longdescription = ''
        self.picture = ''
        self.filename = ''
        self.type = ''    

def populateIsoList():
    
    
    numIsos = 0          
    isoList = []
    
    filelist = os.listdir(MORESTUFF)
    filelist.sort()
    print filelist
    # for every file in the directory
    for filename in filelist:
	 iso=Iso()			#This is almost similar to what you will find in isolist.py. If you are looking for comments, you'll find them in isolist.py
         image_name=re.split('-|_|[0-9]*',filename,1)[0]+'.png'
         desc_file_name=re.split('-|_|[0-9]*',filename,1)[0]+'.txt'
         
        
	 iso.displayname=filename
	 iso.category='noidea'
	 iso.description=filename
	 desc_file_path=HOMEDIR+'/src/text/'+desc_file_name
	 try:
	    desc_file=open(desc_file_path)
	 except:
	    desc_file=open(HOMEDIR+'/src/text/default.txt')
	 iso.longdescription=desc_file.readlines()
	 
         iso.picture=ISOIMAGEPATH+image_name
         iso.filename=filename
         iso.type='DVD'
         
         isoList.append(iso)
         
    return isoList

def retnumisos():
           return numIsos
