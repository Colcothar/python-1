import unirest

def myCallback(response):
	print ("code:"+ str(response.code))
 	print ("******************")
	print ("headers:"+ str(response.headers))
	print ("******************")
	print ("body:"+ str(response.body))
	print ("******************")
	print ("raw_body:"+ str(response.raw_body))

def consumeGetAsync():
	params = {'test1':'param1','test2':'param2'}
	url = 'http://httpbin.org/get'
	entete = {"Accept": "application/json"}
	unirest.get(url, headers = entete, params = params, callback = myCallback)

if __name__ == '__main__':
	consumeGetAsync()
