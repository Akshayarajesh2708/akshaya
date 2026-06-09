from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Student Website</title>
        </head>
        <body>
            <h1>Welcome to My Python Webpage</h1>
            <p>This webpage is running using Python.</p>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

server = HTTPServer(("localhost", 8000), MyHandler)

print("Server running at http://localhost:8000")
server.serve_forever()