import os
import http.server
import socketserver
import urllib.request
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        msg = 'Hello! the external ip is %s' % (exteral_ip)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
