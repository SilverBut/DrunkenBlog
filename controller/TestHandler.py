#coding=utf-8
__author__='silver'
from controller.base import BaseHandler

class TestHandler(BaseHandler):
    def get(self):
        self.write('Hello World!')

    def post(self):
        self.get()