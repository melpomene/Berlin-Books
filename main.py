import web

render = web.template.render('templates/')
        
urls = (
    '/', 'index',
    '/callback', 'callback',
    '/auth', 'auth',
)

app = web.application(urls, globals())


class index:
	def GET(self):
		name = 'Bob'    
		return render.index(name)

class callback:
	""" Callback from facebook oauth 2 """
	def GET(self):
		return "GET CALLBACK"

class auth:
	"""Promt for facebook login""" 
	def GET(self): 
		return "AUTH HERE"


if __name__ == "__main__":
    app.run()