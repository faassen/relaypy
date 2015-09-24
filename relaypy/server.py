from wsgi_graphql import wsgi_graphql
from wsgiref.simple_server import make_server
from webob.dec import wsgify
from webob.exc import HTTPNotFound

from .schema import StarWarsSchema


def server():
    graphql_wsgi = wsgi_graphql(StarWarsSchema)

    @wsgify
    def mount_graphql(request):
        if request.path_info_pop() != 'graphql':
            raise HTTPNotFound()
        return request.get_response(graphql_wsgi)

    server = make_server('127.0.0.1', 5000, mount_graphql)
    print "Python GraphQL server running on http://127.0.0.1:5000"
    server.serve_forever()
