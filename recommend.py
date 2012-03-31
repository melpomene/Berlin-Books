
class Recommend():
	def build_dict(self, users_book_list):
		"""
		Expecting  [{"name":"tom", "books":["bok1", "bok2"]},{"name":"eva", "books":["bok1"] } ]

		"""
		d = {}
		i = 0
		for user in users_book_list:
			for book in user["books"]:
				if book not in d.values():
					d[i] = book
					i += 1
		matrix = []

		for i in xrange(len(users_book_list)):
			row = []
			for j in xrange(len(d)):
				if d[j] in users_book_list[i]["books"]: 
					row.append(1)
				else:
					row.append(0)
			matrix.append(row)

		self.matrix = matrix
		self.book_dictionary = d
	def build_user(self, user_book_list):
		"""
			Expecting list of books by user
		"""
		user = []
		for i in xrange(len(self.book_dictionary)):
			if self.book_dictionary[i] in user_book_list:
				user.append(1)
			else:
				user.append(0)
		self.user = user
		

	def compare(self):
		greatest = 0
		greatest_user = None
		for user in self.matrix:
			total = 0
			for i in xrange(len(self.user)):
				if self.user[i] == 1 and user[i] == 1: 
					total += 1
			if total > greatest:
				greatest = total
				greatest_user = user

		print "You: \t\t\t" + str(self.user)
		print "Your best match: \t" + str(greatest_user)
		print "Maybe you have missed out these titles:"
		for i in xrange(len(self.user)):
			if self.user[i] == 0 and greatest_user[i] == 1:
				print self.book_dictionary[i] 
				
		
if __name__ == "__main__":
	r = Recommend()
	r.build_dict([{"name":"tom", "books":["bok1", "bok2", "bok3"]}, {"name":"eva", "books":["bok1", "bok4"] } ])
	r.build_user(["bok1", "bok2"])
	r.compare()

