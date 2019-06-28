# -*- coding: utf-8 -*-
from __future__ import division
from random import randint
from subprocess import *
import StringIO
import argparse
import inspect
import json
import logging
import os
import random
import re
import requests
import socket
import struct
import sys
import time
import traceback
import updater
import linecache
from collections import OrderedDict
#Local
from facebook import Facebook
from tools import Tools
try:
	import global_mst
	import japan_mst
except:
	pass

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getVersion():
	return '3'
	#return Popen('git rev-parse HEAD', stdout=PIPE, shell=True).stdout.read ().strip ()

class API(object):
	def __init__(self,japan=False):
		self.isJapan=False
		if japan:
			self.setIsJapan()
		self.verboose=True#MILA False
		self.bot_version=getVersion()#3
		print '[+] Version %s loaded'%(self.bot_version)
		self.current_mst=self.loadMST()
		self.t=Tools(2 if self.isJapan else 1)
		self.s=requests.session()
		self.s.headers.update({'Content-Type':'application/x-www-form-urlencoded','Connection':'keep-alive','User-Agent':'FF%20EXVIUS/2.1.3 CFNetwork/808.1.4 Darwin/16.1.0','Accept-Language':'en-us'})
		self.s.verify=False
		#if 'win' not in sys.platform:
		#	self.s.proxies.update({'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',})#self.t.getRandomProxy())
		#if 'win' in sys.platform:
		#	self.s.proxies.update({'http': 'http://127.0.0.1:8888','https': 'https://127.0.0.1:8888',})
		self.settings={}
		self.settings['qrVcDe48']=''
		self.settings['user']={}
		self.settings['user']['units']={}
		self.settings['user']['ach']=None
		self.settings['user']['session_device']=self.t.genRandomDeviceID()
		self.settings['openedChests']=[]
		self.settings['friends']={}
		self.settings['units']={}
		self.settings['user']['license']='test'
		self.isJapan=False
		self.isStarter=True
		self.isFresh=False
		self.isFacebook=False
		self.lastError='error #3'
		self.db=None
		self.canRetry=True
		self.dropped_stuff=[]
		self.lastFriend=0
		self.allUnits=0
		self._api_time=0
		self.current_farm_loop=0
		self.run_count=0
		self.error_repeat=0
		self.run_mid=0
		self.proxy='NO'
		self.lb=0
		self.canFriend=False
		self.canRefill=False
		self.canChest=False
		self.canLoot=False
		self.canELoot=False
		self.canUnits=False
		self.canSolve=False
		self.isMaster=False
		self.canOrbs=False
		self.canCOrbs=False
		self.isSummon=False
		self.isMaintance=False
		self.doEquipInj=None
		self.doItemInj=None
		self.doMateriaInj=None
		self.isinject=False
		self.wM9AfX6I=None
		self.F_RSC_VERSION=0
		self.F_MST_VERSION=0
		self.gl_base='https://v365-lapis.gumi.sg/lapisProd/app/php/gme'
		self.jp_base='https://v57-ios.game.exvius.com/lapis/app/php/gme'
		print '[+] ready to work'

	def setUSERID(self,id):
		self.P_USER_ID=id

	def setHANDLENAME(self,id):
		self.P_HANDLE_NAME=id

	def setMODEL_CHANGE_CNT(self,id):
		self.P_MODEL_CHANGE_CNT=str(id)
		
	def setDevice(self,id):
		self.settings['K1G4fBjF']=str(id)
		
	def setDeviceId(self,id,device):
		self.device_id=id
		self.settings['K1G4fBjF']=str(device)
		
	def hasLicense(self):
		return 'test' not in self.settings['user']['license']
		
	def setIsInject(self):
		self.isinject=True
		
	def setIsJapan(self):
		self.isJapan=True
		
	def whoami(self):
		try:
			return inspect.stack()[1][3]
		except:
			return ''
		
	def getLastError(self):
		self.dolog('%s() was called'%(self.whoami()))
		return self.lastError
		
	def haveNewUnits(self):
		tmp_cnt=self.allUnits
		_data=self.GetUserInfoRequest()
		if _data:
			B71MekS8=json.loads(_data)['B71MekS8']
			if tmp_cnt<>len(B71MekS8):
				return True
		return False

	def getUser_ID(self):
		try:
			return self.settings['user']['m3Wghr1j']
		except:
			return None

	def getUSERID(self):
		try:
			return self.settings['user']['9Tbns0eI']
		except:
			return None

	def getHANDLE(self):
		try:
			return self.settings['user']['9qh17ZUf']
		except:
			return None

	def dolog(self,s):
		try:
			if 'ffbf' <> socket.gethostname():
				if self.verboose:
					try:
						print '%s%s %s'%('[%s]'%self.settings['user']['m3Wghr1j'] if 'm3Wghr1j' in self.settings['user'] else '',s,time.strftime('%H:%M:%S'))
					except:
						pass
		except:
			pass

	def setDB(self):
		pass

	def closeDB(self):
		pass
		
	def setProxie(self,ip,port):
		self.dolog('%s() was called'%(self.whoami()))
		if ip == 'NO':
			return
		#if self.isMaster and ip is None:
		#	self.s.proxies.update({'http': None,'https': None,})
		if ip and 'socks5' in ip:
			self.s.proxies.update({'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',})
		else:
			pp='%s:%s'%(ip,port)
			self.dolog(pp)
			self.proxy=ip
			self.s.proxies.update({'http': 'http://%s'%(pp),'https': 'https://%s'%(pp),})

	def addTMR(self,id,tmr,charname):
		pass

	def addLoot(self):
		pass

	def updateProxy(self,time):
		pass

	def clearTMR(self):
		pass

	def clearStatus(self):
		pass

	def addAccountInfo(self,plain_res):
		pass

	def changeStatus(self,msg,run,type=0):
		pass

	def setPlayerID(self,id,device):
		self.dolog('id %s device %s'%(id,device))
		self.settings['6e4ik6kA']=id
		self.settings['K1G4fBjF']=str(device)
	
	def setLicense(self,lic):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog(lic)
		self.settings['user']['license']=lic

	def setRefill(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will refill energy')
		self.canRefill=True
		
	def setFriends(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will use friends')
		self.canFriend=True

	def setLb(self,lb):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will add %s lb'%lb)
		self.lb=int(lb)

	def setOrbs(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will refill orbs')
		self.canOrbs=True

	def setCOrbs(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will refill collos orbs')
		self.canCOrbs=True

	def setChests(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will open chests')
		self.canChest=True

	def setLoot(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will collect loot')
		self.canLoot=True

	def setELoot(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will collect exp loot')
		self.canELoot=True

	def setUnits(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will collect units')
		self.canUnits=True

	def setSummon(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.isSummon=True

	def setSolve(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot will solve missions')
		self.canSolve=True

	def setMaster(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.dolog('[+] bot is the Master')
		self.isMaster=True

	def setQuite(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.verboose=False

	def loadMST(self):
		try:
			if self.isJapan:
				return japan_mst.latestmst
			else:
				return global_mst.latestmst
		except:
			self.dolog('loadMST fucked')
			return 0

	def updateMST(self,data):
		self.dolog('%s() was called'%(self.whoami()))
		data=json.loads(data)
		c1qYg84Q=data['c1qYg84Q']
		for i in c1qYg84Q:
			if 'F_RSC_VERSION' == i['a4hXTIm0']:
				F_RSC_VERSION=i['wM9AfX6I']
			if 'F_MST_VERSION' == i['a4hXTIm0']:
				mst=i['wM9AfX6I']
				self.wM9AfX6I=mst
				self.F_MST_VERSION=mst
		print int(self.F_MST_VERSION) == int(mst),self.F_MST_VERSION,mst
		#if int(self.F_MST_VERSION) == int(mst):
		#	return
		if self.isJapan:
			fn='japan_mst.py'
		else:
			fn='global_mst.py'
		with open(fn, 'w') as file:
			if self.isJapan:
				file.write('latestmst=%s\nlatestrsc=%s'%(mst,F_RSC_VERSION))
			else:
				file.write('latestmst=%s'%(mst))
		_looking_for=str(mst)
		try:
			updater.Updater(1 if not self.isJapan else 2).setTT(c1qYg84Q)
		except:
			pass

	def getRandomError(self):
		self.dolog('%s() was called'%(self.whoami()))
		foo = ['counting 0 and 1 while sleeping','somebody heal me','oh no a wild ERROR appeared','deep sleep','this is as frustrating for us as it is for you.']
		return random.choice(foo)

	def getRandomDone(self):
		self.dolog('%s() was called'%(self.whoami()))
		foo = ['task done','dobby is free','ready for another task','give me some work','please give me work']
		return random.choice(foo)

	def getRandomWork(self):
		self.dolog('%s() was called'%(self.whoami()))
		foo = ['working','catching pikachu','cooking','farming','calculating','You try to relax!']
		return random.choice(foo)

	def setFarmMode(self,mid,cnt):
		self.dolog('%s() was called'%(self.whoami()))
		#self.setDB()
		self.current_farm_loop=0
		#try:
		self.dolog('farming to do.. %s %s'%(mid,cnt))
		self.clearTMR()
		taskDone=False
		self.run_count=cnt
		self.run_mid=self.t.findMissionName(mid)
		try:
			while(self.current_farm_loop<cnt):
				res=self.startMission(mid)
				if not res[0]:
					self.dolog('mission dead')
					break
				else:
					if (random.random()<0.7):
						self.changeStatus('~ %.2f min left'%((((cnt-self.current_farm_loop)*17)/60)),self.current_farm_loop+1,2)
					else:
						self.changeStatus(self.getRandomWork(),self.current_farm_loop+1,2)
				self.current_farm_loop+=1
			taskDone = (self.current_farm_loop==cnt)
			self.dolog('farm done %s:%s:%s'%(self.current_farm_loop,cnt,mid))
			if taskDone:
				self.changeStatus(self.getRandomDone(),self.current_farm_loop,1)
			else:
				self.changeStatus(self.getLastError(),self.current_farm_loop,0)
		except Exception,e:
			print str(e)
			if not self.isMaintance:
				self.changeStatus('report this error',self.current_farm_loop,0)
			self.closeDB()
			self.dolog(traceback.print_exc())
			self.dolog('DAS SOLLTE NICHT PASSIEREN')
			return None
		self.closeDB()
		self.dolog('task done')

	def getFresh(self):
		self.dolog('%s() was called'%(self.whoami()))
		return self.isFresh
		
	def setFacebook(self,token,id):
		self.dolog('%s() was called'%(self.whoami()))
		self.settings['fkt']=token
		self.settings['fid']=id
		self.isFacebook=True

	def makemesort(self,q,w):
		return OrderedDict([('a4hXTIm0',q),('wM9AfX6I',w)])

	def createVersionTag(self):
		#self.dolog('%s() was called'%(self.whoami()))
		_data=[]
		_data.append(self.makemesort('F_APP_VERSION_IOS' if self.settings['K1G4fBjF']=='1' else 'F_APP_VERSION_AND','1654' if self.isJapan else '1070'))
		_data.append(self.makemesort('F_RSC_VERSION',str(self.F_RSC_VERSION)))
		_data.append(self.makemesort('F_MST_VERSION',str(self.F_MST_VERSION)))
		return _data
		
	def createUserInfoTag(self):
		#self.dolog('%s() was called'%(self.whoami()))
		_data=[{}]
		if self.isJapan:
			_data[0]['6Nf5risL']='0'
			_data[0]['io30YcLA']=self.t.genRandomDeviceString()
			_data[0]['K1G4fBjF']=self.settings['K1G4fBjF']
			_data[0]['e8Si6TGh']=self.t.getHashedDeviceID(self.settings['6e4ik6kA']) if not hasattr(self, 'device_id') else self.device_id
			_data[0]['1WKh6Xqe']='ver.20180523'
			_data[0]['64anJRhx']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
			if not self.isStarter:
				_data[0]['JC61TPqS']=self.settings['user']['JC61TPqS']
				_data[0]['9qh17ZUf']=self.settings['user']['9qh17ZUf']
				_data[0]['9Tbns0eI']=self.settings['user']['9Tbns0eI']
				_data[0]['m3Wghr1j']=self.settings['user']['m3Wghr1j']
				_data[0]['ma6Ac53v']=self.settings['user']['ma6Ac53v']
				_data[0]['6Nf5risL']=self.settings['user']['6Nf5risL']
				_data[0]['D2I1Vtog']='0'
				try:
					_data[0]['D2I1Vtog']=self.settings['user']['D2I1Vtog']
				except:
					pass
		else:
			_data[0]['6Nf5risL']='0'
			_data[0]['io30YcLA']=self.t.genRandomDeviceString()
			_data[0]['Y76dKryw']='DE'
			_data[0]['1WKh6Xqe']='ver.3.0.1'
			_data[0]['NggnPgQC']=self.settings['user']['session_device']
			_data[0]['K1G4fBjF']=self.settings['K1G4fBjF']
			_data[0]['6e4ik6kA']=self.settings['6e4ik6kA']
			_data[0]['e8Si6TGh']=self.t.getHashedDeviceID(self.settings['6e4ik6kA'])
			_data[0]['64anJRhx']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
			if self.isFacebook:
				_data[0]['X6jT6zrQ']=self.settings['fid']
				_data[0]['DOFV3qRF']=self.settings['fkt']
			if not self.isStarter:
				_data[0]['D2I1Vtog']='0'
				_data[0]['JC61TPqS']=self.settings['user']['JC61TPqS']
				_data[0]['9Tbns0eI']=self.settings['user']['9Tbns0eI']
				_data[0]['m3Wghr1j']=self.settings['user']['m3Wghr1j']
				try:
					_data[0]['D2I1Vtog']=self.settings['user']['D2I1Vtog']
				except:
					pass
				_data[0]['9qh17ZUf']=self.settings['user']['9qh17ZUf']
				_data[0]['mESKDlqL']=self.settings['user']['mESKDlqL']
				_data[0]['ma6Ac53v']=self.settings['user']['ma6Ac53v']
				_data[0]['9K0Pzcpd']=self.settings['user']['9K0Pzcpd']
				_data[0]['iVN1HD3p']=self.settings['user']['iVN1HD3p']
		if self.isFresh:
			_data[0]['9qh17ZUf']=self.settings['user']['9qh17ZUf'] if '9qh17ZUf' in self.settings['user'] else 'Rain'
		return _data

	def createSignalKeyTag(self):
		#self.dolog('%s() was called'%(self.whoami()))
		_data=[]
		_data.append({'qrVcDe48':self.settings['qrVcDe48']})
		return _data
		
	def loadRSC(self):
		try:
			self.F_MST_VERSION=str(japan_mst.latestmst)
			self.F_RSC_VERSION=str(japan_mst.latestrsc)
		except:
			pass
		
	def createBody(self,init=False):
		if self.isJapan and self.F_MST_VERSION==0:
			self.loadRSC()
		_data={}
		_data['c1qYg84Q']=self.createVersionTag()
		_data['LhVz6aD2']=self.createUserInfoTag()
		if not init:
			_data['QCcFB3h9']=self.createSignalKeyTag()
		if self.isFacebook:
			_data['Euv8cncS']=[{'K2jzG6bp':'1'}]
		return _data

	def parseUserInfo(self,data):
		#self.dolog('%s() was called'%(self.whoami()))
		LhVz6aD2=json.loads(data)['LhVz6aD2'][0]
		if '9Tbns0eI' in LhVz6aD2 and len(LhVz6aD2['9Tbns0eI'])==0:
			if len(data)<=300:
				self.dolog('UNICORN %s'%(data))
			self.isFresh=True
			if 'win' in sys.platform:
				self.dolog('[+] found fresh account, will do tutorial')
				self.settings['user']['9qh17ZUf']='Rain'
				self.CreateUserRequest()
			else:
				return None
		if '9Tbns0eI' in LhVz6aD2 and len(LhVz6aD2['9Tbns0eI'])>=2:
			for i in LhVz6aD2:
				if i=='9qh17ZUf':
					o=LhVz6aD2[i].encode('ascii','ignore')
					self.settings['user'][i]=o
				else:
					self.settings['user'][i]=LhVz6aD2[i]
			self.isStarter=False

	def parseUserData(self,data):
		#self.dolog('%s() was called'%(self.whoami()))
		LhVz6aD2=json.loads(data)['3oU9Ktb7'][0]
		if '9Tbns0eI' in LhVz6aD2 and len(LhVz6aD2['9Tbns0eI'])>=2:
			for i in LhVz6aD2:
				if i=='B6kyCQ9M':
					self.settings['user']['current_energy']=int(LhVz6aD2[i])
				self.settings['user'][i]=LhVz6aD2[i]
		
	def callApi(self,dtt,id,qo3PECw6=None,repeat=None):
		self.dolog('%s() was called'%(self.whoami()))
		if self.error_repeat >=3:
			self.dolog('have more than 3 repeat exit')
			return None
		key=self.t.getAPIKey(id)
		point=self.t.getAPIPoint(id)
		aid=self.t.getAPIID(id)
		if not repeat:
			_data={}
			_data['TEAYk6R1']={}
			_data['TEAYk6R1']['ytHoz4E2']=self._api_time
			self._api_time+=randint(1,10000)
			_data['TEAYk6R1']['z5hB3P01']=aid
			_data['t7n6cVWf']={}
			try:
				_data['t7n6cVWf']['qrVcDe48']=self.t.encrypt(json.dumps(dtt),key)
			except:
				self.changeStatus('some error',self.current_farm_loop,0)
				self.dolog('O.O wtf %s'%(dtt))
				return None
		else:
			_data=repeat
		if self.isJapan:
			tmpurl=self.jp_base+point
		else:
			tmpurl=self.gl_base+point
		try:
			r=self.s.post(tmpurl,data=json.dumps(_data),stream=True)#,timeout=6)
		except requests.exceptions.ChunkedEncodingError:
			self.lastError='ChunkedEncodingError'
			self.dolog('ChunkedEncodingError proxy dead %s'%(self.settings['user']['m3Wghr1j'] if 'm3Wghr1j' in self.settings['user'] else ''))
			self.changeStatus('ChunkedEncodingError proxy',self.current_farm_loop,0)
			time.sleep(1)
			#if not self.isSummon:
				#self.error_repeat+=1
			return self.callApi(dtt,id)
			#else:
			#	return None
		except requests.exceptions.ProxyError:
			self.updateProxy('proxy dead')
			self.dolog('proxyerror proxy dead %s'%(self.proxy))
			self.lastError='ProxyError'
			self.changeStatus('proxy error',self.current_farm_loop,0)
			return None
		except requests.exceptions.ConnectionError:
			self.updateProxy('proxy dead')
			self.changeStatus('proxy error',self.current_farm_loop,0)
			self.lastError='ConnectionError'
			self.dolog('connectionerror proxy dead %s'%(self.proxy))
			return None
		except requests.exceptions.Timeout:
			self.updateProxy('proxy dead')
			self.changeStatus('proxy timeout',self.current_farm_loop,0)
			self.dolog('Timeout %s'%(self.proxy))
			self.lastError='Timeout'
			time.sleep(2)
			if not self.isSummon:
				self.error_repeat+=1
				return self.callApi(dtt,id)
			else:
				return None
		except:
			self.lastError='some error'
			self.changeStatus('some error',self.current_farm_loop,0)
			self.dolog('FUCKING EXCP %s'%(traceback.print_exc()))
			time.sleep(2)
			if not self.isSummon:
				self.error_repeat+=1
				return self.callApi(dtt,id)
			else:
				return None
		if r.status_code==500:
			self.dolog('we have 500')
			return None
		_chunks=''

		try:
			for chunk in r.iter_content(chunk_size=1024): 
				if chunk:
					_chunks=_chunks+chunk
		except:
			print 'FUCK GUMI 720'
			return self.callApi(dtt,id)
		try:
			if not _chunks:
				self.dolog('no content...')
				return self.callApi(dtt,id)
		except:
			self.dolog('ficken ihn')
			time.sleep(2)
			return self.callApi(dtt,id)
		if 'SERVER_MSG_160' in _chunks:
			return self.callApi(dtt,id)
		#HAS SOME DATA DO SOMETHING
		if 'maintenance' in _chunks or '\u305f\u3060\u3044\u307e' in _chunks:
			self.isMaintance=True
			self.dolog('We are undergoing mainten')
			_looking_for='[Bot] %s maintenance started %s'%('JP' if self.isJapan else 'GL',time.strftime('%d-%m-%Y'))
			self.changeStatus('We are undergoing mainten..',self.current_farm_loop,0)
			self.lastError='We are undergoing mainten..'
			if not self.isMaster:
				return None
				exit(1)
			return None
		if 't7n6cVWf' not in _chunks:
			#self.dolog('WE DONT HAVE GAME DATA %s'%(r.content.replace('\n','').replace('\r','')))
			pass
		if 'bCf65yoK' in _chunks:
			#self.dolog('we have error? %s'%(r.content.replace('\n','').replace('\r','')))
			try:
				_erro=json.loads(_chunks)['bCf65yoK']['Wk1v6upb']
				_error_str=self.t.findError(_erro)
				self.lastError=_error_str
				self.changeStatus(_error_str,self.current_farm_loop,0)
			except:
				self.log('GUMI FUCKED UP RESPONSE')
				return self.callApi(dtt,id)
		#MILA WORK TO DO
		if 'SERVER_MSG_114' in _chunks or 'SERVER_MSG_158' in _chunks or 'SERVER_MSG_36' in _chunks or 'SERVER_MSG_83' in _chunks or 'SERVER_MSG_190' in _chunks or 'SERVER_MSG_129' in _chunks or 'SERVER_MSG_85' in _chunks or 'SERVER_MSG_160' in _chunks:
			#self.dolog('huehner kacken %s'%(_chunks.replace('\n','').replace('\r','')))
			self.canRetry=False
			return None
		if '403 Forbidden' in _chunks:
			self.updateProxy('proxy dead')
			self.dolog('proxy dead 403 %s'%(self.proxy))
			self.changeStatus('proxy blocked',self.current_farm_loop,0)
			self.lastError='proxy blocked'
			return None
		if 'Bad Gateway' in _chunks:
			self.updateProxy('bad gateway')
			if not self.isSummon:
				self.dolog('Bad Gateway %s'%(self.proxy))
				self.changeStatus('bad gateway',self.current_farm_loop,0)
				self.lastError='bad gateway'
				time.sleep(2)
				#self.error_repeat+=1
				return self.callApi(dtt,id)
			else:
				return None
		if 'SERVER_MSG_34' in _chunks and not self.isinject:
			self.dolog('SERVER_MSG_34')
			time.sleep(0.5)
			#self.error_repeat+=1
			return self.callApi(dtt,id)
		if r.status_code <>200:
			self.updateProxy('proxy dead')
			self.dolog('not 200')
			self.changeStatus('gumis server did not answer',self.current_farm_loop,0)
			self.lastError='no data from gumi'
			if not self.isSummon:
				time.sleep(2)
				self.error_repeat+=1
				return self.callApi(dtt,id)
			else:
				return None
		if '_MSG_' in _chunks or 'qrVcDe48' not in _chunks:
			#error_int=int(re.search('SERVER_MSG_([0-9*])',_error_str).group(1))
			#if error_int <=200:
			#print _chunks.replace('\r','').replace('\n','')
			self.changeStatus('we have some error',self.current_farm_loop,0)
			#self.dolog('baeren sind los %s'%(r.content.replace('\n','').replace('\r','')))
			return None#r.content.replace('\n','').replace('\r','')
		if 'SERVER_MSG_225' in _chunks:
			self.dolog('SERVER_MSG_225')
			self.FriendListRequest(1)
			return self.MissionEndRequest(qo3PECw6,_data)
		'''
		if '_MSG_' in r.content or 'qrVcDe48' not in r.content and not 'SERVER_MSG_24' in r.content:
			self.dolog('baeren sind los %s'%(r.content.replace('\n','').replace('\r','')))
			return r.content.replace('\n','').replace('\r','')
		'''
		plain_res=None
		try:
			if 't7n6cVWf' in _chunks:
				plain_res=self.t.decrypt(json.loads(_chunks)['t7n6cVWf']['qrVcDe48'],key)
		except:
			self.dolog('error beim decrypted')
			#time.sleep(2)
			#self.callApi(dtt,id,None,_data)
			#print 'sind noch da'
			time.sleep(0.5)
			return self.callApi(dtt,id,None,_data)
		if plain_res is None:
			self.dolog('das ende erreicht')
			return _chunks
		self.updateProxy(str(r.elapsed.total_seconds()))
		if 'c1qYg84Q' in plain_res and 'F_MST_VERSION' in plain_res and self.isMaster:
			self.dolog('updaten mst')
			self.updateMST(plain_res)
		if 'qrVcDe48' in plain_res:
			self.settings['qrVcDe48']=json.loads(plain_res)['QCcFB3h9'][0]['qrVcDe48']
		if 'LhVz6aD2' in plain_res:
			if 'm3Wghr1j' in plain_res:
				self.parseUserInfo(plain_res)
		if '1k3IefTc' in plain_res:
			self.parseFav(plain_res)
		if '3oU9Ktb7' in plain_res:
			self.parseUserData(plain_res)
			self.addAccountInfo(plain_res)
		if 'B71MekS8' in plain_res:
			self.parseMyUnits(plain_res)
		if 'pzf5se6V' in plain_res:
			self.parseMyFriends(plain_res)
		if '5Eb0Rig6' in plain_res:
			self.parseMyTeams(plain_res)
		if '8PEB5o7G' in plain_res:
			self.parseMyTeamSetup(plain_res)
		if 'Ur6CKS2e' in plain_res and len(json.loads(plain_res)['Ur6CKS2e'][0]['qo3PECw6'])>=1:
			self.RmRetireRequest(json.loads(plain_res)['Ur6CKS2e'][0]['qo3PECw6'])
		if 'W0E8BHa8' in plain_res and len(json.loads(plain_res)['W0E8BHa8'])>=1:
			self.parseUnlocked(plain_res)
		#if '1Ke2wFgm' in plain_res and len(json.loads(plain_res)['1Ke2wFgm'][0]['qo3PECw6'])>=1:
		#	self.startMission(json.loads(plain_res)['1Ke2wFgm'][0]['qo3PECw6'],True)
		try:
			json.loads(plain_res)
		except:
			self.dolog('bad json from gumi')
			return self.callApi(dtt,id)
		return plain_res

	def parseUnlocked(self,i):
		self.settings['user']['unlocked']={}
		self.settings['user']['unlocked']=json.loads(i)['W0E8BHa8']
		
	def isUnlocked(self,id):
		if 'unlocked' in self.settings['user']:
			id=str(id)
			for i in self.settings['user']['unlocked']:
				if i['vUCf4Rw3']==id and i['N6hVhvgf']=='1':
					return True
		return False
		
	def parseFav(self,data):
		if '1k3IefTc' in data and len(json.loads(data)['1k3IefTc'])>=1:
			try:
				self.settings['user']['fav']={}
				self.settings['user']['fav']=json.loads(data)['1k3IefTc'][0]['og2GHy49']
			except:
				pass
		
	def sellAll(self,stars):
		sum=0
		selling=[]
		for u in self.settings['units']:
			if self.settings['units'][u]['id'][-1]==str(stars) and self.settings['units'][u]['lvl']=='1':
				found=self.t.findUnitPrice(self.settings['units'][u]['id'])
				if found <>0:
					#print found,self.settings['units'][u]['id']
					sum+=int(found)
					#print u,self.settings['units'][u]
					selling.append(u)
		return self.UnitSellRequest(','.join(selling),sum)#B71MekS8 MILA
		
	def unfavAll(self):
		return self.UnitFavoriteRequest(self.settings['user']['fav'],'')
		
	def relog(self):
		self.InitializeRequest()
		self.GetUserInfoRequest()
		
	def parseMyFriends(self,raw):
		#self.dolog('%s() was called'%(self.whoami()))
		raw=self.byteify(raw)
		data=json.loads(raw)
		if 'pzf5se6V' in raw and len(data['pzf5se6V'])>=1:
			friends=data['pzf5se6V']
			for f in friends:
				if 'm3Wghr1j' in f and f['m3Wghr1j']:
					id=f['m3Wghr1j']
					self.settings['friends'][id]={}
					self.settings['friends'][id]['name']=f['9qh17ZUf'].encode('ascii','ignore')
					self.settings['friends'][id]['charid']=f['3HriTp6B']
					self.settings['friends'][id]['isfriend']=f['K3BV17gk']
		
	def GetBackgroundDownloadInfoRequest(self):
		data={}
		data.update(self.createBody())
		return self.callApi(data,'GetBackgroundDownloadInfoRequest')

	def GameSettingRequest(self):
		data={}
		data.update(self.createBody())
		return self.callApi(data,'GameSettingRequest')

	def InitializeRequest(self):
		data={}
		data.update(self.createBody(True))
		if self.isJapan:
			if hasattr(self,'P_USER_ID'):
				data['LhVz6aD2'][0]['9Tbns0eI']=self.P_USER_ID
				data['LhVz6aD2'][0]['6Nf5risL']=self.P_MODEL_CHANGE_CNT if hasattr(self,'P_MODEL_CHANGE_CNT') else '1'
		r= self.callApi(data,'InitializeRequest')
		if not r:
			self.changeStatus('can not load account',self.current_farm_loop,0)
			self.lastError='can not load account'
			return None
		t=json.loads(r)
		if 'c1qYg84Q' in t:
			for i in t['c1qYg84Q']:
				if i['a4hXTIm0']=='F_MST_VERSION':
					self.F_MST_VERSION=i['wM9AfX6I']
				if i['a4hXTIm0']=='F_RSC_VERSION':
					self.F_RSC_VERSION=i['wM9AfX6I']
		return r

	def CreateUserRequest(self):
		data={}
		data.update(self.createBody())
		return self.callApi(data,'CreateUserRequest')

	def LogShit(self,inp):
		if len(inp)<=1000:
			self.dolog('PRETTY FUCKED %s'%(inp.replace('\n','').replace('\r','')))

	def setAllUnits(self,_data):
		self.dolog('%s() was called'%(self.whoami()))
		if _data:
			if 'B71MekS8' in _data:
				self.settings['user']['units']=json.loads(_data)['B71MekS8']
				self.allUnits=len(self.settings['user']['units'])

	def getMyUnits(self):
		self.dolog('%s() was called'%(self.whoami()))
		return self.settings['user']['units']

	def getPASSWORD(self):
		return self.P_PASSWORD if hasattr(self,'P_PASSWORD') else None

	def getACCOUNT_ID(self):
		return self.P_ACCOUNT_ID if hasattr(self,'P_ACCOUNT_ID') else None

	def getMODEL_CHANGE_CNT(self):
		return self.P_MODEL_CHANGE_CNT if hasattr(self,'P_MODEL_CHANGE_CNT') else 0

	def GetUserInfoRequest(self):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		if 'ffbf' <> socket.gethostname():
			try:
				self.dolog('[+] our player id is %s:%s'%(self.settings['user']['m3Wghr1j'] if 'm3Wghr1j' in self.settings['user'] else 'NONE',self.settings['user']['9qh17ZUf']))
			except:
				pass
		tmp= self.callApi(data,'GetUserInfoRequest')
		if tmp:
			_tmp=json.loads(tmp)
			if 'c52MWCji' in tmp:# and 'D3fzIL1s' in tmp:
				if len(_tmp['LhVz6aD2'][0]['c52MWCji'])>=1:# and len(_tmp['LhVz6aD2'][0]['D3fzIL1s'])>=1:
					#self.P_PASSWORD=_tmp['LhVz6aD2'][0]['D3fzIL1s']
					self.P_ACCOUNT_ID=_tmp['LhVz6aD2'][0]['c52MWCji']
			if '6Nf5risL' in tmp:
				self.P_MODEL_CHANGE_CNT=_tmp['LhVz6aD2'][0]['6Nf5risL']
			if self.isFresh:
				self.completeTutorial(True)
				self.isFresh=False
			#self.FriendListRequest(1)
			self.setAllUnits(tmp)
			#self.FriendListRequest(1)
			if not self.isJapan:
				self.sgHomeMarqueeInfoRequest('en','hd')
			self.RoutineHomeUpdateRequest()
			self.RoutineWorldUpdateRequest()
		return tmp

	def RoutineHomeUpdateRequest(self):
		data={}
		data.update(self.createBody())
		return self.callApi(data,'RoutineHomeUpdateRequest')

	def RbEntryRequest(self):
		data={}
		data.update(self.createBody())
		return self.callApi(data,'RbEntryRequest')

	def ClsmEntryRequest(self):
		data={}
		data.update(self.createBody())
		return self.callApi(data,'ClsmEntryRequest')

	def UnitFavoriteRequest(self,mGuM1Z9e,v9Eb7m1NR):
		data={}
		data['R8U3uD1i']=[]
		data['R8U3uD1i'].append({'mGuM1Z9e':mGuM1Z9e,'9Eb7m1NR':str(v9Eb7m1NR)})
		data.update(self.createBody())
		return self.callApi(data,'UnitFavoriteRequest')

	def UnitSellRequest(self,S5Ib7En1,FBjo93gK):
		data={}
		data['Ray54PNQ']=[]
		data['Ray54PNQ'].append({'S5Ib7En1':S5Ib7En1,'FBjo93gK':str(FBjo93gK)})
		data.update(self.createBody())
		return self.callApi(data,'UnitSellRequest')

	def ItemSellRequest(self,v8X7LwE3r,v97h4mIQo):
		data={}
		data['2tHu3Chy']=[]
		data['2tHu3Chy'].append({'8X7LwE3r':v8X7LwE3r,'97h4mIQo':str(v97h4mIQo)})
		data.update(self.createBody())
		return self.callApi(data,'ItemSellRequest')

	def UnitMixRequest(self,WbGYcN17,B6H34Mea,v7UR4J2SE,UDMIFB72,og2GHy49):
		data={}
		data['f08du6EW']=[]
		data['f08du6EW'].append({'WbGYcN17':WbGYcN17,'B6H34Mea':str(B6H34Mea),'7UR4J2SE':str(v7UR4J2SE),'UDMIFB72':str(UDMIFB72),'og2GHy49':str(og2GHy49)})
		data.update(self.createBody())
		return self.callApi(data,'UnitMixRequest')

	def ClsmLotteryRequest(self,i5pd8xr3):
		data={}
		data['wPBq3it9']=[]
		data['wPBq3it9'].append({'VR3DuS2M':'0','i5pd8xr3':str(i5pd8xr3)})
		data.update(self.createBody())
		return self.callApi(data,'ClsmLotteryRequest')

	def sgMissionUnlockRequest(self,qo3PECw6):
		data={}
		data['ySFXhkpu']=[]
		data['ySFXhkpu'].append({'qo3PECw6':str(qo3PECw6)})
		data.update(self.createBody())
		return self.callApi(data,'sgMissionUnlockRequest')

	def ClsmStartRequest(self,i5pd8xr3):
		data={}
		data['wPBq3it9']=[]
		data['wPBq3it9'].append({'VR3DuS2M':'0','Jnt7cCV5':'0','i5pd8xr3':str(i5pd8xr3)})
		data.update(self.createBody())
		return self.callApi(data,'ClsmStartRequest')

	def ClsmEndRequest(self,i5pd8xr3,VR3DuS2M,_data):
		data={}
		data['wPBq3it9']=[]
		data['wPBq3it9'].append({'VR3DuS2M':str(VR3DuS2M),'i5pd8xr3':str(i5pd8xr3)})
		data['09HRWXDf']=self.build09HRWXDf(_data,i5pd8xr3,True)
		data['nSG9Jb1s']=self.buildnSG9Jb1s(_data,i5pd8xr3,True)
		data.update(self.createBody())
		return self.callApi(data,'ClsmEndRequest')

	def startCollos(self,i5pd8xr3):
		self.RbEntryRequest()
		self.ClsmEntryRequest()
		self.ClsmLotteryRequest(i5pd8xr3)
		if self.canCOrbs and int(self.settings['user']['xDm19iGS'])==0:
			self.dolog('[+] refilling collos orbs')
			self.ShopUseRequest(21,'')
		_startdata=self.ClsmStartRequest(i5pd8xr3)
		if _startdata:
			if '_MSG_' in _startdata or 'qrVcDe48' not in _startdata and not 'SERVER_MSG_24' in _startdata:
				self.LogShit(_startdata)
				return None,None
			self.dolog('[+] mission (%s) started'%(i5pd8xr3))
			_startdata_json=json.loads(_startdata)
			if self.isinject:
				sleeping=3
			elif 'win' not in sys.platform:
				sleeping=random.randint(15,30)
			else:
				sleeping=10
			time.sleep(sleeping)
			_mission_end_data=self.ClsmEndRequest(i5pd8xr3,2,_startdata_json)
			if _mission_end_data:
				if '_MSG_' in _mission_end_data or 'qrVcDe48' not in _mission_end_data and not 'SERVER_MSG_24' in _mission_end_data:
					self.LogShit(_mission_end_data)
					return None,None
				vd=self.checkReward(_mission_end_data,json.loads(_mission_end_data),i5pd8xr3)
				vi=self.checkTMR(_mission_end_data)
				vd=vd+vi+'[+] mission (%s) completed'%(i5pd8xr3)
				self.dolog('[+] mission (%s) completed'%(i5pd8xr3))
				return True,vd
		return None,None

	def TransferCodeIssueRequest(self,pasw):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		data['LhVz6aD2'][0]['D3fzIL1s']=pasw
		r= self.callApi(data,'TransferCodeIssueRequest')
		return json.loads(r)['LhVz6aD2'][0]['c52MWCji']
		
	def TransferCodeCheckRequest(self,ACCOUNT_ID,PASSWORD):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		data['LhVz6aD2'][0]['c52MWCji']=ACCOUNT_ID
		data['LhVz6aD2'][0]['D3fzIL1s']=PASSWORD
		return self.callApi(data,'TransferCodeCheckRequest')

	def TransferRequest(self,c52MWCji,D3fzIL1s):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		data['QCcFB3h9']=[]
		data['QCcFB3h9'].append({'qrVcDe48':''})
		data['LhVz6aD2'][0]['9Tbns0eI']=self.settings['user']['9Tbns0eI']
		data['LhVz6aD2'][0]['6Nf5risL']=self.settings['user']['6Nf5risL']
		data['LhVz6aD2'][0]['c52MWCji']=c52MWCji
		data['LhVz6aD2'][0]['D3fzIL1s']=D3fzIL1s
		return self.callApi(data,'TransferRequest')

	def getJpPlayerData(self,c52MWCji,D3fzIL1s):
		if not self.TransferCodeCheckRequest(c52MWCji,D3fzIL1s):
			self.lastError='login invalid'
			return None
		self.isStarter=True
		self.TransferRequest(c52MWCji,D3fzIL1s)
		self.isStarter=True
		
	def RoutineWorldUpdateRequest(self):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		return self.callApi(data,'RoutineWorldUpdateRequest')

	def LoginBonusRequest(self):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		return self.callApi(data,'LoginBonusRequest')

	def RoutineEventUpdateRequest(self):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data.update(self.createBody())
		return self.callApi(data,'RoutineEventUpdateRequest')

	def FriendListRequest(self,I40XmJV5):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['I53AVzSo']=[]
		data['I53AVzSo'].append({'I40XmJV5':str(I40XmJV5)})
		data.update(self.createBody())
		return self.callApi(data,'GetReinforcementInfoRequest')#MILA

	def PartyDeckEditRequest(self,Kgvo5JL2,fix=False):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['5Eb0Rig6']={}
		data['5Eb0Rig6']=self.settings['user']['teams']
		if 'beasts' in self.settings['user']:
			data['49rQB3fP']={}
			data['49rQB3fP']=self.settings['user']['beasts']
		data['CN92arJK']=[]
		if fix:
			data['CN92arJK'].append({'Kgvo5JL2':'0','MBIYc89Q':'0','Isc1ga3G':'0','igrz05CY':'0','r21y0YzS':'0'})
		else:
			data['CN92arJK'].append({'Kgvo5JL2':str(Kgvo5JL2),'MBIYc89Q':str(self.settings['user']['team']['MBIYc89Q']),'Isc1ga3G':str(self.settings['user']['team']['Isc1ga3G']),'igrz05CY':str(self.settings['user']['team']['igrz05CY']),'r21y0YzS':str(Kgvo5JL2)})
		data.update(self.createBody())
		return self.callApi(data,'PartyDeckEditRequest')

	def NoticeUpdateRequest(self,goAiX84L):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['p4U2NosZ']=[]
		data['p4U2NosZ'].append({'goAiX84L':goAiX84L})
		data.update(self.createBody())
		return self.callApi(data,'NoticeUpdateRequest')

	def FriendSearchRequest(self,m3Wghr1j):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['I53AVzSo']=[]
		data['I53AVzSo'].append({'m3Wghr1j':str(m3Wghr1j),'8zE6w9RP':'0'})
		data.update(self.createBody())
		res= json.loads(self.callApi(data,'FriendSearchRequest'))
		if len(res['2K05IxtX'])>=1:
			return json.dumps(res['2K05IxtX'][0])
		return None
		
	def summonUnits(self,X1IuZnj2,nqzG3b2v,v2RtVPS3b,zJ1A6HXm):
		res=self.GachaExeRequest(X1IuZnj2,nqzG3b2v,v2RtVPS3b,zJ1A6HXm)
		if not res:
			return None
		tmp=[]
		rj=json.loads(res)['5yLD4dYI']
		for u in rj:
			units=u['UJz5QED2'].split(',')
			for z in units:
				tmp.append(str(z.split(':')[1]))
		return tmp
		
	def GachaExeRequest(self,X1IuZnj2,nqzG3b2v,v2RtVPS3b,zJ1A6HXm):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['5yLD4dYI']=[]
		data['5yLD4dYI'].append(({'zJ1A6HXm':str(zJ1A6HXm),'nqzG3b2v':str(nqzG3b2v),'2RtVPS3b':str(v2RtVPS3b),'X1IuZnj2':str(X1IuZnj2)}))
		data.update(self.createBody())
		return self.callApi(data,'GachaExeRequest')

	def UpdateSwitchInfoRequest(self,dIPkNn61):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['0jqUZuT1']=[]
		data['0jqUZuT1'].append({'dIPkNn61':str(dIPkNn61)})
		data.update(self.createBody())
		return self.callApi(data,'UpdateSwitchInfoRequest')

	def ShopUseRequest(self,gdR2tJI9,Qy5EvcK1):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['L5Nj3cKE']=[]
		data['L5Nj3cKE'].append({'gdR2tJI9':gdR2tJI9,'Qy5EvcK1':Qy5EvcK1})
		data.update(self.createBody())
		return self.callApi(data,'ShopUseRequest')

	def RmRetireRequest(self,qo3PECw6):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['jQsE54Iz']=[]
		data['jQsE54Iz'].append({'0XUs3Tv6':'0','b6PwoB37':'0','7vh6LXEw':'0','qo3PECw6':str(qo3PECw6)})
		data.update(self.createBody())
		return self.callApi(data,'RmRetireRequest')

	def MissionWaveStartRequest(self,qo3PECw6):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['jQsE54Iz']=[]
		if self.canFriend and len(self.settings['friends'].keys())>=1:
			rnd_friend=random.choice(self.settings['friends'].keys())
			self.dolog('[+] friend %s:%s'%(rnd_friend,self.settings['friends'][rnd_friend]['name']))
			v0XUs3Tv6='5' if len(self.settings['friends'][rnd_friend]['isfriend'])==0 else '10'
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':str(v0XUs3Tv6),'xojJ2w0S':'0','w40YsHIz':rnd_friend,'qLke7K8f':self.settings['friends'][rnd_friend]['charid']})
			self.lastFriend=rnd_friend
			del self.settings['friends'][rnd_friend]
			if len(self.settings['friends'].keys())==0:
				self.FriendListRequest(1)
		else:
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':'0','xojJ2w0S':'0'})
		data.update(self.createBody())
		return self.callApi(data,'MissionWaveStartRequest')

	def MissionWaveReStartRequest(self,qo3PECw6):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['jQsE54Iz']=[]
		if self.canFriend and len(self.settings['friends'].keys())>=1:
			rnd_friend=random.choice(self.settings['friends'].keys())
			self.dolog('[+] friend %s:%s'%(rnd_friend,self.settings['friends'][rnd_friend]['name']))
			v0XUs3Tv6='5' if len(self.settings['friends'][rnd_friend]['isfriend'])==0 else '10'
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':str(v0XUs3Tv6),'xojJ2w0S':'0','w40YsHIz':rnd_friend,'qLke7K8f':self.settings['friends'][rnd_friend]['charid']})
			self.lastFriend=rnd_friend
			del self.settings['friends'][rnd_friend]
			if len(self.settings['friends'].keys())==0:
				self.FriendListRequest(1)
		else:
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':'0','xojJ2w0S':'0'})
		data.update(self.createBody())
		return self.callApi(data,'MissionWaveReStartRequest')

	def MissionStartRequest(self,qo3PECw6):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['jQsE54Iz']=[]
		if self.canFriend and len(self.settings['friends'].keys())>=1:
			rnd_friend=random.choice(self.settings['friends'].keys())
			self.dolog('[+] friend %s:%s'%(rnd_friend,self.settings['friends'][rnd_friend]['name']))
			v0XUs3Tv6='5' if len(self.settings['friends'][rnd_friend]['isfriend'])==0 else '10'
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':str(v0XUs3Tv6),'xojJ2w0S':'0','w40YsHIz':rnd_friend,'qLke7K8f':self.settings['friends'][rnd_friend]['charid']})
			self.lastFriend=rnd_friend
			del self.settings['friends'][rnd_friend]
			if len(self.settings['friends'].keys())==0:
				self.FriendListRequest(1)
		else:
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':'0','xojJ2w0S':'0'})
		data.update(self.createBody())
		return self.callApi(data,'MissionStartRequest')

	def MissionReStartRequest(self,qo3PECw6):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['jQsE54Iz']=[]
		if self.canFriend and len(self.settings['friends'].keys())>=1:
			rnd_friend=random.choice(self.settings['friends'].keys())
			self.dolog('[+] friend %s:%s'%(rnd_friend,self.settings['friends'][rnd_friend]['name']))
			v0XUs3Tv6='5' if len(self.settings['friends'][rnd_friend]['isfriend'])==0 else '10'
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':str(v0XUs3Tv6),'xojJ2w0S':'0','w40YsHIz':rnd_friend,'qLke7K8f':self.settings['friends'][rnd_friend]['charid']})
			self.lastFriend=rnd_friend
			del self.settings['friends'][rnd_friend]
			if len(self.settings['friends'].keys())==0:
				self.FriendListRequest(1)
		else:
			data['jQsE54Iz'].append({'qo3PECw6':str(qo3PECw6),'0XUs3Tv6':'0','xojJ2w0S':'0'})
		data.update(self.createBody())
		return self.callApi(data,'MissionReStartRequest')

	def mergeChests(self,new):
		self.dolog('%s() was called'%(self.whoami()))
		self.settings['openedChests'].extend(new)
		
	def DungeonResourceLoadMstListRequest(self,id):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['1zTjkp5B']=[]
		data['1zTjkp5B'].append({'6uIYE15X':str(id),'89EvGKHx':'0'})
		data.update(self.createBody())
		return self.callApi(data,'DungeonResourceLoadMstListRequest')
		
	def MissionEndRequest(self,qo3PECw6,_data):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['L4i4418y']=[]
		data['L4i4418y'].append({'6q35TL07':'0'})
		data['jQsE54Iz']=[{}]
		data['jQsE54Iz'][0]['qo3PECw6']=str(qo3PECw6)
		if self.canFriend and len(self.settings['friends'].keys())>=1:
			data['jQsE54Iz'][0]['w40YsHIz']=str(self.lastFriend)
		elif self.canFriend and len(self.settings['friends'].keys())==0:
			self.FriendListRequest(1)
			return self.MissionEndRequest(qo3PECw6,_data)
		data['2urzfX6d']=[]
		_2=self.build2urzfX6d(_data,qo3PECw6)
		data['2urzfX6d'].append(_2 if _2 else {'Z1p0j9uF':'0'})
		data['09HRWXDf']=self.build09HRWXDf(_data,qo3PECw6)
		data['nSG9Jb1s']=self.buildnSG9Jb1s(_data,qo3PECw6)
		if self.settings['user']['ach'] and len(self.settings['user']['ach'])>=1:
			data['nSG9Jb1s']={}
			data['nSG9Jb1s']=self.settings['user']['ach']
		if self.canChest and self.t.findMissionType(qo3PECw6) == 2:
			data['jQsE54Iz'][0]['dIPkNn61']=','.join(self.settings['openedChests'])
		data.update(self.createBody())
		return self.callApi(data,'MissionEndRequest')#,qo3PECw6,_data)

	def sgHomeMarqueeInfoRequest(self,KmgMTuj5,v3a162M47):
		self.dolog('%s() was called'%(self.whoami()))
		data={}
		data['yJjS7dKX']=[]
		data['yJjS7dKX'].append({'KmgMTuj5':KmgMTuj5})
		data['H6o3079i']=[]
		data['H6o3079i'].append({'3a162M47':v3a162M47})
		data.update(self.createBody())
		return self.callApi(data,'sgHomeMarqueeInfoRequest')

	def setACH(self,data):
		self.dolog('%s() was called'%(self.whoami()))
		self.settings['user']['ach']={}
		self.settings['user']['ach']=data
		
	def startMission_(self,id,reenter=False,cnt=0):
		need_unlock=[9200001,9200002,9200003,9210001,9210002,9210003]
		self.dolog('%s() was called'%(self.whoami()))
		id=int(id)
		if id in need_unlock:
			if not self.isUnlocked(id):
				res=self.sgMissionUnlockRequest(id)
				if not res:
					return None,None
		_mission_name=self.t.findMissionName(id)
		self.dolog('[+] mission %s (%s) started'%(_mission_name,id))
		_ms_type=self.t.findMissionType(int(id))
		_ecost=self.t.findMissionCost(int(id))
		self.mission_rounds=self.t.findMissionRound(int(id))#MILA
		if self.canRefill and int(self.settings['user']['7wV3QZ80'])>8 and _ecost>self.settings['user']['current_energy']:
			self.dolog('[+] refilling energy')
			self.ShopUseRequest(20,'')
		if self.canOrbs and int(self.settings['user']['Ddsg1be4'])==0:
			self.dolog('[+] refilling orbs')
			self.ShopUseRequest(22,'')
		if _ms_type == 2:
			if reenter:
				_mission_data=self.MissionReStartRequest(id)
			else:
				_mission_data=self.MissionStartRequest(id)
		else:
			if reenter:
				_mission_data=self.MissionWaveReStartRequest(id)
			else:
				_mission_data=self.MissionWaveStartRequest(id)
		if _mission_data:
			if 'R_MSG_' in _mission_data or 'qrVcDe48' not in _mission_data and not 'SERVER_MSG_24' in _mission_data:
				self.LogShit(_mission_data)
				return None,None
			self.DungeonResourceLoadMstListRequest(id)
			if self.isinject:
				sleeping=3
			elif 'win' not in sys.platform:
				sleeping=random.randint(15,30)
			else:
				sleeping=10
			time.sleep(sleeping)
			_mission_end_data=self.MissionEndRequest(id,json.loads(_mission_data))
			if _mission_end_data:
				if 'R_MSG_' in _mission_end_data or 'qrVcDe48' not in _mission_end_data and not 'SERVER_MSG_24' in _mission_end_data:
					self.LogShit(_mission_end_data)
					return None,None
				vd=self.checkReward(_mission_end_data,json.loads(_mission_end_data),id)
				vi=self.checkTMR(_mission_end_data)
				vd=vd+vi
				self.dolog('[+] mission %s (%s) completed'%(_mission_name,id))
				return True,vd
		if cnt <=3 and self.canRetry:
			self.dolog('fuck gumi %s'%(cnt))
			time.sleep(2)
			return self.startMission(id,reenter,cnt+1)
		self.dolog('[+] line 691 wtf')
		self.dolog(self.getLastError())
		return None,None

	def startMission(self,id,reenter=False,cnt=0):
		#if self.isJapan:
		#	self.TransferCodeIssueRequest('ApplePass')
		if ',' in str(id):
			id = id.split(',')
			res=[]
			for _m in id:
				r=self.startMission_(_m,reenter,cnt)
				if r:
					if r[0]:
						res.append(r[1])
			return [True,'\n'.join(res)]
		else:
			return self.startMission_(id,reenter,cnt)						

	def parseMyTeams(self,data):
		#self.dolog('%s() was called'%(self.whoami()))
		self.settings['user']['teams']={}
		self.settings['user']['teams']=json.loads(data)['5Eb0Rig6']
		if '49rQB3fP' in data:
			self.settings['user']['beasts']={}
			self.settings['user']['beasts']=json.loads(data)['49rQB3fP']

	def parseMyTeamSetup(self,data):
		#self.dolog('%s() was called'%(self.whoami()))
		self.settings['user']['team']={}
		self.settings['user']['team']=json.loads(data)['8PEB5o7G'][0]
		
	def parseMyUnits(self,data):
		#self.dolog('%s() was called'%(self.whoami()))
		_units={}
		B71MekS8=json.loads(data)['B71MekS8']
		for unit in B71MekS8:
			if 'f17L8wuX' in unit:
				f17L8wuX=unit['f17L8wuX']#tmr
				og2GHy49=unit['og2GHy49']#id
				Z06cK4Qi=unit['3HriTp6B']#charid
				lvl=unit['7wV3QZ80']
				if int(Z06cK4Qi)>=900000000:
					pass
				if og2GHy49 in _units:
					pass
				else:
					_units[og2GHy49]={}
					_units[og2GHy49]['tmr']=f17L8wuX
					_units[og2GHy49]['id']=Z06cK4Qi
					_units[og2GHy49]['lvl']=lvl
		self.settings['units']=_units

	def checkReward(self,_data,_json,id):
		#self.dolog('%s() was called'%(self.whoami()))
		if _data:
			reward_string=''
			if '09HRWXDf' in _data:
				_reward_table=_json['09HRWXDf'][0]
				possible=['xF9Sr1a6','JHMit30L','Sp7fF6I9','02aARqrv','Z7G0yxXe','EWmQy52k','V1X7tjBv','REB5tAL9','81fnjKLw','3imo7rf4','Iyx9Bos7','VZ8DSco1','Mh1BA4uv','XMgu7qE0','04yIhXME','Ym8F0ndw','34pqHBIC','0w6yHTEz','E6kmo39Q','ypU1T0kR','30u6XYiB','1Z2TD5ai','JmUQ5Kf7','ERJa3SL5','Z6yB9eYd','aqH0nm3Y','3ueDCf8Y','2LqvowY8','95JxZzuG','7rA9WGQe','pbX64czP','9ibA0nq4','R1kg3EBA','2U05aV9Z','Vy9YXBE7']
				for i in possible:
					if i in _data and len(_reward_table[i])>=1:
						reward_string=reward_string+','+self.getRewardString(_reward_table[i])
				if len(reward_string)>=1:
					if reward_string[0] == ',':
						reward_string=reward_string[1:]
				self.addLoot()
				reward_string='[+] mission %s completed\n[+] unit exp %s\n[+] rank exp %s/%s, level %s\n[+] reward %s\n[+] energy left %s/%s\n[+] gil %s'%(self.t.findMissionName(id),_reward_table['S4U09svH'],self.settings['user']['B6H34Mea'],self.t.findLevelExp(int(self.settings['user']['7wV3QZ80'])),self.settings['user']['7wV3QZ80'],reward_string,self.settings['user']['B6kyCQ9M'],_json['3oU9Ktb7'][0]['m0bD2zwU'],_json['3oU9Ktb7'][0]['7UR4J2SE'])
			return reward_string
		
	def checkTMR(self,data):
		#self.dolog('%s() was called'%(self.whoami()))
		changes=[]
		if '8gSkPD6b' in data:
			v8gSkPD6b=json.loads(data)['8gSkPD6b']
			for unit in v8gSkPD6b:
				og2GHy49=unit['og2GHy49']#charid
				Z06cK4Qi=unit['Z06cK4Qi']#char id for name
				f17L8wuX=unit['f17L8wuX']#tmr
				if og2GHy49 in self.settings['units']:
					if f17L8wuX <> self.settings['units'][og2GHy49]['tmr']:
						changes.append('%s %s%%'%(self.t.findUnitName(Z06cK4Qi)[0],float(f17L8wuX)/1000 * 100))
						if 'win' not in sys.platform:
							self.addTMR(og2GHy49,f17L8wuX,self.t.findUnitName(Z06cK4Qi)[0])
						self.settings['units'][og2GHy49]['tmr']=f17L8wuX
		if len(changes)>=1:
			return '\n[+] tmr changes %s'%(','.join(changes))
		else:
			return ''

	def buildnar74pDu(self,data):
		res=[]
		if 'wbet57nF' in data:
			for i in data['wbet57nF']:
				res.append(i['V9j8wJcC'])
		return ','.join(sorted(res))

	def buildf6M1cJgk(self,data):
		res=[]
		rit={}
		if 'y35YvQjZ' in data:
			for i in data['y35YvQjZ']:
				j=i['xqartN26']
				if j in rit:
					rit[j]['count']+=1
				else:
					rit[j]={}
					rit[j]['count']=1
		if 'wbet57nF' in data:
			for i in data['wbet57nF']:
				j=i['xqartN26']
				if j in rit:
					rit[j]['count']+=1
				else:
					rit[j]={}
					rit[j]['count']=1
		if '6v0LPiRe1' in data:
			for i in data['6v0LPiRe']:
				j=i['xqartN26']
				if j in rit:
					rit[j]['count']+=1
				else:
					rit[j]={}
					rit[j]['count']=1
		for e in rit:
			res.append('%s:%s'%(e,rit[e]['count']))
		return ','.join(sorted(res))

	def builduU21m4ry(self,data):
		if 'wbet57nF' not in data:
			return ''
		res=[]
		for i in data['wbet57nF']:
			res.append('%s:1'%(i['xqartN26']))
		return ','.join(sorted(res))

	def build6v0LPiRe(self,data):
		t={}
		p=[]
		if 'y35YvQjZ' in data:
			y35YvQjZ=data['y35YvQjZ']
			for i in y35YvQjZ:
				if '9BetM2Ds' in i and i['9BetM2Ds']:
					j=i['9BetM2Ds'].split(':')
					o='%s:%s'%(j[0],j[1])
					if o in t:
						t[o]['count']+=int(j[2])
					else:
						t[o]={}
						t[o]['count']=int(j[2])
				if 'MZn8LC6H' in i and i['MZn8LC6H']:
					j=i['MZn8LC6H'].split(':')
					o='%s:%s'%(j[0],j[1])
					if o in t:
						t[o]['count']+=int(j[2])
					else:
						t[o]={}
						t[o]['count']=int(j[2])
		if '6v0LPiRe' in data:
			v6v0LPiRe=data['6v0LPiRe']
			for i in v6v0LPiRe:
				if '9BetM2Ds' in i and i['9BetM2Ds']:
					j=i['9BetM2Ds'].split(':')
					o='%s:%s'%(j[0],j[1])
					if o in t:
						t[o]['count']+=int(j[2])
					else:
						t[o]={}
						t[o]['count']=int(j[2])
				if 'MZn8LC6H' in i and i['MZn8LC6H']:
					j=i['MZn8LC6H'].split(':')
					o='%s:%s'%(j[0],j[1])
					if o in t:
						t[o]['count']+=int(j[2])
					else:
						t[o]={}
						t[o]['count']=int(j[2])
		if 'JR7jZci2' in data:
			JR7jZci2=data['JR7jZci2']
			for i in JR7jZci2:
				if '9BetM2Ds' in i and i['9BetM2Ds']:
					j=i['9BetM2Ds'].split(':')
					o='%s:%s'%(j[0],j[1])
					if o in t:
						t[o]['count']+=int(j[2])
					else:
						t[o]={}
						t[o]['count']=int(j[2])
				if 'MZn8LC6H' in i and i['MZn8LC6H']:
					j=i['MZn8LC6H'].split(':')
					o='%s:%s'%(j[0],j[1])
					if o in t:
						t[o]['count']+=int(j[2])
					else:
						t[o]={}
						t[o]['count']=int(j[2])
		for e in t:
			if e:
				e_=e.split(':')
				p.append('%s:%s:%s'%(e_[0],e_[1],t[e]['count']))
		if len(p)==0:
			return ''
		return ','.join(p)
		
	def buildSp7fF6I9(self,data):
		if 'bV34YIJQ' not in data:
			return ''
		bV34YIJQ=data['bV34YIJQ']
		Bi6hVv34=data['Bi6hVv34']
		res=[]
		rit={}
		unt={}
		for i in Bi6hVv34:
			j=i['xqartN26']
			if j in unt:
				unt[j]['count']+=1
			else:
				unt[j]={}
				unt[j]['count']=1
		for i in bV34YIJQ:
			mlt=unt[i['xqartN26']]['count']
			if '9BetM2Ds' in i and i['9BetM2Ds']:
				j=i['9BetM2Ds'].split(',')
				for u in j:
					z=u.split(':')
					o='%s:%s'%(z[0],z[1])
					if o in rit:
						rit[o]['count']+=int(z[2])*mlt
					else:
						rit[o]={}
						rit[o]['count']=int(z[2])*mlt
			if '3frn4ILX' in i and i['3frn4ILX']:
				j=i['3frn4ILX'].split(',')
				for u in j:
					z=u.split(':')
					o='%s:%s'%(z[0],z[1])
					if o in rit:
						rit[o]['count']+=int(z[2])*mlt
					else:
						rit[o]={}
						rit[o]['count']=int(z[2])*mlt
		for e in rit:
			res.append('%s:%s'%(e,rit[e]['count']))
		if len(res)==0:
			return ''
		return ','.join(sorted(res,key = lambda x: x.split(':')[1]))

	def rndI(self,min,max):
		return str(random.randint(min,max))

	def buildnSG9Jb1s(self,data,id,colloeseum=False):
		res=[]
		dmg=self.getMaxDMG(data)
		dmg = int(dmg * random.uniform(1, 2))
		if colloeseum:
			res.append({'NYb0Cri6':'CLSM_TOTAL_DAMAGE','6gAX1BpC':str(dmg)})
			res.append({'NYb0Cri6':'CLSM_MAX_DAMAGE_TURN','6gAX1BpC':str(dmg)})
		else:
			res.append({'NYb0Cri6':'MAX_DAMAGE_TURN','6gAX1BpC':str(dmg)})
			res.append({'NYb0Cri6':'TOTAL_DAMAGE','6gAX1BpC':str(dmg)})
			#res.append({'NYb0Cri6':'MAX_DAMAGE_HIT','6gAX1BpC':self.rndI(1000,100000)})
			#res.append({'NYb0Cri6':'MAX_SPARK_CHAIN_TURN','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'TOTAL_CRITICAL','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'MAX_CRITICAL_TURN','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'TOTAL_MAGIC_USE','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'TOTAL_ABILITY_USE','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'TOTAL_LB_CRISTAL','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'MAX_ELEMENT_CHAIN_TURN','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'MAX_CHAIN_TURN','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'MAX_LB_CRISTAL','6gAX1BpC':self.rndI(1,100)})
			#res.append({'NYb0Cri6':'TOTAL_BEAST_USE','6gAX1BpC':self.rndI(1,100)})
			if self.mission_rounds>=1:
				res.append({'NYb0Cri6':'TOTAL_MISSION_BATTLE_WIN','6gAX1BpC':str(self.mission_rounds)})
			else:
				res.append({'NYb0Cri6':'TOTAL_STEPS','6gAX1BpC':str(randint(1000,10000))})
		return res
		
	def getMaxDMG(self,data):
		total=0
		if 'bV34YIJQ' in data:
			bV34YIJQ=data['bV34YIJQ']
			for unt in bV34YIJQ:
				if 'fh31sk7B' in unt:
					fh31sk7B=unt['fh31sk7B']
					total+=int(fh31sk7B)
		return total
		
	def build09HRWXDf(self,data,id,colloeseum=False):
		res={}
		res['Wdi3MAs2']=str(randint(200000,900000)) if not colloeseum else str(randint(0,200))
		res['Syar71nw']='0'
		res['nar74pDu']=self.buildnar74pDu(data)
		res['8CfoLQv5']='0'
		res['f6M1cJgk']=self.buildf6M1cJgk(data)
		res['Sp7fF6I9']=self.buildSp7fF6I9(data) if self.canLoot else ''
		if not colloeseum:
			res['S4U09svH']=str(randint(200000,900000))
			res['ZGSr7T06']='0'
			res['wQhu9G7n']='0'
			res['xF9Sr1a6']=self.build6v0LPiRe(data) if self.canLoot else ''
			res['7a1Ugx4e']='0'
			res['t4v2o0zM']='0'
			res['PB3vLE2r']='0'
			res['aK4k1PvY']='0'
			res['NCFk6Zv1']='0'
			res['A90DrNfp']=self.buildA90DrNfp(data) if self.lb >0 else ''
			res['R1kg3EBA']=self.buildR1kg3EBA(data) if self.canChest else ''
			res['Mh1BA4uv']=self.buildMh1BA4uv(data) if self.canChest else ''
			res['Z7G0yxXe']=self.buildZ7G0yxXe(data) if self.canChest else ''
			res['EWmQy52k']=self.buildEWmQy52k(data) if self.canELoot else ''
			res['2U05aV9Z']=self.buildJR7jZci2(data) if self.canUnits else ''
			res['uU21m4ry']=self.builduU21m4ry(data)
			res['V59rxm82']=self.buildV59rxm82(data)
			if False:#INJECTION MILA
				pass
				#res['9ibA0nq4']='23:180:10'#P_IMPORTANT_ITEM_REWARD yes?
				#res['3js9MxiK']='23:180:10'#P_IMPORTNT_ITEM_REWARD
			if self.doEquipInj:
				res['Ym8F0ndw']=self.doEquipInj
				self.doEquipInj=None
			if self.doItemInj:
				res['REB5tAL9']=self.doItemInj
				self.doItemInj=None
			if self.doMateriaInj:
				res['ERJa3SL5']=self.doMateriaInj
				self.doMateriaInj=None
		return [res]

	def setInjectEquip(self,l,count):
		self.setIsInject()
		tmp=[]
		for i in l:
			tmp.append('21:%s:%s'%(i,count))
		self.doEquipInj= ','.join(tmp)
		
	def setInjectItem(self,l,count):
		self.setIsInject()
		tmp=[]
		for i in l:
			tmp.append('20:%s:%s'%(i,count))
		self.doItemInj= ','.join(tmp)
		
	def setInjectMateria(self,l,count):
		self.setIsInject()
		tmp=[]
		for i in l:
			tmp.append('22:%s:%s'%(i,count))
		self.doMateriaInj= ','.join(tmp)

	def solveMission(self,id):
		#self.dolog('%s() was called'%(self.whoami()))
		try:
			res={}
			clgs=self.t.getChallenges(int(id))
			if clgs:
				for m in clgs:
					q=clgs[m].split(',')
					for p in q:
						w=p.split(':')
						w[0]=int(w[0])
						if w[0]==68:#fin quest DONE
							pass
						elif w[0]==33:#no ko DONE
							pass
						elif w[0]==35:#party x less DONE
							pass
						elif w[0]==34:#party x more DONE
							pass
						elif w[0]==38:#no continue DONE
							pass
						elif w[0]==0:#use item DONE
							res['4p6CrcGt']='101000100:1'
						elif w[0]==1:#no items DONE
							pass
						elif w[0]==45:#evoke x more DONE
							res['9JBtk2LE']='1:%s'%(int(w[1])+1)
						elif w[0]==17:#lb unused DONE
							pass
						elif w[0]==16:#use lb DONE
							res['s2rX7g0o']='100000202:1'
						elif w[0]==6:#no magic DONE
							pass
						elif w[0]==5:#use magic DONE
							if 'i1yJ3hmT' in res:
								res['i1yJ3hmT']+=',30090:1'
							else:
								res['i1yJ3hmT']='30090:1'
						elif w[0]==28:#use esper DONE
							res['9JBtk2LE']='1:1'
						elif w[0]==41:#use magic x time DONE
							if 'i1yJ3hmT' in res:
								res['i1yJ3hmT']+=',30090:%s'%(int(w[1])+1)
							else:
								res['i1yJ3hmT']='30090:%s'%(int(w[1])+1)#20010 MILA
						elif w[0]==26:#deal x damage DONE
							if 'qr5PoZ1W' in res:
								res['qr5PoZ1W']+= ',%s:1'%(w[1])
							else:
								res['qr5PoZ1W']= '%s:1'%(w[1])
						elif w[0]==49:#use more x lb DONE
							res['s2rX7g0o']='100000202:%s'%(int(w[1])+1)
						elif w[0]==7:#use x abiltiy DONE
							if 'i1yJ3hmT' in res:
								res['i1yJ3hmT']+=',%s:1'%(w[1])
							else:
								res['i1yJ3hmT']='%s:1'%(w[1])
						elif w[0]==21:#use x ability DONE
							res['Pqi5r1TZ']='%s:1'%(w[1])
						elif w[0]==13:#use x magic DONE
							if int(w[1])==2:
								if 'i1yJ3hmT' in res:
									res['i1yJ3hmT']+= ',20190:1'
								else:
									res['i1yJ3hmT']= '20190:1'
							elif int(w[1])==1:
								if 'i1yJ3hmT' in res:
									res['i1yJ3hmT']+= ',10060:1'
								else:
									res['i1yJ3hmT']= '10060:1'
							elif int(w[1])==3:
								if 'i1yJ3hmT' in res:
									res['i1yJ3hmT']+= ',30010:1'
								else:
									res['i1yJ3hmT']= '30010:1'
						elif w[0]==30:#evoke x DONE
							if '9JBtk2LE' in res:
								res['9JBtk2LE']+=',%s:1'%(w[1])
							else:
								res['9JBtk2LE']='%s:1'%(w[1])
						elif w[0]==12:#no x magic DONE
							pass
						elif w[0]==14:#magic unused DONE
							pass
						elif w[0]==40:#less x items DONE
							pass
						elif w[0]==36:#x in party
							pass
						elif w[0]==29:#no esper DONE
							pass
						elif w[0]==18:#kill boss with lb DONE
							res['73CfbLEx']='%s@%s:1@5:100000102'%(w[1],w[2])
						elif w[0]==15:#kill boss with magic DONE
							res['73CfbLEx']='%s@%s:1@2:20020'%(w[1],w[2])
						elif w[0]==59:#deal x x times DONE
							#res['qr5PoZ1W']= '%s:%s'%(w[1],int(w[2])+1)
							if 'qr5PoZ1W' in res:
								res['qr5PoZ1W']+=',%s:%s'%(w[1],int(w[2])+1)
							else:
								res['qr5PoZ1W']='%s:%s'%(w[1],int(w[2])+1)
						elif w[0]==32:#kill boss with esper DONE
							res['73CfbLEx']='%s@%s:1@3:1'%(w[1],w[2])
						elif w[0]==20:#no abiltity DONE
							pass
						elif w[0]==2:#use x item DONE
							res['4p6CrcGt']='%s:1'%(w[1])
						elif w[0]==23:#kill boss with ability
							pass
						elif w[0]==4:#kill boss with item
							pass
						elif w[0]==75:#clear within x turns DONE
							pass
						elif w[0]==77:#kill x within turns DONE
							pass
						elif w[0]==1000:#clear within x sec
							res['7TyWeg0H']='%s'%(int(w[1])-1)
						else:
							self.dolog('dont know %s for %s'%(w,id))#m,a,w
							pass
				return res
			else:
				return None
		except: 
			return None

	def buildMh1BA4uv(self,data):
		p=[]
		c=[]
		if 'pDFgB3i0' in data:
			pDFgB3i0=data['pDFgB3i0']
			for r in pDFgB3i0:
				if 'NiG2wL3A' in r and 'dIPkNn61' in r and r['dIPkNn61'] and r['NiG2wL3A']:# and (int(r['dIPkNn61'])<=50000000):
					w=r['NiG2wL3A'].split(':')
					if int(w[0]) == 21:
						o='%s:%s:%s:%s'%(w[0],w[1],w[2],r['dIPkNn61'])
						c.append(r['dIPkNn61'])
						p.append(o)
		if len(p)==0:
			return ''
		self.mergeChests(c)
		return ','.join(p)

	def buildZ7G0yxXe(self,data):
		p=[]
		c=[]
		if 'pDFgB3i0' in data:
			pDFgB3i0=data['pDFgB3i0']
			for r in pDFgB3i0:
				if 'NiG2wL3A' in r and 'dIPkNn61' in r and r['dIPkNn61'] and r['NiG2wL3A']:# and (int(r['dIPkNn61'])<=50000000):
					w=r['NiG2wL3A'].split(':')
					if int(w[0]) == 20:
						o='%s:%s:%s:%s'%(w[0],w[1],w[2],r['dIPkNn61'])
						c.append(r['dIPkNn61'])
						p.append(o)
		if len(p)==0:
			return ''
		self.mergeChests(c)
		return ','.join(p)
		
	def buildR1kg3EBA(self,data):
		p=[]
		c=[]
		if 'pDFgB3i0' in data:
			pDFgB3i0=data['pDFgB3i0']
			for r in pDFgB3i0:
				if 'NiG2wL3A' in r and 'dIPkNn61' in r and r['dIPkNn61'] and r['NiG2wL3A']:# and (int(r['dIPkNn61'])<=50000000):
					w=r['NiG2wL3A'].split(':')
					if int(w[0]) == 60:
						o='%s:%s:%s:%s'%(w[0],w[1],w[2],r['dIPkNn61'])
						c.append(r['dIPkNn61'])
						p.append(o)
		if len(p)==0:
			return ''
		self.mergeChests(c)
		return ','.join(p)

	def buildV59rxm82(self,data):
		res=[]
		if '6v0LPiRe' in data:
			for i in data['6v0LPiRe']:
				res.append('10:%s:%s'%(i['2fY1IomW'],i['h4Sjf96p']))
		if 'YjHhvN65' in data:
			for i in data['YjHhvN65']:
				res.append('0:%s:%s'%(i['2fY1IomW'],i['i2ar9yXM']))
		if len(res)==0:
			return ''
		return ','.join(sorted(res))
	
	def buildEWmQy52k(self,data):
		r=[]
		t={}
		if 'vM21k0do' in data:
			vM21k0do=data['vM21k0do']
			for i in vM21k0do:
				if '1Fa7rL5R' in i and i['1Fa7rL5R']:
					o=i['1Fa7rL5R'].split(':')
					z='%s:%s'%(o[0],o[1])
					if z in t:
						t[z]['count']+=int(o[2])
					else:
						t[z]={}
						t[z]['count']=int(o[2])
			for i in t:
				r.append('%s:%s'%(i,t[i]['count']))
		return ','.join(r)
	
	def buildJR7jZci2(self,data):
		r=[]
		t={}
		if 'y35YvQjZ' in data:
			y35YvQjZ=data['y35YvQjZ']
			for i in y35YvQjZ:
				if 'Vf5DGw07' in i and i['Vf5DGw07']:
					r.append(str(i['Vf5DGw07']))
		if 'JR7jZci2' in data:
			JR7jZci2=data['JR7jZci2']
			for i in JR7jZci2:
				if 'Vf5DGw07' in i and i['Vf5DGw07']:
					r.append(str(i['Vf5DGw07']))
		if 'bV34YIJQ' in data:
			bV34YIJQ=data['bV34YIJQ']
			for i in bV34YIJQ:
				if 'Vf5DGw07' in i and i['Vf5DGw07']:
					r.append(str(i['Vf5DGw07']))
		return ','.join(r)

	def build2urzfX6d(self,data,qo3PECw6):
		t={}
		p=[]
		p2=[]
		_rr={}
		if self.canSolve:
			_r=self.solveMission(qo3PECw6)
			if _r:
				_rr.update(_r)
		'''
		p.sort(key = lambda x: x.split(':')[0])
		'''
		if 'y35YvQjZ' in data:
			for i in data['y35YvQjZ']:
				if '6v7y3QcJ' in i and i['6v7y3QcJ']:
					_str='%s:%s:%s'%(i['6v7y3QcJ'],i['2fY1IomW'],i['6Yc4RkdM'])
					if _str not in p:
						p.append(_str)
		if 'wbet57nF' in data:
			for i in data['wbet57nF']:
				if '2fY1IomW' in i and i['2fY1IomW']:
					_str='%s:0:0'%(i['2fY1IomW'])
					p2.append(_str)
		p.sort()
		_rr['69ieJGhD']=','.join(p)#P_TURN_INFO
		_rr['Z1p0j9uF']='0'#P_UNIT_DEAD_CNT
		_rr['vMo5cnmx']=','.join(p2)#P_MONSTER_DATA
		return _rr

	def buildA90DrNfp(self,data):#MILA
		tmp=[]
		for u in self.settings['units']:
			tmp.append('%s:%s'%(u,self.lb))
		return ','.join(tmp)
		
	def getRewardString(self,io):
		self.dolog('%s() was called'%(self.whoami()))
		r=[]
		if '@' in io:
			rewards=io.split(',')
			for e in rewards:
				try:
					w=e.split('@')
					if len(w)==3:
						reward=w[1].split(':')
						if len(reward)==4:
							self.dropped_stuff.append((reward[1],reward[2]))
							#self.addLoot(reward[1],reward[2])
							r.append('%s x%s'%(self.t.findItemName(reward[1]),reward[2]))
				except:
					pass
		else:
			rewards = io.split(',')
			for reward in rewards:
				try:
					if reward:
						reward= reward.split(':')
						self.dropped_stuff.append((reward[1],reward[2]))
						#self.addLoot(reward[1],reward[2])
						r.append('%s x%s'%(self.t.findItemName(reward[1]),reward[2]))
				except:
					pass
		return ','.join(r)
		
	def TUTGL(self):
		self.dolog('%s() was called'%(self.whoami()))
		self.FriendListRequest(1)
		self.RoutineHomeUpdateRequest()
		self.sgHomeMarqueeInfoRequest('en','sd')
		print self.startMission(1110100)[1]
		print self.startMission(1110101)[1]
		self.FriendListRequest(0)
		print self.startMission(1110103)[1]
		self.FriendListRequest(0)
		self.UpdateSwitchInfoRequest('')
		self.UpdateSwitchInfoRequest('10002002')
		self.RoutineWorldUpdateRequest()
		self.UpdateSwitchInfoRequest('10000111,80011002')
		self.GachaExeRequest(3,3001,1,0)
		self.UpdateSwitchInfoRequest('10000209,10003001')
		self.RoutineEventUpdateRequest()
		self.LoginBonusRequest()
		self.UpdateSwitchInfoRequest('10000116,10000155')
		self.UpdateSwitchInfoRequest('')
		
	def TUTJP(self):
		#self.setDeviceId(self.t.getHashedDeviceID(Tools().genRandomDeviceID()))
		self.InitializeRequest()
		#self.CreateUserRequest()
		self.UpdateSwitchInfoRequest('10000152')
		#self.GetUserInfoRequest()
		self.FriendListRequest('1')
		self.RoutineHomeUpdateRequest()
		print self.startMission(1110100)[1]
		print self.startMission(1110101)[1]
		self.FriendListRequest('0')
		print self.startMission(1110103)[1]
		self.FriendListRequest('0')
		self.UpdateSwitchInfoRequest('')
		self.UpdateSwitchInfoRequest('10002002')
		self.UpdateSwitchInfoRequest('10000111')
		self.RoutineWorldUpdateRequest()
		self.RoutineEventUpdateRequest()
		self.UpdateSwitchInfoRequest('80011002')
		self.GachaExeRequest(3,3001,1,0)
		self.UpdateSwitchInfoRequest('10000117,10000209')
		self.UpdateSwitchInfoRequest('10003001')
		self.LoginBonusRequest()
		self.RoutineHomeUpdateRequest()
		self.NoticeUpdateRequest('1450')
		self.RoutineHomeUpdateRequest()
		self.UpdateSwitchInfoRequest('10000155,10000167')
		self.UpdateSwitchInfoRequest('')
		self.RoutineWorldUpdateRequest()
		print self.TransferCodeIssueRequest('apple')

	def completeTutorial(self,force=False):
		if self.isStarter or force:
			if self.isJapan:
				self.TUTJP()
			else:
				self.TUTGL()

	def byteify(self,input):
		if isinstance(input, dict):
			return {self.byteify(key): self.byteify(value)
					for key, value in input.iteritems()}
		elif isinstance(input, list):
			return [self.byteify(element) for element in input]
		elif isinstance(input, unicode):
			return input.encode('utf-8')
		else:
			return input

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	#LOGIN
	parser.add_argument('--deviceid', default=Tools().genRandomDeviceID())
	parser.add_argument('--ftoken', default=None)
	parser.add_argument('--fid', default=None)
	parser.add_argument('--proxy', default=None)
	parser.add_argument('--port', default=None)
	parser.add_argument('--device', default=1)
	parser.add_argument('--license', default=None)
	parser.add_argument('--mission', default=1110100)
	#OPTIONS
	parser.add_argument('--chests', action='store_true', default=False)
	parser.add_argument('--refill', action='store_true', default=False)
	parser.add_argument('--loot', action='store_true', default=False)
	parser.add_argument('--eloot', action='store_true', default=False)
	parser.add_argument('--solve', action='store_true', default=False)
	parser.add_argument('--friends', action='store_true', default=False)
	parser.add_argument('--master', action='store_true', default=False)
	parser.add_argument('--orbs', action='store_true', default=False)
	parser.add_argument('--corbs', action='store_true', default=False)
	parser.add_argument('--units', action='store_true', default=False)
	#EXTRA
	parser.add_argument('--lb', default=0)
	parser.add_argument('--repeat', default=0)
	parser.add_argument('--team', default=None)
	parser.add_argument('--q', action='store_true', default=False)
	#JAPAN
	parser.add_argument('--japan', action='store_true', default=False)
	parser.add_argument('--user_id', default=None)
	parser.add_argument('--password', default=None)
	parser.add_argument('--handle', default=None)
	parser.add_argument('--userid', default=None)
	parser.add_argument('--cnt', default=None)
	results = parser.parse_args()
	a=API()
	a.setPlayerID(results.deviceid,results.device)
	if results.user_id and results.password:
		print 'HAVE JAPAN!'#MILA
	if results.japan:
		a.setIsJapan()
		#a.setHANDLENAME(results.handle)
		a.setUSERID(results.handle)
		a.setMODEL_CHANGE_CNT(results.cnt)
	if results.q:
		a.setQuite()
	if results.master:
		a.setMaster()
	if results.ftoken and results.fid:
		a.setFacebook(results.ftoken,results.fid)
	if results.proxy and results.port:
		a.setProxie(results.proxy,results.port)
	if results.license:
		a.setLicense(results.license)
	if results.solve:
		a.setSolve()
	if results.refill:
		a.setRefill()
	if results.friends:
		a.setFriends()
	if results.chests:
		a.setChests()
	if results.orbs:
		a.setOrbs()
	if results.corbs:
		a.setCOrbs()
	if results.loot:
		a.setLoot()
	if results.eloot:
		a.setELoot()
	if results.units:
		a.setUnits()
	if results.lb:
		a.setLb(results.lb)
	if results.master:
		a.dolog('machen master arbeit')
		while(1):
			try:
				if results.proxy and results.port:
					a.setProxie(results.proxy,results.port)
				if not results.japan:
					a.GetBackgroundDownloadInfoRequest()
					a.GameSettingRequest()
				a.InitializeRequest()
			except:
				pass
			a.dolog('sleeping for next update')
			time.sleep(300)
	else:
		if not a.isJapan:
			a.GetBackgroundDownloadInfoRequest()
			a.GameSettingRequest()
		if a.InitializeRequest():
			a.GetUserInfoRequest()
			a.completeTutorial()
			#if results.team:
			#	a.PartyDeckEditRequest(results.team)
			if results.repeat:
				a.setFarmMode(results.mission,int(results.repeat))
			else:
				a.startMission(results.mission)
				if 'win' not in sys.platform:
					a.closeDB()