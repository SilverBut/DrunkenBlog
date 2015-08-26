#!/usr/bin/python
import tornado.ioloop, tornado.web, tornado.options
import sys, os, yaml
import controller.base
import logging
from logging import *

# Log config. Try to use ./exp.py -log=DEBUG
loglevel='INFO'
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level, format='[%(asctime)s][%(levelname)s] %(message)s')

def __ReadConfigFile__():
    config_filename="config.yaml"
    conf={}
    try:
        with open(config_filename,'r') as fin:
            conf = yaml.load(fin)
    except:
        print("Has no or invaild config file. Use default value")
    conf   

# run config
setting = {
    "debug":True,
    "default_handler_class": "controller.error.Error403",
    "static_path": "static",
}
__ReadConfigFile__()

#sys config
tornado.options.define("port", default=80, help="listening port", type=int)
tornado.options.define("addr", default="127.0.0.1", help="listening address")
tornado.options.parse_command_line()

application = tornado.web.Application([
    (r"^/$", "controller.page.IndexPage"),
    (r"^/article.aspx/([\w-!():.,\[\]]+)$", "controller.article.ArticleHandler"),
    (r"^/list.aspx/*$", "controller.list.FirstPageHandler"),
    (r"^/list.aspx/(\d+)$", "controller.list.PageHandler"),
    (r"^/page.aspx/([\w-!():.,\[\]]+)$", "controller.page.SpecialPageHandler")
], **setting)




if __name__ == "__main__":
    try:
        application.listen(80)
        tornado.ioloop.IOLoop.instance().start()
    except:
        import traceback
        print(traceback.print_exc())
    finally:
        sys.exit(0)