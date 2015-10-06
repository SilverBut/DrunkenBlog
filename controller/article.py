#coding=utf-8
__author__='silver'
from controller.base import BaseHandler
from util.filemanager import getdocumentdetail
from util.mdparser import article
import tornado.web

class ArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        filename=args[0]
        rootdir=self.opts.document_location
        try:
            fileinfo=getdocumentdetail(rootdir+'/'+filename+'.md')
        except FileNotFoundError:
            raise tornado.web.HTTPError(404, reason='Non-existing article.')
        blog=article(fileinfo['path'])
        blog.render()
        self.render("article.htm", title=blog.info['title'], md_html=blog.html, articleInfo=blog.info)

    def post(self):
        self.get()