#!/usr/bin/env python

import BaseHTTPServer, CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import sys, argparse, socket
from time import sleep
 
parser = argparse.ArgumentParser(description='Happy to serve you')
parser.add_argument('--port', type=int, default=8000, help='the port number to listen to')
parser.add_argument('-t', '--notryports', default=True, action="store_false", help='if a port is busy, automatically try other ones')
parser.add_argument('--share', default=False, action="store_true", help='Run as server accessible via your local network')
args = parser.parse_args()
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]
tryports = args.notryports
port = args.port
ipaddr = None

if args.share:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("wikipedia.org",80))
    ipaddr = s.getsockname()[0]
    s.close()

while True:
    try:
        if ipaddr:
            server_address = (ipaddr, port)
            servername = ipaddr
        else:
            server_address = ("localhost", port)
            servername = "localhost"
        httpd = server(server_address, handler)
        print "Serving at --> http://{0}:{1}".format(servername, port)
        httpd.serve_forever()
    except socket.error, e:
        if e.errno == 98:
            if tryports:
                if port < 2000:
                    port = 2000
                else:
                    port += 1
                sleep(.01)
            else:
                print """
====================================
Error: port ({0}) is already in use
====================================
 
You can pick another port number
(for example 9999) with:
 
    serve --port 9999
""".format(port)
                break
        else:
            raise(e)

