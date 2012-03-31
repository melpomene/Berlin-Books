import web, ConfigParser, urlparse, tempfile
import auth as oauth2

config = ConfigParser.RawConfigParser()
config.read('config.ini')
FACEBOOK_ID = config.get("FACEBOOK", "ID")
FACEBOOK_SECRET = config.get("FACEBOOK", "SECRET")

render = web.template.render('templates/')

def index(**k):
	fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://0.0.0.0:8080/callback")
	return render.index(auth=fb.auth_string, access_token=k['access_token'])

def callback(**k):
	fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://0.0.0.0:8080/callback")
	print("Doing the auth token request")
	string = fb.request_access_token(k['code'])
	print "Got answer now parsing"
	response = urlparse.parse_qs(string)
	print("done doing the auth token request.")

	session 				= k['session']
	session.access_token 	= response['access_token']
	print session.access_token
	session.expires 		= response['expires']
	print session.expires
	return render.callback()
