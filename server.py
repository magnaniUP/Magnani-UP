import http.server
import socket
import socketserver
import os

PORT = 8080
DIRECTORY = '/home/tiagobarreto/Downloads/magnani'

socketserver.TCPServer.allow_reuse_address = True

class DualStackServer(http.server.HTTPServer):
    address_family = socket.AF_INET6
    allow_reuse_address = True
    def server_bind(self):
        try:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        except (AttributeError, OSError):
            pass
        super().server_bind()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    try:
        # Try dual-stack IPv6 (which also listens on IPv4)
        server = DualStackServer(('::', PORT), CustomHandler)
        print(f'Serving DualStack (IPv4 + IPv6) on port {PORT}...')
    except Exception as e:
        print(f'DualStack failed ({e}), falling back to IPv4 0.0.0.0...')
        server = http.server.HTTPServer(('0.0.0.0', PORT), CustomHandler)
        print(f'Serving IPv4 on port {PORT}...')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
