import tornado.websocket
import tornado.web

class Story(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
    	if message == "fetchOne":
    		with open("/var/log/syslog") as f:
			    lines = f.readlines()
			    last_row = lines[-1]
			    self.write_message(last_row+"\r")

    	else:
    		self.write_message("Unrecognized message: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True