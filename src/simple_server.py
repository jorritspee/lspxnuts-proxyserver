from http.server import HTTPServer, BaseHTTPRequestHandler
import logging, requests, json

BASE_URL_NUTS_NODE = "http://host.docker.internal:1323"

class S(BaseHTTPRequestHandler):
	def _set_response(self):
		#introspect incoming access token
		bearer = self.headers['Authorization'] # Bearer YourTokenHere
		token = bearer.split()[1]  # YourTokenHere
		tokenvalidationresult = introspect_access_token(token)
                
		#pyObj = json.loads(tokenvalidationresult)
		pyObj = tokenvalidationresult
		
		#print(pyObj)
		
		if(pyObj["active"] == False):
			self.send_response(403)
		else:
			self.send_response(200)
			
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps(tokenvalidationresult).encode('utf-8'))
	def do_GET(self):
		logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
		self._set_response()
                
		#bearer = self.headers['Authorization'] # Bearer YourTokenHere
		#token = bearer.split()[1]  # YourTokenHere
		#tokenvalidationresult = introspect_access_token(token)
		self._set_response()
		#self.wfile.write("\ntoken validation result: {}".format(tokenvalidationresult).encode('utf-8'))

		self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))
		self.wfile.write("\nheaders: {}".format(self.headers).encode('utf-8'))
	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
		self._set_response()
                
		#bearer = self.headers['Authorization'] # Bearer YourTokenHere
		#token = bearer.split()[1]  # YourTokenHere
		#tokenvalidationresult = introspect_access_token(token)
		self._set_response()
		#self.wfile.write("\ntoken validation result: {}".format(tokenvalidationresult).encode('utf-8'))
                
		self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
		self.wfile.write("\nheaders: {}".format(self.headers).encode('utf-8'))
		self.wfile.write("\npost data: {}".format(post_data).encode('utf-8'))
        

def run(server_class=HTTPServer, handler_class=S):
    """Entrypoint for python server"""
    server_address = ("0.0.0.0", 8000)
    httpd = server_class(server_address, handler_class)
    print("launching server...")
    httpd.serve_forever() 

def introspect_access_token(access_token):
    """
    Introspects an access token to determine its validity.
    Args:
        access_token (str): The access token to introspect.
    Returns:
        dict: A dictionary containing information about the access token if it is valid.
    Raises:
        Exception: If the introspection request fails or the token is invalid.
    """
    endpoint = f"{BASE_URL_NUTS_NODE}/internal/auth/v1/accesstoken/introspect"
    request_body = { "token" : f"{access_token}" }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(endpoint, data=request_body, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Introspection failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    run()