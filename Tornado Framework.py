import tornado.ioloop
import tornado.web
class ApplicationHandler(tornado.web.RequestHandler):
    def get(self):
        self.message = message = """<html> 
<head> 
<title>Tornado Framework</title> 

</head> 
<body 
<h2>Welcome to the Tornado framework</h2> 
</body> 
</html>"""
        self.write(message)
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", ApplicationHandler),
    ])
    application.listen(5001)
    tornado.ioloop.IOLoop.instance().start()