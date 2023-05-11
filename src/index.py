from http.server import HTTPServer, BaseHTTPRequestHandler
import logging, requests, json

BASE_URL_NUTS_NODE = "http://host.docker.internal:1323"

class S(BaseHTTPRequestHandler):
	def _set_response(self):
		responseCode = 200
		responseObj = { "hello": "world"}

		#introspect incoming access token
		bearer = self.headers['Authorization'] # Bearer YourTokenHere
		if bearer is None:
			responseCode = 403
			responseObj = {"no": "token"}
			print('no token!')
		else:
			token = bearer.split()[1]  # YourTokenHere
			tokenvalidationresult = introspect_access_token(token)
			pyObj = tokenvalidationresult
			#print(pyObj)
			if(pyObj["active"] == False):
				responseCode  = 403
				responseObj = pyObj
			else:
				responseObj = { "token": "okay!"}
		
		self.send_response(responseCode)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		self.wfile.write(json.dumps(responseObj).encode('utf-8'))
	def do_GET(self):
		print("GET request,\n\nPath: " + str(self.path) + "\n\nHeaders:\n" + str(self.headers) + "\n")
		self._set_response()

	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		print("POST request\n\nPath:" + str(self.path) + "\n\nHeaders:\n" + str(self.headers) + "Body:\n" + post_data.decode('utf-8') + "\n")
		self._set_response()  

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

	#we need an exception handler here for
	response = requests.post(endpoint, data=request_body, headers=headers)

	if response.status_code == 200:
		return response.json()
	else:
		raise Exception(f"Introspection failed with status code {response.status_code}: {response.text}")
		return False

if __name__ == "__main__":
	run()