#coding=utf-8
__author__='silver'
from controller.base import BaseHandler
from util.filemanager import getdocumentdetail
from util.filemanager import getdocumentlist
from util.mdparser import article
import tornado.web

class IndexPage(BaseHandler):
    def get(self, *args, **kwargs):
        self.redirect('/list.aspx')

    def post(self):
        self.get()

class SpecialPageListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        special_page_root_dir=self.opts.document_location+"/pages/"
        try:
            lst=getdocumentlist(special_page_root_dir, recursive=False)
            if len(lst)==0:
                raise FileNotFoundError
        except FileNotFoundError:
            raise tornado.web.HTTPError(404, reason='No special pages.')
        for i in range(len(lst)):
            lst[i].update(article(lst[i]['path']).extract())
        lst.sort(key=lambda i:i['title'])
        self.render('list.htm', pagetitle="Some lonely pages.", articleInfo=lst, pagenum=1, max_page=1)

    def post(self):
        self.get()

class SpecialPageHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.redirect('/list.aspx')

    def post(self):
        self.get()