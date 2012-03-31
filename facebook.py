import http, json

baseurl = 'https://graph.facebook.com/'
access_token_query = '?access_token='

class Facebook():

	def __init__(self, token): 
		self.access_token = access_token_query + token
	
	def get_friends(self):
		""" Prints all friends"""
		query_url = baseurl +'me/friends' + self.access_token
		
		r = http.get(query_url)
		if r.status_code != 200: 
			print "There was a problem connecting to facebook.\nStatus code: " + str(r.status_code)
		else:
			jr = json.loads(r.content)
			return jr["data"]

	def get_books(self, friend_id="me"):
		query_url = baseurl +str(friend_id) + '/books' + self.access_token
		print query_url
		r = http.get(query_url)

		if r.status_code != 200:
			print "There was a problem connecting to facebook.\nStatus code: " + str(r.status_code)
		else:
			jr = json.loads(r.content)
			string = ""
			#for book in jr["data"]:
			#	string += book['name'] + '\n'
			#return string

	def generate_batch_request(self, friends):
		batch = list()
		print friends[10]["id"]
		for friend in friends:
			entry = dict()
			entry['method'] = 'GET'
			entry['relative_url'] = friend['id'] + "/books"
			batch.append(entry)
		# batch_req = "&batch=" + json.dumps(batch)

		batch_req = '&batch=[{"method": "GET", "relative_url": "me"},\
            {"method": "GET", "relative_url": "me/friends?limit=50"}]'
		

		query_url = baseurl + self.access_token + batch_req
		response = http.get(query_url)
		print response.content
		return json.dumps(batch)



