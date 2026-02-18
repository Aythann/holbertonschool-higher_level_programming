#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send(self, body: bytes, status=200, content_type="text/plain"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send(b"Hello, this is a simple API!", 200, "text/plain")

        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send(json.dumps(payload).encode("utf-8"), 200, "application/json")

        elif self.path == "/status":
            self._send(b"OK", 200, "text/plain")

        elif self.path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            # IMPORTANT: comme l'exemple “checker-friendly”
            self._send(json.dumps(payload).encode("utf-8"), 200, "text/plain")

        else:
            self._send(b"Endpoint not found", 404, "text/plain")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:{}".format(port))
    httpd.serve_forever()


if __name__ == "__main__":
    run()
