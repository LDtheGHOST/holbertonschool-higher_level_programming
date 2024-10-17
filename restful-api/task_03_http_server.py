#!/usr/bin/env python3

import json
from http.server
import BaseHTTPRequestHandler, HTTPServer
    """la je fais mes importations"""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """ je cree une classe qui prend en parametre (http.server.BaseHTTPRequestHandler)"""
    
    def do_GET(self):
        """ je cree une fonction que je defini et ou je fais une demande GEt """

        if self.path == '/':
             """je fais ma condition dans la quel je dis le cheminement"""

            self.send_response(200)
                """ je resoit une reponse 200 qui est valide """
        
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
                """ la si mon code est valide je recoit un message text hello blablabla"""
        
        elif self.path == '/data':
            """ sinon je fais un autre cheminemt qui ira ans la data"""

            self.send_response(200)
                """si c'est bon je recois 200"""
        
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
                 """si c'est valide je recois un message de ma bibiotheque json qui va me donner toute les information demander"""
        
        elif self.path == '/status':
             """ sinon je fais un autre cheminement similaire a la deuxieme condition"""

            self.send_response(200)
                """si c'est bon je recois 200"""
        
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"OK")
                 """pareil que la deuxieme condition et affichera ok"""
        
        else:
            self.send_response(404)
                """ si je reoit 404 qui et une erreur"""
        
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
                 """ et m'envoi un message Point de terminaison non trouvé"""

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()