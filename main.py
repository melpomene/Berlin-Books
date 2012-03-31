import web
import view

render = web.template.render('templates/')
        
urls = (
    '/', 'index',
    '/callback', 'callback',
    '/auth', 'auth',
)

app = web.application(urls, globals())


class index:
	def GET(self):
		return render.base(view.index())

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