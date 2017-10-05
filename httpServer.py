from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

ADDR = "localhost"
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):        
    def do_POST(self):
        print(self.path)
        # print(self.rfile.read())
        length = int(self.headers['Content-length'])
        self.send_response(200, "OK")
        self.end_headers()
        print(self.rfile.read(length))
        self.wfile.write("serverdata")





httpd = HTTPServer((ADDR, PORT), RequestHandler)
httpd.serve_forever()