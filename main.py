#!/usr/bin/python
import tornado.ioloop
import tornado.web, tornado.options
import sys, os, yaml
import controller.base

setting = {
    "debug":True,
    "default_handler_class": controller.base.NotFoundHandler,
    "static_path": "static",
}

application = tornado.web.Application([
    (r"^/\d.*", "controller.testdemo.TestHandler")
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