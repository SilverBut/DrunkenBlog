#coding=utf-8
__author__='silver'
import os
from os.path import splitext
from os.path import isfile
from os import listdir
from os import stat
from os import stat_result
from os import walk
from os import stat_float_times
#from re import re
from datetime import datetime 
from dateutil import tz

"""

Function: util.filemanager.getdocumentlist(
                                            dir, # path to the directory
                                            recursive=True, # if it should recursive at the dir
                                            detail=True, # if need time and other detailed infos(in unix time format)
                                            )
Return Value: [{path, filename, [t_create, t_modify]},..]

"""

def getdocumentlist(path, recursive=True, detail=True):
    path=os.path.normpath(path)
    path=os.path.relpath(path)  #convert to rel path
    document_list=[]
    # have the list
    if recursive:
        for curdir, curdirlist, curfilelist in walk(path):
            for filename in curfilelist:
                    document_list.append({
                            "filename":splitext(filename)[0], 
                            "path":curdir+"/"+filename
                        })
    else:
        for filename in listdir(path):  #have a loop test
            if os.path.isfile(path+'/'+filename):
                document_list.append({
                        "filename":splitext(filename)[0], 
                        "path":path+'/'+filename          # just use relative path
                    })
    # find the detailed time if need
    if detail:
        # state save
        _stat=os.stat_float_times() 
        os.stat_float_times(False) 
        for x in range(len(document_list)):
            document_list[x].update(getdocumentdetail(document_list[x].get('path')))
        #state restore
        os.stat_float_times(_stat) 
    return document_list

def getdocumentdetail(path):
    # os.stat_float_times(False) should be executed before all calls
    m=stat(path)
    strt=datetime.fromtimestamp(m.st_mtime, tz=tz.gettz('Asia/Shanghai')).strftime(r"%Y/%m/%d %H:%M")
    print(strt)
    return {"path":path, "t_create":m.st_ctime, "t_modify":m.st_mtime, 'last_update':strt}
    # os.stat_float_times(True)  should be executed after all calls

if __name__=="__main__":
    print(getdocumentlist('.', detail=False))
    print('---')
    print(getdocumentlist('../controller'))