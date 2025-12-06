#!/usr/bin/python3
"""
A simple HTTP server using Python's http.server module.
Serves different responses based on endpoints:
- /          -> Plain text greeting
- /data      -> JSON data
- /status    -> API status
- anything else -> 404 Not Found
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define the request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            # Root endpoint: simple text
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == "/data":
            # JSON data endpoint
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        
        elif self.path == "/status":
            # Status endpoint
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            # Undefined endpoint
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# Start the server
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
