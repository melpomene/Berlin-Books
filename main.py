import web, ConfigParser, view
import auth as oauth2
config = ConfigParser.RawConfigParser()
config.read('config.ini')
FACEBOOK_ID = config.get("FACEBOOK", "ID")
FACEBOOK_SECRET = config.get("FACEBOOK", "SECRET")

render = web.template.render('templates/')
        
urls = (
    '/', 'index',
    '/callback', 'callback',
    '/auth', 'auth',
)

app = web.application(urls, globals())


class index:
	def GET(self):
		fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://localhost:8080/callback")
		return fb.auth_string
		#return render.base(view.index())

class callback:
	""" Callback from facebook oauth 2 """
	def GET(self):
		ans = web.input(secret = "")
		return render.base(view.callback(code=str(ans.code)))

class auth:
	"""Promt for facebook login""" 
	def GET(self): 
		return "AUTH HERE"


if __name__ == "__main__":
    app.run()