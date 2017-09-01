# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:37:11 2017

@author: harsh.arora
"""

import os, zipfile
import pandas as pd
from pathlib import Path

dir_name = 'C:\Users\harsh.arora\Videos\server'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file


for item in os.listdir(dir_name):
#    print(item)
    for item in os.listdir(dir_name+'\\'+item):
#       print (item)
#       file_path = dir_name+'\\'+item
#        print file_path
#        path_list = file_path.split(os.sep)
#        print path_list
        new = item.split('_')
#        print new
        for item in new:
            x=new[3]
#            print x
            y=x.split('.')
#            print y
            z=y[0]
#            print z
            
alist = [];
for item1 in os.listdir(dir_name):
    #print item1
    for item in os.listdir(dir_name+'\\'+item1):
       # print item
        file_path = dir_name +'\\'+ item1+'\\'+item
       # print file_path
        alist.append(file_path)
        
for i in range(0,len(alist)):
    a = repr(alist[i]);
    a = a.replace('\'','')
    print(a)
       # my_file = Path(repr(alist[i]))
       # if my_file.exists():
        #    print("true")
    price=pd.read_csv(a)
    price.insert(0,'imei',z)
#    print (price)
    price.to_csv(a)
        
        
        
            

           