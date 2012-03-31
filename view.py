import web, ConfigParser, urlparse, tempfile
import auth as oauth2

config = ConfigParser.RawConfigParser()
config.read('config.ini')
FACEBOOK_ID = config.get("FACEBOOK", "ID")
FACEBOOK_SECRET = config.get("FACEBOOK", "SECRET")

render = web.template.render('templates/')

def index(**k):
	fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://localhost:8080/callback")
	return render.index(auth=fb.auth_string)

def callback(**k):
	fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://localhost:8080/callback")
	response = urlparse.parse_qs(fb.request_access_token(k['code']))
	session = k['session']
	session.access_token 	= response['access_token']
	session.expires 		= response['expires']
	print session.expires

	return render.callback()
