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
    
    filelist = os.listdir(ISOPATH)
    filelist.sort()
   
    # for every file in the directory
    for filename in filelist:
	 iso=Iso()
         image_name=re.split('-|_|[0-9]*',filename,1)[0]+'.png'		#if iso is ubuntu_13.04_i386, the image_name will be ubuntu.png
         desc_file_name=re.split('-|_|[0-9]*',filename,1)[0]+'.txt'	#desc_file_name is the txt file that contains the decription. ubuntu.txt, for example
	 iso.displayname=filename
	 iso.category='noidea'						#seriously, I have no idea what's a category
	 iso.description=filename					#Ths is not really a description. Its a SHORT description. Filename would suffice. Will change the variable name to something more sensible next time
	 desc_file_path=HOMEDIR+'/src/text/'+desc_file_name		#the path to desc_file_name
	 try:		#Default text should be loaded in case a matching text file is not present
	    desc_file=open(desc_file_path)
	 except:
	    desc_file=open(HOMEDIR+'/src/text/default.txt')
	 iso.longdescription=desc_file.readlines()		#This is description that will be displayed. Reading the lines from the txt file
         iso.picture=ISOIMAGEPATH+image_name
         iso.filename=filename
         iso.type='DVD'						#Who uses CD these days? Let everything go to a DVD!
         isoList.append(iso)
            
           
    return isoList

def retnumisos():
           return numIsos