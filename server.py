from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
from 


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')


def mainm():
    httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   keyfile='',
                                   certfile='',
                                   server_side=True)

    httpd.serve_forever()


if __name__ == '__main__':
    main()
