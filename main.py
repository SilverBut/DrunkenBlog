#!/usr/bin/python
import tornado.ioloop, tornado.web, tornado.options
import sys, os, yaml
import controller.base
import logging
from logging import *

#Load System Config from command line and config file
tornado.options.define("port", default=80, help="listening port", type=int)
tornado.options.define("addr", default="127.0.0.1", help="listening address")
tornado.options.define("debug", default=False, help="Whether the server is "\
                        "under the debug mode. CATUION IN PRODUCTION SERVER!"
                        , type=bool)
tornado.options.define("compress_response", default=False, help="Open it if "\
                        "you want to compress the response.", type=bool)
tornado.options.define("config_file", default="config.ini", help="Define "\
                        "the config file.")
tornado.options.define("document_location", default="documents", help="Redefine"\
                        " the location of your documents. DO NOT ADD SLASHES AFTER"\
                        " YOUR LOCATION!")
tornado.options.define("domain", default="localhost", help="URL displayed")
tornado.options.parse_command_line()
try:
    a=open(tornado.options.options.config_file)
    a.close()
    tornado.options.parse_config_file(tornado.options.options.config_file)
except:
    warning("Unable to use config file. Use default settings.")

#Load settings to var
setting = {
    "debug":tornado.options.options.debug,
    "default_handler_class": controller.base.NotFoundHandler,
    "template_path": "template",
    "static_path": "static",
    "compress_response": tornado.options.options.compress_response
}

# Route config
application = tornado.web.Application([
    (r"^/$", "controller.page.IndexPage"),
    (r"^/article\.aspx/((?:[\w\-!():.,\[\]]|(?:%20))+)$", "controller.article.ArticleHandler"),
    (r"^/list\.aspx/*$", "controller.list.FirstPageHandler"),
    (r"^/list\.aspx/(\d+)$", "controller.list.PageHandler"),
 #   (r"^/page\.aspx/((?:[\w\-!():.,\[\]]|(?:%20))+)$", "controller.page.SpecialPageHandler")
    (r"^/abc/.*$", "controller.testdemo.TestHandler")
], **setting)

# Server loop
if __name__ == "__main__":
    try:
        application.listen(80)
        tornado.ioloop.IOLoop.instance().start()
    except:
        import traceback
        error(traceback.print_exc())
    finally:
        sys.exit(0)