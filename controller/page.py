#coding=utf-8
__author__='silver'
from controller.base import BaseHandler

class IndexPage(BaseHandler):
    def get(self, *args, **kwargs):
        self.redirect('/list.aspx')

    def post(self):
        self.get()
