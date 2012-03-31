import requests

class ReadmillAuth:

	def __init__(self, client_id, client_secret, redirect_uri):
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri
		self.auth_str = "http://readmill.com/oauth/authorize?response_type=code&client_id=" + \
		                self.client_id + "&redirect_uri=" + self.redirect_uri


	def do_test(self):
		print(self.auth_str)

	def set_callback_code(self, callback_code):
		if (callback_code == "user_denied"):
			raise Exception("User denied.")
		self.callback_code = callback_code

	def generate_access_token(self):
		access_token_uri = "http://readmill.com/oauth/token?grant_type=authorization_code&client_id=" + \
		                   self.cliend_id + "&client_secret=" + self.client_secret + "redirect_uri=" + \
		                   self.redirect_uri + "&code=" + callback_code
		requests.post(access_token_uri)

	def generate_refresh_token(self, refresh_token):
		refresh_token = "http://readmill.com/oauth/token?grant_type=refresh_token&client_id=" + \
		                self.client_id + "&client_secret=" + self.client_secret + "&refresh_token=" + \
		                refresh_token

class FacebookAuth:
	