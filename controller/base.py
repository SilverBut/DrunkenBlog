#coding=utf-8
__author__='silver'
import tornado.web, json, time, re
from random import choice as randchoice
import tornado.options
from tornado import gen
from os import stat as filestat

def error_process(obj, status_code, **kwargs):
    msgtext=str((kwargs['exc_info'][1]))
    if obj.settings.get("serve_traceback") and "exc_info" in kwargs:
        # in debug mode, try to send a traceback
        import traceback
        for line in traceback.format_exception(*kwargs["exc_info"]):
            obj.write(line)
    obj.set_status(status_code)
    obj.render("err.html", code=status_code, \
                            text=msgtext,\
                            domain=obj.opts.domain,\
                            port=obj.opts.port,\
                            path=obj.request.uri
                            )

MOTTO_TEXT = open('motto.txt', 'r', encoding='utf-8').readlines()
MOTTO_CHANGE = filestat('motto.txt').st_mtime
def getrandmotto():
	global MOTTO_TEXT
	global MOTTO_CHANGE
	if not MOTTO_CHANGE == filestat('motto.txt').st_mtime:
		MOTTO_TEXT = open('motto.txt', 'r', encoding='utf-8').readlines()
		MOTTO_CHANGE = filestat('motto.txt').st_mtime
	return randchoice(MOTTO_TEXT)

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.opts=tornado.options.options
        super(BaseHandler, self).__init__(*args, **kwargs)
    def write_error(self, status_code, **kwargs):
        error_process(self, status_code, **kwargs)
    def render(self, template_name, comment=False, *args, **kwargs):  \
        # logic procedure: 
        #   Global switch has most priority
        #   Article option will be treated if defined
        #   When it is undefined, partial switch will came to effort
        #   that means:
        #
        #   Global  |           0           |      1(Default)       |
        #   Section | 0(Default)|     1     |     0     |     1     |
        #   Article | 0 | 1 | U | 0 | 1 | U | 0 | 1 | U | 0 | 1 | U |
        #   Result  |           0           | 0 | 1 | 0 | 0 | 1 | 1 |       
        motto_single=getrandmotto()
        comment=self.opts.comment and kwargs.get('articleInfo', {}).get('comment', comment)
        if comment:     
            commentinfo={'url':'','identifier':'','jsaddr':''}
            commentinfo['url']="//"+self.opts.domain+self.request.uri
            commentinfo['identifier']=self.request.uri
            commentinfo['jsaddr'] = self.opts.comment_js
            super(BaseHandler, self).render(template_name, commentinfo=commentinfo, motto_text=motto_single, *args, **kwargs)
        else:
            super(BaseHandler, self).render(template_name, motto_text=motto_single, *args, **kwargs)

class NotFoundHandler(BaseHandler):
    def get(self, *args, **kwargs):
        raise tornado.web.HTTPError(504)

    def post(self, *args, **kwargs):
        self.get(*args, **kwargs)

class StaticBaseHandler(tornado.web.StaticFileHandler, BaseHandler):
    def write_error(self, status_code, **kwargs):
        error_process(self, status_code, **kwargs)
