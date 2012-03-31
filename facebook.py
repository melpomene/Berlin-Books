import requests, json

baseurl = 'https://graph.facebook.com/'
access_token_query = '?access_token='

def facebook():
	def __init__(self, token): 
		self.access_token = access_token_query + token
	
	def get_friends(self):
		""" Prints all friends"""
		query_url = baseurl +'me/friends' + access_token + self.access_token
		r = requests.get(query_url)
		if r.status_code != 200: 
			print "There was a problem connecting to facebook.\nStatus code: " + str(r.status_code)
		else:
			jr = json.load(r.content)
			for friend in jr["data"]:
				print friend["name"] + "\n"

	def get_books(self, friend_id):
		query_url = baseurl +str(friend_id) + '/books' + access_token + self.access_token
		r = requests.get(query_url)
		if r.status_code != 200:
			print "There was a problem connecting to facebook.\nStatus code: " + str(r.status_code)
		else:
			jr = json.load(r.content):
				for book in jr["data"]:
					print book['name'] + '\n'
		



