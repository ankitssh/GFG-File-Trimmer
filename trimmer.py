# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:04:34 2020

@author: Ankit Sharma
"""

import os,re

files=[]
directoryContents = os.listdir("./")

for x in directoryContents:
    if re.search("\w+WithMarker.*",x):
        files.append(x)


for x in files:
    reader=open("./"+x,"r+")
    text=reader.read().strip()
    reader.seek(0)
    reader.write(text)
    reader.close()
    
print("Success")
    
    
    
    
        

