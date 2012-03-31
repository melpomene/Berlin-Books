import web, ConfigParser, urlparse
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
	web.config.session_parameters.handler = 'file'
	web.config.handler_parameters.file_prefix = 'sess'
	web.config.handler_parameters.file_dir = '/tmp'
	s = web.ctx.session
	s.start()
	s.auth_token = response

	print s.auth_token
	return render.callback()
