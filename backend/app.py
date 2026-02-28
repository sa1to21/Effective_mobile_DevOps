from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        text = "Hello from Effective Mobile!"
        self.wfile.write(text.encode('utf-8'))

server_address = ('0.0.0.0', 8080)
httpd = HTTPServer(server_address, HttpHandler)
print('http server запущен на порту 8080')
httpd.serve_forever()