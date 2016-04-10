# Demo of GraphQL Relay server in Python

This uses graphql-relay and graphql-wsgi to implement a
Relay-compliant GraphQL server in Python. It exposes the Relay "Star
Wars" model. It is an example of how you can use
[graphql-wsgi](https://github.com/faassen/graphql-wsgi).

To build it you can cobble it together using `pip` yourself, but beware you
need to do some checkouts first of the various projects as there are
no releases yet.

Alternatively you can use buildout (using a clean Python from a
virtual environment):

```
$ python bootstrap-buildout.py
$ bin/buildout
```

This grabs all the sources automatically.

Once you have it installed, you should have a demo server available
called `relaypy_server`. If you used buildout, you can do:

```
bin/relaypy_server
```

You can then go to http://localhost:5000/graphql and do queries, for instance::

```
http://localhost:5000/graphql?query={rebels{ships{edges{node{id,%20name}}}}}
```

You can also go to http://localhost:5000/graphiql to see a graphical
user interface that lets you explore the schema.

To rebuild the graphiql editor:

```
npm install
npm run build
```
