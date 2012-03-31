import web, ConfigParser
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
	oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://localhost:8080/callback")
	return render.callback(code = k['code'])