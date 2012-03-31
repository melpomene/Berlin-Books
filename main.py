import web, view


render = web.template.render('templates/')
        
urls = (
    '/', 'index',
    '/callback', 'callback',
    '/auth', 'auth',
)

web.config.debug = False

app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'auth_token': "undefined"})

class index:
	def GET(self):
		return session.auth_token
		return render.base(view.index(session.auth_token))

class callback:
	""" Callback from facebook oauth 2 """
	def GET(self):
		ans = web.input(secret = "")
		return render.base(view.callback(code=str(ans.code), session=session))

class auth:
	"""Promt for facebook login""" 
	def GET(self): 
		return "AUTH HERE"



if __name__ == "__main__":
    app.run()