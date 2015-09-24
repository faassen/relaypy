from wsgi_graphql import wsgi_graphql
from wsgiref.simple_server import make_server

from .schema import StarWarsSchema


def server():
    wsgi = wsgi_graphql(StarWarsSchema)
    server = make_server('127.0.0.1', 5000, wsgi)
    server.serve_forever()
