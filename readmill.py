import requests, json
class Readmill():
    CLIENTID = "95cc31aac4a26da8b5c67388120428b4"
    baseUrl = "http://api.readmill.com"
    
    def getUser(self, id):
        r = requests.get( baseUrl + "/users/"+str(id)+"?client_id="+CLIENTID)
        if r.status_code == 200: 
            return json.loads(r.content)
        else: 
            raise Exception, "Error Occured: " + str(r.error)
    def
    
    def getBook(id):
        r = requests.get( baseUrl + "/books/"+str(id)+"?client_id="+CLIENTID)
        if r.status_code == 200: 
            return json.loads(r.content)
        else: 
            raise Exception, "Error Occured: " + str(r.error)
            
    def findBook(title=None, author=None, isbn=None)
        baseStr = baseUrl + "/books/match?client_id="+CLIENTID
        params = []
        if title is not None:
            params.append("&q[title]=" + title)
        if author is not None:
            params.append("&q[author]=" + author)
        if isbn is not None:
            params.append("&q[isbn]=" + isbn)
        baseStr += ''.join(params)
        r = requests.get(baseStr)
        if r.status_code == 200: 
            return json.loads(r.content)
        else: 
            raise Exception, "Error Occured: " + str(r.error)
    
    def auth(self):
        pass # http://pypi.python.org/pypi/requests-oauth
    
    
    
    
