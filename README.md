# EX01 Developing a Simple Webserver
## Date:15-10-2026
## REG NO:26018193
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM: 
~~~
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
~~~

## OUTPUT:
![alt text](<Screenshot 2026-10-24 143554.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

