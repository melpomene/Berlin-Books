import http, json, urllib

baseurl = 'https://graph.facebook.com/'
access_token_query = '?access_token='

class Facebook():

	def __init__(self, token): 
		self.access_token = token
	
	def get_friends(self):
		""" Prints all friends"""
		query_url = baseurl +'me/friends?access_token=' + self.access_token
		
		r = http.get(query_url)
		if r.status_code != 200: 
			print "There was a problem connecting to facebook.\nStatus code: " + str(r.status_code)
		else:
			jr = json.loads(r.content)
			return jr["data"]

	def get_books(self, friend_id="me"):
		query_url = baseurl +str(friend_id) + '/books?access_token=' + self.access_token
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
		responses = list()
		print friends[10]["id"]

		for i in range(len(friends)):
			entry = dict()
			entry['method'] = 'GET'
			entry['relative_url'] = friends[i]['id'] + "/books"
			batch.append(entry)
			if (i%50 == 49) or (i == len(friends)-1):
				batch_req = json.dumps(batch)
				post_data = "access_token=" + self.access_token +"&batch=" + batch_req
				response = http.post(baseurl, post_data)
				responses.append(response.content)
				batch = list()
				## REMOVE ME
				break


		for response in responses:
			json_response = json.loads(response)
			print json_response
		return json.dumps(batch)

	def do_fql_request(self):
		queries = dict()
		friends_query = '"friends_q":"SELECT uid2 FROM friend WHERE uid1 = me()"'
		books_query = '"books_q":"SELECT uid,books FROM user WHERE uid IN (SELECT uid2 FROM #friends_q) AND books != \'\' "'
		req_url = baseurl + "fql?q=" + urllib.quote("{" + friends_query + "," + books_query + "}") + "&access_token=" + self.access_token
		#print req_url
		r = http.get(req_url)
		json_r = json.loads(r.content)
		print json_r['data'][1]['fql_result_set']


		#print r.content

