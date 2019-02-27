import socket
#import tty
import paramiko
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop

"""REF:
tornado:
https://www.cnblogs.com/aguncn/p/5665916.html
https://github.com/huashengdun/webssh/blob/master/webssh/handler.py

django
https://blog.csdn.net/linxi7/article/details/76161584
"""

hostname = "xxx"
port = xxx
username = "xxx"
key_filename = r"xxx"

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    channel = None
    
    def open(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=port, username=username, key_filename=key_filename)
        #self.channel = ssh
        # pty
        channel = ssh.invoke_shell(term='xterm')
        self.channel = channel
        # js使用同一ws后，timeout后, 执行下一命令将继续读取，除非send ctrc
        # 故减少为2, 但仍旧卡住，需使用异步方式以判断是否结束接收
        self.channel.settimeout(2) 
        # @TODO: https://github.com/huashengdun/webssh/blob/master/webssh/worker.py
        #self.rconn.setblocking(0)

    @tornado.gen.coroutine
    def on_message(self, message):
        #self.write_message(">>> " + message)
        #stdin, stdout, stderr = self.channel.exec_command(message)
        #result = stdout.read()
        
        # ctr c
        if message == chr(3):
            self.ctr_c()
            return
        
        # clear
        
        self.channel.sendall(message + '\n')
        try:
            while True:
                result = self.channel.recv(5)
                if result:
                    yield self.write_message(result.decode('utf-8'))
                else:
                    # If a string of length zero is returned, the channel stream has closed.                    
                    break
        except socket.timeout:
            pass
    
    # this function should move out, and move use async
    def ctr_c(self):
        if self.channel and self.channel.active:
            # https://stackoverflow.com/questions/33290207/python-paramiko-send-ctrlc-to-an-ssh-shell
            self.channel.send(chr(3))

    def on_close(self):
        if not self.channel.closed:
            self.channel.close()

    def check_origin(self, origin):
        # 403
        # https://blog.csdn.net/orangleliu/article/details/42008423
        return True
    
    def on_ping(self, data):
        print('on_ping' + repr(data))

class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("websockets.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexPageHandler),
            (r'/ws', WebSocketHandler)
        ]

        settings = {
            'template_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
