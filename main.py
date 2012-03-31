import web, view


render = web.template.render('templates/')
        
urls = (
    '/', 'index',
    '/callback', 'callback',
)

web.config.debug = False

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'access_token': 'undefined', 'expires':'0'})

class index:
	def GET(self):
		print(session)
		return render.base(view.index(access_token=session.access_token, session=session))

class callback:
	""" Callback from facebook oauth 2 """
	def GET(self):
		ans = web.input(secret = "")
		return render.base(view.callback(code=str(ans.code), session=session))


if __name__ == "__main__":
    app.run()