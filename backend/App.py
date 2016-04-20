import tornado.ioloop
import tornado.web
from WebSocket import Story

if __name__ == "__main__":
    app = tornado.web.Application([
        ("/ws/story", Story),
    ])
    app.listen(6626)
    print("Ready to work!")
    tornado.ioloop.IOLoop.current().start()