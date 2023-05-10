# lxpxnuts-proxy-server
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

## How to use
1. Put the base-url of the Nuts-node in the variable BASE_URL_NUTS_NODE (example: "http://host.docker.internal:1323" )
2. Build and run the Docker-image
```
$ docker build -t my-python-app .
$ docker run -it --rm --name my-running-app my-python-app
```
3. send requests to the Proxy-server's API by using Postman and debug!
