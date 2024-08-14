import json
from http.server import BaseHTTPRequestHandler, HTTPServer

print("Hello")

#Sample Database:
books = [
    {'id': 1,'title': '1984', 'author':'Orwell'},
    {'id': 2,'title': 'To Kill a Mockingbird', 'author':'Harper Lee'},
    {'id': 3,'title': 'The Great Gatsby', 'author':'F. Scott Fitzgerald'},
]

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(books).encode())

def run(server_class = HTTPServer, handler_class = SimpleHandler, port = 8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()