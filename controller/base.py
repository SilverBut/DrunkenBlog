#coding=utf-8
__author__='silver'
import tornado.web, json, yaml, os, time, re
from tornado import gen

class BaseHandler(tornado.web.RequestHandler):
    def redirect(self, url, permanent=False, status=None):
        super(BaseHandler, self).redirect(url, permanent, status)
        raise tornado.web.Finish()

    def custom_error(self, info, **kwargs):
        if not self._finished:
            status_code = kwargs.get("status_code", 500)
            self.set_status(status_code)
            error_title = kwargs.get("title", "Error")
            error_status = kwargs.get("status", "Error raised by ASP.net:")
            self.write(error_title+error_status+str(status_code))
        raise tornado.web.Finish()

class NotFoundHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.custom_error("File Not Found", status_code = 404)

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)