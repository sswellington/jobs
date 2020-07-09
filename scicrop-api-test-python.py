import json
import requests as req

def open_json(file):
	"""
	Open a file json of the disk and the function return this file json
	Use the lib `json` - RFC 7159
		https://docs.python.org/3/library/json.html?highlight=json#module-json	
	...
	Parameters:
	file : str
		path where is the json file
	Return : datatypes
		json file
	"""
	with open(file) as f:
		return (json.load(f))

def submit(addressee, message): 
	"""
	Send messagem for address
	Use the lib `request`
		https://requests.readthedocs.io/en/master/
	...
	Parameters:
	addressee : str
		url of addressee
	message : datatypes
		message content in json format  
	Return : unsigned int
		get HTTP Status Messages 
		more information: 
		https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
	"""
	ack = req.post(url=addressee, json=message)
	return (ack.status_code)

if __name__ == '__main__':
	data = open_json('test.json')
	url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'
	
	try:
		ack = submit(url,data)
		if (ack == 200) :
			print("Message sent successfully")
		else :
			print("Error sending message:",ack)
	except req.exceptions.RequestException as e:
		raise SystemExit(e)