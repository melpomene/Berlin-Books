import http, urllib, json

base_url = "https://www.googleapis.com/books/v1/volumes"

def get_book_info(name):
	query_url = base_url + "?q=" + urllib.quote(name)
	r = http.get(query_url)
	json_r = json.loads(r.content)
	if (json_r['items'] > 0):
		item = json_r['items'][0]
		return_item = dict()
		if 'title' in item['volumeInfo']:       return_item['title'] = item['volumeInfo']['title']
		if 'authors' in item['volumeInfo']:     return_item['authors'] = item['volumeInfo']['authors']
		if 'description' in item['volumeInfo']: return_item['description'] = item['volumeInfo']['description']
		if 'imageLinks' in item['volumeInfo']:  return_item['images'] = item['volumeInfo']['imageLinks']
		return return_item
	else:
		raise Exception("no metadata found.")