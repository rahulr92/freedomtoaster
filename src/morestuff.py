import os
import re
from xml.dom.ext.reader import Sax2
from xml.dom.NodeFilter import NodeFilter
from xml.dom import minidom, Node
import sqlite3 as sqlite
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
    con=sqlite.connect('test.db')
    filelist = os.listdir(MORESTUFF)
    filelist.sort()
    print filelist
    # for every file in the directory
    for filename in filelist:
	 iso=Iso()
         image_name=re.split('-|_|[0-9]*',filename,1)[0]+'.png'
         desc_file_name=re.split('-|_|[0-9]*',filename,1)[0]+'.txt'
         #print image_name,desc_file_name
         with con:
	   cur=con.cursor()
	   cur.execute("CREATE TABLE IF NOT EXISTS filelist(name VARCHAR primary key,image VARCHAR,description VARCHAR)")
	   cur.execute("INSERT OR IGNORE INTO filelist values('"+filename+"','"+image_name+"','"+desc_file_name+"')")
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
    print isoList     
    return isoList

def retnumisos():
           return numIsos
