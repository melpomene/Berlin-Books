import requests, json, urllib
class Readmill():
    def __init__(self):
        self.CLIENTID = "95cc31aac4a26da8b5c67388120428b4"
        self.baseUrl = "http://api.readmill.com"
    
    def getUser(self, id):
        r = requests.get( self.baseUrl + "/users/"+str(id)+"?client_id="+self.CLIENTID)
        if r.status_code == 200: 
            return json.loads(r.content)
        else: 
            raise Exception, "Error Occured: " + str(r.error)
    
    def getBook(self, id):
        r = requests.get( self.baseUrl + "/books/"+str(id)+"?client_id="+self.CLIENTID)
        if r.status_code == 200: 
            return json.loads(r.content)
        else: 
            raise Exception, "Error Occured: " + str(r.error)
            
    def auth(self):
        pass # http://pypi.python.org/pypi/requests-oauth

if __name__ == "__main__":
    print "Running tests:"
    r = Readmill()
    print "Get user 1"
    print r.getUser(1)
    print "Find book"
    print r.findBook(isbn="9780765319852") 
    
    
    
    
