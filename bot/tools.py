# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
try:
	import challenges_gl
	import challenges_jp
except:
	pass
import errors
import mission_types_gl
import mission_types_jp
import mission_names_jp
import mission_names_gl
import data_gl
import socket
import units_jp
import units_gl
import levels_jp
import levels_gl
import random
from random import randint
from pkcs7 import PKCS7Encoder

class Tools(object):
	def __init__(self,version=1):
		self.version=version
		self.mode = AES.MODE_ECB
		self.encoder = PKCS7Encoder()
		self.prox=['']
		self.keys={'DungeonResourceLoadMstListRequest':{'url':'/actionSymbol/Sl8UgmP4.php','id':'jnw49dUq','key':'3PVu6ReZ'},'ItemCarryEditRequest':{'url':'/actionSymbol/8BE6tJbf.php','id':'UM7hA0Zd','key':'04opy1kf'},'UnitFavoriteRequest':{'url':'/actionSymbol/sqeRg12M.php','id':'tBDi10Ay','key':'w9mWkGX0'},'MissionReStartRequest':{'url':'/actionSymbol/r5vfM1Y3.php','id':'GfI4LaU3','key':'Vw6bP0rN'},'sgExpdQuestStartRequest':{'url':'/actionSymbol/I8uq68c3.php','id':'I8uq68c3','key':'60Os29Mg'},'RoutineWorldUpdateRequest':{'url':'/actionSymbol/oR1psQ5B.php','id':'6H1R9WID','key':'XDIL4E7j'},'FriendListRequest':{'url':'/actionSymbol/p3hwqW5U.php','id':'u7Id4bMg','key':'1iV2oN9r'},'GetReinforcementInfoRequest':{'url':'/actionSymbol/hXMoLwgE.php','id':'AJhnI37s','key':'87khNMou'},'DailyDungeonSelectRequest':{'url':'/actionSymbol/9LgmdR0v.php','id':'JyfxY2e0','key':'ioC6zqG1'},'sgMissionUnlockRequest':{'url':'/actionSymbol/LJhqu0x6.php','id':'LJhqu0x6','key':'ZcBV06K4'},'GetTitleInfoRequest':{'url':'/actionSymbol/BbIeq31M.php','id':'ocP3A1FI','key':'Mw56RNZ2'},'TownInRequest':{'url':'/actionSymbol/isHfQm09.php','id':'8EYGrg76','key':'JI8zU5rC'},'ClsmStartRequest':{'url':'/actionSymbol/rncR9js8.php','id':'4uCSA3ko','key':'wdSs23yW'},'CraftStartRequest':{'url':'/actionSymbol/w71MZ0Gg.php','id':'Gr9zxXk5','key':'K92H8wkY'},'TownUpdateRequest':{'url':'/actionSymbol/0ZJzH2qY.php','id':'G1hQM8Dr','key':'37nH21zE'},'MissionRetireRequest':{'url':'/actionSymbol/gbZ64SQ2.php','id':'v51PM7wj','key':'oUh1grm8'},'DailyQuestUpdateRequest':{'url':'/actionSymbol/QWDn5epF.php','id':'6QYd5Hym','key':'9QtGVCWg'},'RmStartRequest':{'url':'/actionSymbol/8BJSL7g0.php','id':'7FyJS3Zn','key':'iu67waph'},'ItemSellRequest':{'url':'/actionSymbol/hQRf8D6r.php','id':'d9Si7TYm','key':'E8H3UerF'},'RmEndRequest':{'url':'/actionSymbol/I9p3n48A.php','id':'fyp10Rrc','key':'FX5L3Sfv'},'BundlePurchaseRequest':{'url':'/actionSymbol/tPc64qmn.php','id':'w6Z9a6tD','key':'NE3Pp4K8'},'UnitSellRequest':{'url':'/actionSymbol/0qmzs2gA.php','id':'9itzg1jc','key':'DJ43wmds'},'UpdateSwitchInfoRequest':{'url':'/actionSymbol/SqoB3a1T.php','id':'mRPo5n2j','key':'4Z5UNaIW'},'ArchiveUpdateRequest':{'url':'/actionSymbol/2bCcKx0D.php','id':'cVTxW0K3','key':'IFLW9H4M'},'UnitMixRequest':{'url':'/actionSymbol/6aLHwhJ8.php','id':'UiSC9y8R','key':'4zCuj2hK'},'RateAppRewardRequest':{'url':'/actionSymbol/L0OsxMaT.php','id':'L0OsxMaT','key':'m1pPBwC3'},'RbReStartRequest':{'url':'/actionSymbol/DQ49vsGL.php','id':'6ZNY3zAm','key':'PRzAL3V2'},'DmgRankStartRequest':{'url':'/actionSymbol/j37Vk5xe.php','id':'5P6ULvjg','key':'1d5AP9p6'},'RoutineHomeUpdateRequest':{'url':'/actionSymbol/1YWTzU9h.php','id':'Daud71Hn','key':'aw0syG7H'},'RbEntryRequest':{'url':'/actionSymbol/30inL7I6.php','id':'f8kXGWy0','key':'EA5amS29'},'MissionContinueRequest':{'url':'/actionSymbol/ZzCXI6E7.php','id':'LuCN4tU5','key':'34n2iv7z'},'ItemBuyRequest':{'url':'/actionSymbol/oQrAys71.php','id':'sxK2HG6T','key':'InN5PUR0'},'ExchangeShopRequest':{'url':'/actionSymbol/1bf0HF4w.php','id':'I7fmVX3R','key':'qoRP87Fw'},'NoticeReadUpdateRequest':{'url':'/actionSymbol/j6kSWR3q.php','id':'pC3a2JWU','key':'iLdaq6j2'},'CampaignAcceptRequest':{'url':'/actionSymbol/n7Hitfg4.php','id':'G6ye0D1t','key':'Xb0G1wcB'},'RmDungeonStartRequest':{'url':'/actionSymbol/NC8Ie07P.php','id':'R5mWbQ3M','key':'A7V1zkyc'},'MissionUpdateRequest':{'url':'/actionSymbol/fRDUy3E2.php','id':'j5JHKq6S','key':'Nq9uKGP7'},'RbMatchingRequest':{'url':'/actionSymbol/mn5cHaJ0.php','id':'DgG4Cy0F','key':'4GSMn0qb'},'DailyQuestClaimAllRewardRequest':{'url':'/actionSymbol/Br9PwJ6A.php','id':'DCmya9WD','key':'KHx6JdrT'},'RbRankingRequest':{'url':'/actionSymbol/3fd8y7W1.php','id':'kcW85SfU','key':'SR6PoLM3'},'FacebookLogoutRequest':{'url':'/actionSymbol/xHTo4BZp.php','id':'xHTo4BZp','key':'wwHxtAy6'},'RoutineGachaUpdateRequest':{'url':'/actionSymbol/qS0YW57G.php','id':'t60dQP49','key':'Q6ZGJj0h'},'BundleStatusRequest':{'url':'/actionSymbol/tPc64qmn.php','id':'uLXAMvCT','key':'PrSPuc8c'},'CraftEndRequest':{'url':'/actionSymbol/9G7Vc8Ny.php','id':'WIuvh09n','key':'yD97t8kB'},'PurchaseCancelRequest':{'url':'/actionSymbol/y71uBCER.php','id':'L7K0ezU2','key':'Z1mojg9a'},'RoutineRaidMenuUpdateRequest':{'url':'/actionSymbol/Sv85kcPQ.php','id':'g0BjrU5D','key':'z80swWd9'},'DmgRankRetireRequest':{'url':'/actionSymbol/8wdmR9yG.php','id':'W3Z4VF1X','key':'5fkWyeE6'},'SearchGetItemInfoRequest':{'url':'/actionSymbol/e4Gjkf0x.php','id':'0D9mpGUR','key':'vK2V8mZM'},'CampaignTieupRequest':{'url':'/actionSymbol/2u30vqfY.php','id':'mI0Q2YhW','key':'72d5UTNC'},'CraftExeRequest':{'url':'/actionSymbol/UyHLjV60.php','id':'PKDhIN34','key':'ZbHEB15J'},'FriendFavoriteRequest':{'url':'/actionSymbol/8IYSJ5H1.php','id':'1oE3Fwn4','key':'3EBXbj1d'},'GachaExeRequest':{'url':'/actionSymbol/oC30VTFp.php','id':'9fVIioy1','key':'oaEJ9y1Z'},'DmgRankEndRequest':{'url':'/actionSymbol/zd5KJ3jn.php','id':'s98cw1WA','key':'7pGj8hSW'},'PurchaseSettlementRequest':{'url':'/actionSymbol/yt82BRwk.php','id':'JsFd4b7j','key':'jmh7xID8'},'UnitEquipRequest':{'url':'/actionSymbol/nIk9z5pT.php','id':'pB3st6Tg','key':'45VZgFYv'},'GetUserInfoRequest':{'url':'/actionSymbol/u7sHDCg4.php','id':'X07iYtp5','key':'rcsq2eG7'},'MailListRequest':{'url':'/actionSymbol/u3E8hpad.php','id':'KQHpi0D7','key':'7kgsrGQ1'},'SublimationSkillRequest':{'url':'/actionSymbol/xG3jBbw5.php','id':'s48Qzvhd','key':'97Uvrdz3'},'FacebookRewardListRequest':{'url':'/actionSymbol/8YZsGLED.php','id':'8YZsGLED','key':'85YBRzZg'},'PurchaseGiveUpRequest':{'url':'/actionSymbol/C2w0f3go.php','id':'BFf1nwh6','key':'xoZ62QWy'},'RbBoardPieceOpenRequest':{'url':'/actionSymbol/iXKfI4v1.php','id':'hqzU9Qc5','key':'g68FW4k1'},'TownOutRequest':{'url':'/actionSymbol/0EF3JPjL.php','id':'sJcMPy04','key':'Kc2PXd9D'},'UnitClassUpRequest':{'url':'/actionSymbol/8z4Z0DUY.php','id':'zf49XKg8','key':'L2sTK0GM'},'DailyQuestClaimRewardRequest':{'url':'/actionSymbol/Br9PwJ6A.php','id':'Zy8fYJ5e','key':'jwYGF3sY'},'RmEntryRequest':{'url':'/actionSymbol/fBn58ApV.php','id':'wx5sg9ye','key':'p2tqP7Ng'},'MissionBreakRequest':{'url':'/actionSymbol/P4oIeVf0.php','id':'17LFJD0b','key':'Z2oPiE6p'},'LoginBonusRequest':{'url':'/actionSymbol/iP9ogKy6.php','id':'vw9RP3i4','key':'Vi6vd9zG'},'sgExpdQuestRefreshRequest':{'url':'/actionSymbol/vTgYyHM6lC.php','id':'vTgYyHM6lC','key':'vceNlSf3gn'},'sgExpdAccelerateRequest':{'url':'/actionSymbol/Ik142Ff6.php','id':'Ik142Ff6','key':'d3D4l8b4'},'BeastBoardPieceOpenRequest':{'url':'/actionSymbol/Y2Zvnad9.php','id':'0gk3Tfbz','key':'7uxYTm3k'},'MissionStartRequest':{'url':'/actionSymbol/63VqtzbQ.php','id':'29JRaDbd','key':'i48eAVL6'},'RmRetireRequest':{'url':'/actionSymbol/fBn58ApV.php','id':'e0R3iDm1','key':'T4Undsr6'},'CraftAddRequest':{'url':'/actionSymbol/iQ7R4CFB.php','id':'QkN1Sp64','key':'qz0SG1Ay'},'MailReceiptRequest':{'url':'/actionSymbol/M2fHBe9d.php','id':'XK7efER9','key':'P2YFr7N9'},'FacebookAddFriendRequest':{'url':'/actionSymbol/NAW9vJnm.php','id':'NAW9vJnm','key':'532vAYUy'},'PartyDeckEditRequest':{'url':'/actionSymbol/6xkK4eDG.php','id':'TS5Dx9aZ','key':'34qFNPf7'},'BeastMixRequest':{'url':'/actionSymbol/7vHqNPF0.php','id':'C8X1KUpV','key':'WfNSmy98'},'FriendDeleteRequest':{'url':'/actionSymbol/8R4fQbYh.php','id':'a2d6omAy','key':'d0VP5ia6'},'CreateUserRequest':{'url':'/actionSymbol/0FK8NJRX.php','id':'P6pTz4WA','key':'73BUnZEr'},'TrophyRewardRequest':{'url':'/actionSymbol/05vJDxg9.php','id':'wukWY4t2','key':'2o7kErn1'},'PurchaseHoldRequest':{'url':'/actionSymbol/dCxtMZ27.php','id':'79EVRjeM','key':'5Mwfq90Z'},'MedalExchangeRequest':{'url':'/actionSymbol/0X8Fpjhb.php','id':'LiM9Had2','key':'dCja1E54'},'GameSettingRequest':{'url':'/actionSymbol/OTX6Fmvu.php','id':'OTX6Fmvu','key':'4foXVwWd'},'PurchaseSettingRequest':{'url':'/actionSymbol/9hUtW0F8.php','id':'QkwU4aD9','key':'ePFcMX53'},'sgExpdMileStoneClaimRequest':{'url':'/actionSymbol/r4A791RF.php','id':'r4A791RF','key':'t04N07LQ'},'GiftUpdateRequest':{'url':'/actionSymbol/noN8I0UK.php','id':'9KN5rcwj','key':'xLEtf78b'},'RbStartRequest':{'url':'/actionSymbol/dR20sWwE.php','id':'eHY7X8Nn','key':'P1w8BKLI'},'InitializeRequest':{'url':'/actionSymbol/fSG1eXI9.php','id':'75fYdNxq','key':'rVG09Xnt'},'PurchaseStartRequest':{'url':'/actionSymbol/tPc64qmn.php','id':'qAUzP3R6','key':'9Kf4gYvm'},'RoutineEventUpdateRequest':{'url':'/actionSymbol/WCK5tvr0.php','id':'4kA1Ne05','key':'V0TGwId5'},'PurchaseListRequest':{'url':'/actionSymbol/YqZ6Qc1z.php','id':'BT28S96F','key':'X3Csghu0'},'PurchaseFailedRequest':{'url':'/actionSymbol/2TCis0R6.php','id':'jSe80Gx7','key':'sW0vf3ZM'},'sgExpdEndRequest':{'url':'/actionSymbol/2pe3Xa8bpG.php','id':'2pe3Xa8bpG','key':'cjHumZ2Jkt'},'VariableStoreCheckRequest':{'url':'/actionSymbol/Nhn93ukW.php','id':'i0woEP4B','key':'Hi0FJU3c'},'GachaInfoRequest':{'url':'/actionSymbol/3nhWq25K.php','id':'UNP1GR5n','key':'VA8QR57X'},'sgExpdRecallRequest':{'url':'/actionSymbol/0Fb87D0F.php','id':'0Fb87D0F','key':'9J02K0lX'},'DungeonLiberationRequest':{'url':'/actionSymbol/0vc6irBY.php','id':'nQMb2L4h','key':'0xDA4Cr9'},'FriendSearchRequest':{'url':'/actionSymbol/6Y1jM3Wp.php','id':'3siZRSU4','key':'VCL5oj6u'},'ClsmEndRequest':{'url':'/actionSymbol/7vHqNPF0.php','id':'3zgbapQ7','key':'6aBHXGv4'},'MissionEndRequest':{'url':'/actionSymbol/0ydjM5sU.php','id':'x5Unqg2d','key':'1tg0Lsqj'},'sgHomeMarqueeInfoRequest':{'url':'/actionSymbol/PBSP9qn5.php','id':'PBSP9qn5','key':'d3GDS9X8'},'FacebookRewardClaimRequest':{'url':'/actionSymbol/47R9pLGq.php','id':'47R9pLGq','key':'Rja82ZUK'},'ClsmLotteryRequest':{'url':'/actionSymbol/4uj3NhUQ.php','id':'Un16HuNI','key':'pU62SkhJ'},'PurchaseCurrentStateRequest':{'url':'/actionSymbol/bAR4k7Qd.php','id':'9mM3eXgi','key':'X9k5vFdu'},'RmRestartRequest':{'url':'/actionSymbol/NC8Ie07P.php','id':'yh21MTaG','key':'R1VjnNx0'},'TransferCodeCheckRequest':{'url':'/actionSymbol/C9LoeYJ8.php','id':'CY89mIdz','key':'c5aNjK9J'},'sgExpdQuestInfoRequest':{'url':'/actionSymbol/hW0804Q9.php','id':'hW0804Q9','key':'4Bn7d973'},'MissionWaveReStartRequest':{'url':'/actionSymbol/8m7KNezI.php','id':'e9RP8Cto','key':'M3bYZoU5'},'TransferRequest':{'url':'/actionSymbol/v6Jba7pX.php','id':'oE5fmZN9','key':'C6eHo3wU'},'GetBackgroundDownloadInfoRequest':{'url':'/actionSymbol/action.php','id':'lEHBdOEf','key':'Z1krd75o'},'RmDungeonEndRequest':{'url':'/actionSymbol/CH9fWn8K.php','id':'WaPC2T6i','key':'dEnsQ75t'},'FriendAgreeRequest':{'url':'/actionSymbol/1DYp5Nqm.php','id':'kx13SLUY','key':'9FjK0zM3'},'FriendRefuseRequest':{'url':'/actionSymbol/Vw0a4I3i.php','id':'1nbWRV9w','key':'RYdX9h2A'},'OptionUpdateRequest':{'url':'/actionSymbol/0Xh2ri5E.php','id':'otgXV79T','key':'B9mAa7rp'},'TransferCodeIssueRequest':{'url':'/actionSymbol/hF0yCKc1.php','id':'crzI2bA5','key':'T0y6ij47'},'ClsmEntryRequest':{'url':'/actionSymbol/UmLwv56W.php','id':'5g0vWZFq','key':'8bmHF3Cz'},'FriendSuggestRequest':{'url':'/actionSymbol/6TCn0BFh.php','id':'iAs67PhJ','key':'j2P3uqRC'},'CraftCancelRequest':{'url':'/actionSymbol/7WdDLIE4.php','id':'79xDN1Mw','key':'68zcUF3E'},'UpdateUserInfoRequest':{'url':'/actionSymbol/v3RD1CUB.php','id':'ey8mupb4','key':'6v5ykfpr'},'RbEndRequest':{'url':'/actionSymbol/e8AHNiT7.php','id':'os4k7C0b','key':'MVA3Te2i'},'NoticeUpdateRequest':{'url':'/actionSymbol/TqtzK84R.php','id':'CQ4jTm2F','key':'9t68YyjT'},'RmBreakRequest':{'url':'/actionSymbol/8BJSL7g0.php','id':'kWrXKC35','key':'W3YTRI8e'},'ShopUseRequest':{'url':'/actionSymbol/w76ThDMm.php','id':'73SD2aMR','key':'ZT0Ua4wL'},'MissionWaveStartRequest':{'url':'/actionSymbol/Mn15zmDZ.php','id':'BSq28mwY','key':'d2mqJ6pT'},'FriendRequest':{'url':'/actionSymbol/8drhF2mG.php','id':'j0A5vQd8','key':'6WAkj0IH'},'StrongBoxOpenRequest':{'url':'/actionSymbol/48ktHf13.php','id':'PIv7u8jU','key':'sgc30nRh'}}
		self.assignFiles()

	def assignFiles(self):
		if self.version==1:
			self.levels=levels_gl.levels
			self.units=units_gl.units
			self.challenges=challenges_gl.challenges
			self.mission_types=mission_types_gl.mission_types
			self.mission_names=mission_names_gl.missions
		else:
			self.levels=levels_jp.levels
			self.units=units_jp.units
			self.challenges=challenges_jp.challenges
			self.mission_types=mission_types_jp.mission_types
			self.mission_names=mission_names_jp.missions
		self.data=data_gl.data
		
	def findLevelExp(self,lvl):
		try:
			return self.levels[lvl+1]
		except:
			return 106366

	def getRandomProxy(self):
		p=random.choice(self.prox)
		return {'http': 'http://%s:3128'%(p),'https': 'https://%s:3128'%(p),}

	def genRandomIP(self):
		return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

	def findMissionName(self,ch):
		id=str(ch)
		if id in self.mission_names:
			return self.mission_names[id]['name']
		print 'findMissionName %s'%(ch)
		return '--'

	def findMissionType(self,ch):
		try:
			try:
				return self.mission_types[str(ch)]['type']
			except:
				return self.mission_types[int(ch)]['type']
		except:
			print 'error in findMissionType %s'%(ch)
			return 1

	def findMissionCost(self,ch):
		try:
			try:
				return self.mission_types[str(ch)]['energy']
			except:
				return self.mission_types[int(ch)]['energy']
		except:
			print 'error in findMissionCost %s'%(ch)
			return 1

	def findMissionRound(self,ch):
		try:
			try:
				return self.mission_types[str(ch)]['rounds']
			except:
				return self.mission_types[int(ch)]['rounds']
		except:
			print 'error in findMissionRound %s'%(ch)
			return 1

	def findUnitName(self,id):
		if id in self.data['unit']:
			return self.data['unit'][id],str(id)
		print '%s missing id'%(id)
		return '--',id

	def findError(self,rr):
		try:
			return errors.errors[rr]
		except:
			return 'unknown error %s'%(rr)

	def findUnitPrice(self,id):
		if id in self.units:
			return self.units[str(id)]['price']
		else:
			print '%s missing price'%(id)
			return 0

	def getChallenges(self,ch):
		try:
			return self.challenges[str(ch)]
		except:
			return None

	def findItemName(self,id):
		id=str(id)
		if id in self.data['item']:
			return self.data['item'][id]
		elif id in self.data['recipebook']:
			return self.data['recipebook'][id]
		elif id in self.data['unit']:
			return self.data['unit'][id]
		else:
			print '%s missing name'%(id)
			return '--'
			
	def getAPIPoint(self,id):
		return self.keys[id]['url']

	def getAPIID(self,id):
		return self.keys[id]['id']

	def getAPIKey(self,id):
		return self.keys[id]['key']

	def genRandomDeviceID(self):
		return '%s-%s-%s-%s-%s'%(self.genRandomHex(8),self.genRandomHex(4),self.genRandomHex(4),self.genRandomHex(4),self.genRandomHex(12))

	def genRandomHex(self,n):
		return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])
		
	def fillKeyNoBase(self,key):
		return key+((16-len(key))*'\00')

	def fillKeyWithBase(self,key):
		return base64.b64encode(key+((16-len(key))*'\00'))

	def getHashedDeviceID(self,id):
		return self.encrypt(id,'Zy3MDURw')
		
	def getPlainDeviceID(self,id):
		return self.decrypt(id,'Zy3MDURw')

	def genRandomDeviceString(self):
		valid=['iPad1,1_%s.%s','iPad2,1_%s.%s','iPad2,2_%s.%s','iPad2,3_%s.%s','iPad2,4_%s.%s','iPad2,5_%s.%s','iPad2,6_%s.%s','iPad2,7_%s.%s','iPad3,1_%s.%s','iPad3,2_%s.%s','iPad3,3_%s.%s','iPad3,4_%s.%s','iPad3,5_%s.%s','iPad3,6_%s.%s','iPad4,1_%s.%s','iPad4,2_%s.%s','iPad4,3_%s.%s','iPad4,4_%s.%s','iPad4,5_%s.%s','iPad4,6_%s.%s','iPad4,7_%s.%s','iPad4,8_%s.%s','iPad4,9_%s.%s','iPad5,1_%s.%s','iPad5,2_%s.%s','iPad5,3_%s.%s','iPad5,4_%s.%s','iPad6,4_%s.%s','iPad6,7_%s.%s','iPad6,8_%s.%s','iPhone1,1_%s.%s','iPhone1,2_%s.%s','iPhone2,1_%s.%s','iPhone3,1_%s.%s','iPhone3,2_%s.%s','iPhone3,3_%s.%s','iPhone4,1_%s.%s','iPhone5,1_%s.%s','iPhone5,2_%s.%s','iPhone5,3_%s.%s','iPhone5,4_%s.%s','iPhone6,1_%s.%s','iPhone6,2_%s.%s','iPhone7,1_%s.%s','iPhone7,2_%s.%s','iPhone8,1_%s.%s','iPhone8,2_%s.%s']
		return random.choice(valid)%(randint(1,10),randint(0,9))
	
	def encrypt(self,s,key):
		if len(key)<16:
			key=self.fillKeyNoBase(key)
		e = AES.new(key, self.mode)
		padded_text = self.encoder.encode(s.encode('utf-8'))
		return base64.b64encode(e.encrypt(padded_text))

	def decrypt(self,s,key):
		if len(key)<16:
			key=self.fillKeyNoBase(key)
		e = AES.new(key, self.mode)
		return self.encoder.decode(e.decrypt(base64.b64decode(s)))
