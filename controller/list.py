#coding=utf-8
__author__='silver'
from controller.base import BaseHandler
from util.filemanager import getdocumentdetail
from util.filemanager import getdocumentlist
from util.mdparser import article
import tornado.web

class PageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pagenum=int(args[0])
        if pagenum<1:
            raise tornado.web.HTTPError(403)
        rootdir=self.opts.document_location
        lst=getdocumentlist(rootdir, recursive=False)
        # calc out the size
        pagecount=10
        totalcount=len(lst)
        max_page=int(totalcount/pagecount+int((totalcount%pagecount)!=0))
        if pagenum>max_page:
            pagenum=max_page
        # sort and find out the list
        # sort: the older should at the top of the list. sort by t_modify of FS
        lst.sort(key=lambda i:int(i['t_modify']), reverse=True)
        lst=lst[(pagenum-1)*pagecount:pagenum*pagecount]
        #fetch info
        for i in range(len(lst)):
            lst[i].update(article(lst[i]['path']).extract())

        self.render('list.htm', articleInfo=lst, pagenum=pagenum, max_page=max_page)

    def post(self):
        self.get()

class FirstPageHandler(PageHandler):
    def get(self):
        super(FirstPageHandler, self).get(1)