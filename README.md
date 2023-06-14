# lspxnuts-proxyserver
This is some code to create an AORTA-Nuts proxy server.
The idea is to create a Docker-image that includes:
- A Python-based web server
- WIP A Python-script 
- TO DO An .htacess-file that makes sure that all incoming requests (also to /relative/path) are passed through to the Python-script
- TO DO Some .csv- of .json-files that contain some identifier-mappings.

## Functionality
- The Proxy-server exposes itself as a public API that can be used by Nuts-network-participants and AORTA-network-participants
- For Nuts-network-participants the API mimics the behaviour of the authorization server and resource server as specified in the "Toepassing-op-Nuts BgZ"
- For AORTA-network-participants the API mimics the behavious of GBZ's (check with VZVZ)
- The proxy-server is able to transform incoming Nuts-based requests to outgoing AORTA-based requests

## NEW how to use
1. In Visual Studio Code: https://code.visualstudio.com/docs/python/tutorial-flask
2. In short: run and the api is available on http://127.0.0.1:8000

## NEW code structure
- ./app.py initializes the api
- ./resources contains all the classes for the seperate api-endpoints (e.g. notify, request-access-token)
- ./aorta contains classes for interacting with aorta components, e.g. aorta_authorization_client is a client for the aorta authorization server
- ./nuts contains classes for interacting with the nuts-node, e.g. nuts_vcr_client
- ./config.json contains configuration
- Dockerfile needs update

## OLD How to use
1. Put the base-url of the Nuts-node in the variable BASE_URL_NUTS_NODE (example: "http://host.docker.internal:1323" )
2. Build and run the Docker-image
```
$ docker build -t lspxnuts-proxy-docker .
$ docker run -d -p 8000:8000 lspxnuts-proxy-docker

OLD: $ docker build -t my-python-app .
OLD: $ docker run -p 8000:8000 -it --rm --name my-running-app my-python-app
```
3. send requests to the Proxy-server's API by using Postman and debug!


## How-to run locally
1. Install poetry
```shell
brew install poetry
```
2. Install the dependencies:
```shell
poetry install
```
3. Run the application
```shell
poetry run flask --app app run
```

## How to build and run the docker image
```shell
docker build -t lspxnuts-proxy-docker .
docker run -d -p 8000:8000 lspxnuts-proxy-docker
```
