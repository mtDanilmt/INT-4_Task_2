from http.server import BaseHTTPRequestHandler, HTTPServer


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"200 OK")
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=HealthCheckHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print("Starting HTTP server on port 8080")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
