import web

render = web.template.render('templates/')

def index(**k):
	return render.index("test")

def callback(**k):
	return render.callback(k['code'])