#!/usr/bin/python3
import http.server
import json
import socketserver
"""la je fais mes importations"""

PORT = 8000
"""je definie la valeur de port"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """ je cree une classe qui prend en parametre (http.server.BaseHTTPRequestHandler)"""


    def do_GET(self):
        """ je cree une fonction que je defini et ou je fais une demande GEt """

        if self.path == '/':
            """je fais ma condition dans la quel je dis le cheminement"""

            self.send_response(200)
            """ je resoit une reponse 200 qui est valide """

            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            """ la si mon code est valide je recoit un message text hello blablabla"""

        elif self.path == '/data':
            """ sinon je fais un autre cheminemt qui ira ans la data"""

            self.send_response(200)
            """si c'est bon je recois 200"""
            
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": " New York"}
            self.wfile.write(json.dumps(data).encode())
            """si c'est valide je recois un message de ma bibiotheque json qui va me donner toute les information demander"""

        elif self.path == '/status':
            """ sinon je fais un autre cheminement similaire a la deuxieme condition"""

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())
            """pareil que la deuxieme condition et affichera ok"""

        elif self.path == '/info':
            """ pareil que les autres"""

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"Version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())
            """pareil que les autres"""

        else:
            self.send_response(404)
            """ si je reoit 404 qui et une erreur"""

            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())
            """ et m'envoi un message d'erreur"""

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
    """on sort des condition et with avec pour ensuit imprimer le port"""