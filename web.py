from http.server import HTTPServer, BaseHTTPRequestHandler	
content = """	
<!DOCTYPE html>
<html>
<head>
    <title>HTTP Protocol</title>
</head>
<body>
    <h1>HTTP Protocol</h1>
    <p>HTTP stands for Hypertext Transfer Protocol.</p>
    <p>It transfers web pages over the internet.</p>
    <p>The client sends a request to the server.</p>
    <p>The server sends a response to the client.</p>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):	
    def do_GET(self):	
        print("request received")	
        self.send_response(200)	
        self.send_header('content-type', 'text/html; charset=utf-8')	
        self.end_headers()	
        self.wfile.write(content.encode())	
server_address = ('',880)	
httpd = HTTPServer(server_address,myhandler)	
print("my webserver is running...")	
httpd.serve_forever()	