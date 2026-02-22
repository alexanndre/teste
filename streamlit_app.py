from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>Hello, World!</h1>")

if __name__ == "__main__":
    server_address = ("", 8000)  # porta 8000
    httpd = HTTPServer(server_address, HelloHandler)
    print("Servidor rodando em http://localhost:8000")
    httpd.serve_forever()
