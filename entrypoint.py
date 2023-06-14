"""
Server module for running this application with Docker
"""
import os

from waitress import serve

from app import app

port = os.environ['PORT'] if 'PORT' in os.environ else 8080
host = os.environ['HOST'] if 'HOST' in os.environ else '0.0.0.0'
threads = int(os.environ['THREADS']) if 'THREADS' in os.environ else 10
print(f'Starting app {app} application on port {host}:{port}')
serve(app, host=host, port=port, threads=threads)
