import web, ConfigParser, urlparse, tempfile, facebook
import auth as oauth2

config = ConfigParser.RawConfigParser()
config.read('config.ini')
FACEBOOK_ID = config.get("FACEBOOK", "ID")
FACEBOOK_SECRET = config.get("FACEBOOK", "SECRET")

render = web.template.render('templates/')

def index(**k):
	fb_auth = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://0.0.0.0:8080/callback")
	if k['access_token'] == "undefined":
		return render.auth(auth=fb_auth.auth_string)
	else:
		session = k['session']
		fb = facebook.Facebook(session.access_token)
		friends = fb.get_friends()
		friends_books = ""
		for friend in friends: 

			print friend["id"]
			books = fb.get_books(friend["id"])
			print books
			friends_books += books

		#books = fb.get_books()

		return render.index(friend_list="", book_list= "", friend_book_list=friends_books)

def callback(**k):
	fb = oauth2.FacebookAuth(FACEBOOK_ID, FACEBOOK_SECRET, "http://0.0.0.0:8080/callback")
	string = fb.request_access_token(k['code'])
	response = urlparse.parse_qs(string)
	session 				= k['session']
	session.access_token 	= response['access_token'][0]
	session.expires 		= response['expires'][0]
	return render.callback()
