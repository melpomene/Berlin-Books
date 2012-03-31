import web

render = web.template.render('templates/')

def index(**k):
	fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://localhost:8080/callback")
	return render.index("test", fb.auth_string)

def callback(**k):
	oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://localhost:8080/callback")
	return render.callback(k['code'])