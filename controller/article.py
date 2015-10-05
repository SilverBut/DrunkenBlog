#coding=utf-8
__author__='silver'
from controller.base import BaseHandler
from util.filemanager import getdocumentdetail
from util.mdparser import article

class ArticleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        filename=args[0]
        rootdir=self.opts.document_location
        try:
            fileinfo=getdocumentdetail(rootdir+'/'+filename+'.md')
        except FileNotFoundError:
            self.custom_error(status_code=404)
        blog=article(fileinfo['path'])
        blog.render()
        self.render("article.htm", title=blog.info['title'], md_html=blog.html, articleInfo=blog.info)

    def post(self):
        self.get()