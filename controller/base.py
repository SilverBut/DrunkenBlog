#coding=utf-8
__author__='silver'
import tornado.web, json, yaml, time, re
import tornado.options
from tornado import gen

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.opts=tornado.options.options
        super(BaseHandler, self).__init__(*args, **kwargs)
    def write_error(self, status_code, **kwargs):
        self.set_status(status_code)
        self.render("err.html", code=status_code, \
                                text=str((kwargs['exc_info'][1])),\
                                domain=self.opts.domain,\
                                port=self.opts.port,\
                                path=self.request.uri
                                )

class NotFoundHandler(BaseHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(504)

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)

