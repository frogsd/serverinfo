#!/usr/bin/python
#######################
# -*- coding: utf-8 -*-
#######################


import time
import random
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib, sys
from wsgiref.handlers import SimpleHandler

# colour 
G = "\033[32m"; O = "\033[33m"; B = "\033[36m"; R = "\033[31m"; W = "\033[0m"; P = "\033[35m";

print O+("")
mess = """
                 _    _       _    _          _     _         _  
                ( )  ( )     ( )  ( )        ( )   ( )       ( ) 
 _ _ _  ___  __ | | _| | ___ | |_ | | ___  __| | _ | |_  ___ | | 
( V V )( o )( _)( )/ o )(___)( o \( )( o )/ /( _'( ( _ )( o )( _)
 \_^_/  \_/ /_\ /_\\___\     /___//_\/_^_\\_\/_\\_|/_\||/_^_\/_\ 
                                     
                                                         """

print mess
print "                full info your device by TEAM-Z3RODAY"
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik('&_<You can visit our site.......https://hackwapi.com\n ')
mengetik('&_<this script full info your device beacuse it run localhost like them server ')



__version__ = "0.1"
__all__ = ['WSGIServer', 'WSGIRequestHandler', 'demo_app', 'make_server']


server_version = "WSGIServer/" + __version__
sys_version = "Python/" + sys.version.split()[0]
software_version = server_version + ' ' + sys_version


class ServerHandler(SimpleHandler):

    server_software = software_version

    def close(self):
        try:
            self.request_handler.log_request(
                self.status.split(' ',1)[0], self.bytes_sent
            )
        finally:
            SimpleHandler.close(self)



class WSGIServer(HTTPServer):

    """BaseHTTPServer that implements the Python WSGI protocol"""

    application = None

    def server_bind(self):
        """Override server_bind to store the server name."""
        HTTPServer.server_bind(self)
        self.setup_environ()

    def setup_environ(self):

        env = self.base_environ = {}
        env['SERVER_NAME'] = self.server_name
        env['GATEWAY_INTERFACE'] = 'CGI/1.1'
        env['SERVER_PORT'] = str(self.server_port)
        env['REMOTE_HOST']=''
        env['CONTENT_LENGTH']=''
        env['SCRIPT_NAME'] = ''

    def get_app(self):
        return self.application

    def set_app(self,application):
        self.application = application



class WSGIRequestHandler(BaseHTTPRequestHandler):

    server_version = "WSGIServer/" + __version__

    def get_environ(self):
        env = self.server.base_environ.copy()
        env['SERVER_PROTOCOL'] = self.request_version
        env['REQUEST_METHOD'] = self.command
        if '?' in self.path:
            path,query = self.path.split('?',1)
        else:
            path,query = self.path,''

        env['PATH_INFO'] = urllib.unquote(path)
        env['QUERY_STRING'] = query

        host = self.address_string()
        if host != self.client_address[0]:
            env['REMOTE_HOST'] = host
        env['REMOTE_ADDR'] = self.client_address[0]

        if self.headers.typeheader is None:
            env['CONTENT_TYPE'] = self.headers.type
        else:
            env['CONTENT_TYPE'] = self.headers.typeheader

        length = self.headers.getheader('content-length')
        if length:
            env['CONTENT_LENGTH'] = length

        for h in self.headers.headers:
            k,v = h.split(':',1)
            k=k.replace('-','_').upper(); v=v.strip()
            if k in env:
                continue                    
            if 'HTTP_'+k in env:
                env['HTTP_'+k] += ','+v    
            else:
                env['HTTP_'+k] = v
        return env

    def get_stderr(self):
        return sys.stderr

    def handle(self):
        """Handle a single HTTP request"""

        self.raw_requestline = self.rfile.readline()
        if not self.parse_request(): 
            return

        handler = ServerHandler(
            self.rfile, self.wfile, self.get_stderr(), self.get_environ()
        )
        handler.request_handler = self     
        handler.run(self.server.get_app())



def demo_app(environ,start_response):
    from StringIO import StringIO
    stdout = StringIO()
    print >>stdout, "welcome full  Information in your device  "
    print >>stdout
    h = environ.items(); h.sort()
    for k,v in h:
        print >>stdout, k,'=', repr(v)
    start_response("200 OK", [('Content-Type','text/plain')])
    return [stdout.getvalue()]


def make_server(
    host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler
):
    """Create a new WSGI server listening on `host` and `port` for `app`"""
    server = server_class((host, port), handler_class)
    server.set_app(app)
    return server


if __name__ == '__main__':
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    import webbrowser
    webbrowser.open('http://localhost:8000/Team-Z3roday')
    httpd.handle_request() 
    httpd.server_close()
