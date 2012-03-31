import web, view


render = web.template.render('templates/')
        
urls = (
    '/', 'index',
    '/callback', 'callback',
)

web.config.debug = False
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'auth_token': 'undefined', 'expires':'0'})

class index:
	def GET(self):
		return render.base(view.index(auth_token=session.auth_token))

class callback:
	""" Callback from facebook oauth 2 """
	def GET(self):
		ans = web.input(secret = "")
		return render.base(view.callback(code=str(ans.code), session=session))


if __name__ == "__main__":
    app.run()