# -*- coding: utf-8 -*-
import requests
import json

class Facebook(object):
	def __init__(self):
		self.s=requests.session()
		self.s.headers.update({'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
		self.s.verify=False
	
	def getID(self,token):
		r=self.s.get('https://graph.facebook.com/v2.8/me?access_token='+token+'&debug=info&fields=id%2C name%2C email&format=json&include_headers=false&sdk=ios')
		if 's only accessible on the User object after th' in r.content:
			return str(json.loads(r.content)['id'])
		return None
	