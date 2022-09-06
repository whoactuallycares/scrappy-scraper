from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from dbConnector import *
import os

HOST = "0.0.0.0"
PORT = 8080
DB_CONN = db_connect()

class SimpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        # Change file to index.html if no file is specified
        if path[-1] == "/":
            path += "index.html"

        path = "/var/www" + path

        # Check if file exists, return 404 if it doesn't
        if not os.path.exists(path):
            SimpleHTTPRequestHandler.send_error(self, 404, "File not found")
            return

        self.send_response(200)

        # Check file type and set it's corresponding header
        fileType = path[::-1].split(".")[0][::-1]
        if fileType == "js":
            self.send_header("Content-type", "application/javascript; charset=utf-8")
            pass
        elif fileType == "css":
            self.send_header("Content-type", "text/css; charset=utf-8")
            pass
        elif fileType == "html":
            self.send_header("Content-type", "text/html; charset=utf-8")
            pass
        self.end_headers()

        # Return file
        with open(path) as index:
            self.wfile.write(bytes(index.read(), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        # Check reuqest
        if self.path != "/listings":
            return



        # Read data from database and send it as json
        listings = db_read(DB_CONN)
        data = []
        for listing in listings:
            data += [{
                     "id" : listing[0],
                     "name" : listing[1].replace(u'\xa0', u' '), # Fixes weird formatting issues
                     "price" : listing[2],
                     "location" : listing[3],
                     "image_urls" : listing[4].split(";")
                     }]

        self.wfile.write(bytes(str(data).replace("'", '"'), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((HOST, PORT), SimpleServer)
    print(f"Server started http://{HOST}:{PORT}ab")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")