from graphql_wsgi import graphql_wsgi
from wsgiref.simple_server import make_server
from webob.dec import wsgify
from webob.exc import HTTPNotFound
from webob.static import DirectoryApp, FileApp
from .schema import StarWarsSchema


def server():
    graphql = graphql_wsgi(StarWarsSchema)
    static = DirectoryApp('build', index_page=None)
    index = FileApp('index.html')
    graphiql = FileApp('graphiql.html')

    @wsgify
    def mount_graphql(request):
        if request.path_info_peek() == '':
            return request.get_response(index)
        if request.path_info_peek() == 'graphiql':
            return request.get_response(graphiql)
        popped = request.path_info_pop()
        if popped == 'graphql':
            return request.get_response(graphql)
        elif popped == 'static':
            return request.get_response(static)
        raise HTTPNotFound()

    server = make_server('127.0.0.1', 5000, mount_graphql)
    print "Python GraphQL server running on http://127.0.0.1:5000/graphql"
    print "React with Relay UI available on http://127.0.0.1:5000"
    server.serve_forever()
