#coding=utf-8
__author__='silver'
import markdown
import re
from ast import literal_eval as eval
import time
from datetime import datetime as dt
from dateutil import tz
from os.path import splitext, split
from util.filemanager import getdocumentdetail

"""
Class: util.mdparser.article
Usage: To parse or/and render a certain markdown file.
Initial Arguments:
    filepath: 
      string, MUST be provided. path to the md file, such as '~/doc/index.md'
    extracted: 
      boolean, False by default. If self.info has been filled by self.extract().
    hasmeta: 
      boolean, True by default. If the meta info is in the first comment block of text
    removemeta: 
      boolean, False by default. If the meta info should be removed in the render result
    removehead: 
      boolean, True by default. If the old headline of this article should be removed
    encoding:
      string, 'utf-8' by default. encoding of the target file
Functions:
    extract():
        Extract the metainfo from the content if possible
    render():
        Render the content and return the HTML rendered
"""


class article:
    def __init__(self,
                 filepath, 
                 extracted=False,
                 hasmeta=True,  
                 removemeta=False,
                 removehead=True,
                 encoding='utf-8', 
                 extensionlist=['markdown.extensions.toc','markdown.extensions.fenced_code','markdown.extensions.admonition','markdown.extensions.footnotes', 'markdown.extensions.tables']):
        self.extensionlist=extensionlist    
        self.info={}
        self.info.update(getdocumentdetail(filepath))
        self.info['filepath']=filepath
        self.info['encoding']=encoding
        self.info['title']=splitext(split(filepath)[1])[0]
        self.hasmeta=hasmeta
        self.extracted=extracted
        self.removemeta=removemeta
        self.removehead=removehead
        self._mdparser_metainfo_regexp=re.compile(r"<!--\s*({.*?})\s*-->", re.S)
        self._mdparser_delhead_regexp=re.compile(r"-->\s*?(<h1.*?</h1>)")
        self.html=""
        try:
            f=open(self.info['filepath'], 'r', encoding=self.info['encoding'])
            self.text=f.read()
        finally:
            f.close()

    def extract(self):
        #check
        if not self.extracted:
            self.extracted=True
            if self.hasmeta:
                groups=re.match(self._mdparser_metainfo_regexp, self.text)
                if (groups!=None):
                #Extract infos out
                    info=eval(groups.group(1))
                    self.info.update(info)
        #     # time-show strategy:
        #     # show the EARLIER time between last_update and t_modify if available
        #     # use GMT-0 when compares, and DO NOT forget to convert the last_update
        # time_to_show=self.info['t_modify']
        # if 'last_update' in self.info:
        #     ftime=time.mktime(time.strptime("+0800 - "+self.info['last_update'],  \
        #                                  r"%z - %Y/%m/%d %H:%M"))
        #     if ftime<self.info['t_modify']:
        #         time_to_show=ftime
        # #time zone convert
        # self.info['time_to_show']=time.strftime(r"%Y/%m/%d %H:%M",\
        #                                             dt.utcfromtimestamp(time_to_show).\
        #                                                 replace(tzinfo=tz.gettz('UTC')).astimezone(tz=tz.gettz('Asia/Shanghai')).\
        #                                             timetuple()
        #                                         )
        return self.info
        

    def render(self):
        if not self.extracted:
            self.extract()
        # render the markdown    
        self.html=markdown.markdown(self.text, extensions=self.extensionlist)
        # remove meta and headline if need
        # never change the order of the following code, since it is magic
        if self.removehead:
            self.html=self._mdparser_delhead_regexp.sub("-->", self.html, 1)
        if self.removemeta:
            self.html=self._mdparser_metainfo_regexp.sub(" ", self.html, 1)

if __name__=="__main__":
    t=article("test.md", removemeta=True)
    print(t.text)
    t.extract()
    print(t.info)
    t.render()
    print(t.html)