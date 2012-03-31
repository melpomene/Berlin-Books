import oauth2
class Auth(CLIENTID, callback_url):

	# 1. Request access from our app to the readmill account by redirect to auth-link
	# 2. Returns, with auth code in querystring, http://example.com/callback?code=acfbd2c5
	# POST to "http://readmill.com/oauth/token?grant_type=authorization_code&client_id=acfbd2c5&client_secret=e45a23&redirect_uri=http://example.com/callback&code=acfbd2c5"

	def __init__:
		self.CLIENTID = CLIENTID
		self.readmill_token = 		"http://readmill.com/oauth/token"
		self.readmill_auth_link = 	"http://readmill.com/oauth/authorize?response_type=code&client_id=" 
									+ self.CLIENTID + "&redirect_uri=" + self.callback_url

	def auth_urll(self):

	def authReadmill():
