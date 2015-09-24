from setuptools import setup, find_packages

setup(
    name='relaypy',
    version='0.1.dev0',
    description="Relay Python Experiment",
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'graphqllib',
        'graphql-relay',
        'wsgi_graphql',
        'webob'
    ],
    entry_points={
        'console_scripts': [
            'relaypy_server = relaypy.server:server',
        ]
    },
)
