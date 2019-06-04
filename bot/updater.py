# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import base64
import io
import json
import os
import re
import sys
import time
import conf
import socket

def getK(i):
	if i in conf.vars:
		return conf.vars[i]
	else:
		return None

def rp(ii):
	if 'Admin-PC' == socket.gethostname():
		content=ii
		keys=re.findall('"([a-zA-Z0-9]{8,8})"',content)
		found=[]
		for k in keys:
			if k not in found:
				found.append(k)
		for i in found:
			kf=getK(i)
			if i in content:
				if kf:
					content=content.replace(i,'%s:%s'%(i,kf))
		return content
	else:
		return ii

class Tools(object):
	def __init__(self):
		self.mode = AES.MODE_ECB
		self.encoder = PKCS7Encoder()
		self.names={'F_ABILITY_EXPLAIN_MST':{'id':'7FGj2bCh','key':'B2Ka3kft'},'F_ABILITY_MST':{'id':'TK61DudV','key':'4sPQ8aXo'},'F_AI_MST':{'id':'PCm9K3no','key':'yFr6Kj3P'},'F_ARCHIVE_MST':{'id':'Wmd5K32b','key':'t3T1hELp'},'F_AREA_MST':{'id':'Fvix6V0n','key':'pR2DHS6i'},'F_AWARD_MST':{'id':'xH4WGNk8','key':'HZgmc2u9'},'F_AWARD_TYPE_MST':{'id':'jsX49HtE','key':'t3IEWke8'},'F_BANNER_MST':{'id':'oB0YVw67','key':'C6ci5pfG'},'F_BATTLE_BG_MST':{'id':'bqR4p8SN','key':'39mEiDNB'},'F_BATTLE_SCRIPT_MST':{'id':'i7STtbw8','key':'o28ckLUb'},'F_BEAST_BOARD_PIECE_EXT_MST':{'id':'5o0Z6Gwn','key':'Knh15FzM'},'F_BEAST_BOARD_PIECE_MST':{'id':'E9z2e4UZ','key':'XvkVU34H'},'F_BEAST_CP_MST':{'id':'dzA5MC6f','key':'Syax34vR'},'F_BEAST_EXPLAIN_MST':{'id':'J3BkY7wT','key':'jw0X2ZNm'},'F_BEAST_EXP_PATTERN_MST':{'id':'42JaImDh','key':'UY7D3dpn'},'F_BEAST_GROW_MST':{'id':'tSb4Y8QR','key':'7YUDsew3'},'F_BEAST_MST':{'id':'WF57bvfG','key':'hdFeT14k'},'F_BEAST_SKILL_MST':{'id':'zE1hx53P','key':'Y4Fds1Jr'},'F_BEAST_STATUS_MST':{'id':'tWp7f5Ma','key':'XuWn97Hf'},'F_CAPTURE_MST':{'id':'65fHqgnT','key':'w1A9S5sr'},'F_CHALLENGE_MST':{'id':'GL9t6cMF','key':'8Dx2QUZS'},'F_CHARACTER_MST':{'id':'cf29diuR','key':'ru39Q4YK'},'F_CLSM_GRADE_MST':{'id':'q14CSpIb','key':'sn8QPJ24'},'F_CLSM_PROGRESS_MST':{'id':'pF3JiA6L','key':'h8Za6TiL'},'F_CLSM_RANK_MST':{'id':'W2f5GThw','key':'jtbur0h5'},'F_CLSM_ROUND_MST':{'id':'7zEc85n1','key':'V4wZA7Hn'},'F_CRAFT_EXT_MST':{'id':'1GPYxQR3','key':'eHn8EU5o'},'F_DEFINE_MST':{'id':'zg5P1AxM','key':'Zib6m5ed'},'F_DESCRIPTION_FORMAT_MST':{'id':'HL3rXQh7','key':'WvJI5AB8'},'F_DIAMOND_MST':{'id':'mo47BaST','key':'p9sk1MjH'},'F_DUNGEON_MST':{'id':'1Bj4oy5Q','key':'9bEA2SYP'},'F_EFFECT_GROUP_MST':{'id':'ZM06fUem','key':'4WipzuH2'},'F_EFFECT_MST':{'id':'HfRPdg65','key':'d4KR8YSq'},'F_EMBLEM_ITEM_MST':{'id':'SuM2XA05','key':'UyE6HP3h'},'F_ENCOUNT_FIELD_MST':{'id':'2Jtkc4Ar','key':'mhok0p7B'},'F_EQUIP_ITEM_EXPLAIN_MST':{'id':'psuJ5VE2','key':'r6PSK8QW'},'F_EQUIP_ITEM_MST':{'id':'S67QEJsz','key':'T1kP80NU'},'F_EXCHANGE_SHOP_ITEM_MST':{'id':'5hYf3xv1','key':'sg3fXED8'},'F_EXPEDITION_DIFFICULTY_MST':{'id':'4Xy9386a','key':'0vkM7772'},'F_EXPEDITION_MST':{'id':'TdE7Oasq','key':'fFx92pYD'},'F_EXPLORE_AREA_MST':{'id':'b2VdS9Pv','key':'6wm49Yur'},'F_EXPLORE_TIME_MST':{'id':'1jVfJ6CB','key':'0WaTe2ZH'},'F_EXVIUS_POINT_REWARD_MST':{'id':'jiSF1p9I','key':'h8x1tiwz'},'F_FOOTPRINT_MST':{'id':'q3jTCo8m','key':'iI7aS2oq'},'F_FUNCTION_MST':{'id':'6wibj9m8','key':'sy6GRuY2'},'F_GACHA_EFFECT_BLOCK_MST':{'id':'fDI1T97q','key':'7H3P6zF4'},'F_GACHA_EFFECT_PATTERN_MST':{'id':'uw07SXpU','key':'48HhnaKP'},'F_GACHA_SELECT_UNIT_MST':{'id':'qRb73JSY','key':'H9Jye1j3'},'F_GAME_TITLE_MST':{'id':'91D3CfxA','key':'yFZs58K7'},'F_GIFT_MST':{'id':'AK5v1YEd','key':'1cJ4IuP9'},'F_ICON_MST':{'id':'LM1APs6u','key':'8XT23CYy'},'F_IMAGE_SWITCHING_MST':{'id':'K4rvk96u','key':'Ne92GPyR'},'F_IMPORTANT_ITEM_EXPLAIN_MST':{'id':'Nny6xD90','key':'89fcSX4v'},'F_IMPORTANT_ITEM_MST':{'id':'vdeSoq61','key':'tnNGLk45'},'F_ITEM_EXPLAIN_MST':{'id':'E7YMdK3P','key':'TERM4PD7'},'F_ITEM_EXT_BEAST_MST':{'id':'hc8Ham29','key':'wZ5IkW2f'},'F_ITEM_MST':{'id':'1CUX0Qwr','key':'L3f8nko1'},'F_JOB_MST':{'id':'F2mQ87Wt','key':'3CVoZu7s'},'F_LAND_MST':{'id':'23yVcGpH','key':'Y9wKxzI0'},'F_LEARNING_MST':{'id':'DLVF0cN1','key':'4HCdYk80'},'F_LIMITBURST_LV_MST':{'id':'0EvyjKh8','key':'g2hZpVW7'},'F_LIMITBURST_MST':{'id':'c5T4PIyL','key':'6q3eIR9k'},'F_LOGIN_BONUS_MST':{'id':'P3raZX89','key':'8xQP3fUZ'},'F_LOGIN_BONUS_SP_MST':{'id':'gjkPJ95T','key':'o64t9Qmd'},'F_LOGIN_BONUS_SP_REWARD_MST':{'id':'JQ1c6DCd','key':'Ym2rpIA7'},'F_LOGIN_BONUS_TOTAL_REWARD_MST':{'id':'J6dVmNv5','key':'y57ZhtLI'},'F_MAGIC_EXPLAIN_MST':{'id':'8qbVQUx5','key':'8LE2hk3r'},'F_MAGIC_MST':{'id':'6J8jwSDW','key':'2zyP4WQY'},'F_MAP_EVENT_MST':{'id':'91vNbdxg','key':'1YAk2fcr'},'F_MAP_EXT_RESOURCE_MST':{'id':'En90A5BC','key':'9dA6bguS'},'F_MAP_OBJECT_MST':{'id':'7d25gta1','key':'1zYSh5ps'},'F_MAP_ROUTE_MST':{'id':'F1a5PZYq','key':'rASW8N5L'},'F_MATERIA_EXPLAIN_MST':{'id':'bW2GHT1N','key':'7mof2RVP'},'F_MATERIA_LIMIT_MST':{'id':'BX0pRc8A','key':'CVERk9KN'},'F_MATERIA_MST':{'id':'Af46DrVW','key':'4MbdRZI6'},'F_MISSION_MST':{'id':'24Eka6wL','key':'naJ3P84b'},'F_MONSTER_DICTIONARY_EXPLAIN_MST':{'id':'Svq1K0rh','key':'wA4Dxp1m'},'F_MONSTER_DICTIONARY_MST':{'id':'1r6jb9wB','key':'wL4N16V3'},'F_NPC_MST':{'id':'94diC1bt','key':'fvQ37cE0'},'F_PICTURE_STORY_MST':{'id':'PSDIR8b1','key':'SDV4mZL0'},'F_PLAYBACK_CHAPTER_MST':{'id':'Nm36woZx','key':'gHLE4DM0'},'F_PLAYBACK_EVENT_MST':{'id':'IL78hX09','key':'qWr8ZE2D'},'F_PLAYBACK_MAP_MST':{'id':'9Zdr5ap0','key':'ZdM9VQb0'},'F_PLAYBACK_SEASON_MST':{'id':'D2zaT7Ru','key':'UgLId19h'},'F_PRODUCT_MST':{'id':'DEC8Jmy2','key':'OEl4ZmDY'},'F_PURCHASE_AGE_LIMIT_MST':{'id':'okUH6yV7','key':'ZDvrb16x'},'F_QUEST_MST':{'id':'2Px75LpY','key':'20mEeKo3'},'F_QUEST_SUB_MST':{'id':'myGc0U5v','key':'oWcL37sK'},'F_RB_ABILITY_GROUP_MST':{'id':'UHk7x2V8','key':'Q83j0GvZ'},'F_RB_AI_PATTERN_MST':{'id':'A6DJx0Qj','key':'2phgAJt3'},'F_RB_BONUS_RULE_MST':{'id':'09u3Nzk2','key':'7Hm6jxe3'},'F_RB_DEFINE_MST':{'id':'qzTG4ba0','key':'2y1oT5gq'},'F_RB_FORBIDDEN_INFO_MST':{'id':'x6iQrD2e','key':'8yWH5IGC'},'F_RB_LS_MST':{'id':'8tR1K79p','key':'2nJN19qh'},'F_RB_LS_REWARD_MST':{'id':'0Nc4PkAJ','key':'m7XJdkp1'},'F_RB_SS_MST':{'id':'gd74jWQn','key':'gY7NiJL8'},'F_RB_SS_REWARD_MST':{'id':'cg5k2Mxn','key':'KNWf37Bm'},'F_RB_TRADE_BOARD_MST':{'id':'yiuv0Fb9','key':'cbqYR3s7'},'F_RB_TRADE_BOARD_PIECE_MST':{'id':'7Si5wPLj','key':'fXZse89L'},'F_RECIPE_BOOK_MST':{'id':'yu5rvEI3','key':'3t8DMRQE'},'F_RECIPE_MST':{'id':'27pGMZDm','key':'JveAwh98'},'F_RESOURCE_MAP_VERSION_MST_LOCALIZE':{'id':'YIgCpDKW','key':'geHlpoos'},'F_RESOURCE_VERSION_MST_LOCALIZE':{'id':'A1L1GlaQ','key':'JchlFPWK'},'F_RULE_MST':{'id':'7s4egUBN','key':'sf2o1jWL'},'F_SACRIFICE_MST':{'id':'w5JFGPh3','key':'J2u0YBPr'},'F_SEASON_EVENT_ABILITY_MST':{'id':'VMIe9c6U','key':'Na71Z6kg'},'F_SEASON_EVENT_ABILITY_TYPE_MST':{'id':'I0SUr3WY','key':'XY2MA1x3'},'F_SEASON_EVENT_GROUP_FRIEND_LV_MST':{'id':'v5aCt9ne','key':'g7VmK5a9'},'F_SG_TIME_DUNGEON_MST':{'id':'pnjSbo89','key':'UhUsWVhw'},'F_SHOP_MST':{'id':'1ks9q4Pj','key':'X0FA6Ewh'},'F_SOUND_MST':{'id':'9bnqECY6','key':'m2zHEtV0'},'F_SP_CHALLENGE_MST':{'id':'4b6NcpLo','key':'wd1t3MPf'},'F_STORY_EVENT_MST':{'id':'YW9MUm2H','key':'LyjM2nU9'},'F_STORY_MST':{'id':'IiVw7H6k','key':'Cf2WZ8qA'},'F_STORY_SUB_MST':{'id':'8vneWT7G','key':'8ci0TamY'},'F_STRONGBOX_MST':{'id':'X1xsdRk7','key':'qPpXT0Z2'},'F_SUBLIMATION_RECIPE_MST':{'id':'M9K0SJgR','key':'vnkfer76'},'F_SWITCH_MST':{'id':'T46RpNZH','key':'AUx51pni'},'F_SWITCH_TYPE_MST':{'id':'PJw28YRg','key':'5NUkhS4Q'},'F_TEAM_LV_MST':{'id':'NCPTw2p0','key':'qP7TGZE8'},'F_TEXT_ABILITY_EXPLAIN_LONG':{'id':'uxMPAs4y','key':'lECkWwBw'},'F_TEXT_ABILITY_EXPLAIN_SHORT':{'id':'8GJBzdQV','key':'D9UVupRQ'},'F_TEXT_ABILITY_NAME':{'id':'eSB5Ry3E','key':'At4ghcWo'},'F_TEXT_ABILITY_PARAM_MSG':{'id':'3oM745kA','key':'OTxnCDr7'},'F_TEXT_ARCHIVE_NAME':{'id':'QR3zeiJr','key':'CrZmyr8k'},'F_TEXT_AREA_NAME':{'id':'4qiOcmtJ','key':'FhWJxFlW'},'F_TEXT_AWARD_EXPLAIN':{'id':'TlrlvFx5','key':'XfXmnCNF'},'F_TEXT_AWARD_NAME':{'id':'mGPBqPdv','key':'G9IOqfaz'},'F_TEXT_AWARD_TYPE':{'id':'soohaWOo','key':'b23aWS6d'},'F_TEXT_BEAST_NAME':{'id':'148O76GI','key':'pzLuYoDO'},'F_TEXT_BEAST_SKILL_DES':{'id':'Yjq14lAB','key':'g5SJviEC'},'F_TEXT_BEAST_SKILL_NAME':{'id':'k51drhZ6','key':'JHJRAcEx'},'F_TEXT_BUNDLE':{'id':'4OBhnBKu','key':'3VkESseA'},'F_TEXT_CAPTURE_INFO':{'id':'Ir2B1EBL','key':'Ak7An4Ys'},'F_TEXT_CHALLENGE_NAME':{'id':'4bQbA2FH','key':'SFaS7rXZ'},'F_TEXT_CHARACTER_NAME':{'id':'JIqrNzje','key':'iizk8FjI'},'F_TEXT_COLOSSEUM_GRADE':{'id':'Y2rngIF3','key':'7Vzk5Oq9'},'F_TEXT_COLOSSEUM_MONSTER_GROUP_NAME':{'id':'q4z5D08C','key':'04zFXazI'},'F_TEXT_DAILY_QUEST_DES':{'id':'W4525rcx','key':'1ihwWs7f'},'F_TEXT_DAILY_QUEST_DETAIL':{'id':'gCfFcx75','key':'xpLyjA9A'},'F_TEXT_DAILY_QUEST_NAME':{'id':'FBBD8vv6','key':'BhDl8FWG'},'F_TEXT_DIAMOND_NAME':{'id':'mcQeT7mq','key':'tN7Gjdpv'},'F_TEXT_DUNGEON_NAME':{'id':'AyVqkz2B','key':'0cqVvd61'},'F_TEXT_EXCHANGE_SHOP_ITEM':{'id':'r1ZLxyyg','key':'fT1SbKUm'},'F_TEXT_EXPN_STORY':{'id':'N1FxjkHa','key':'AC7L89p8'},'F_TEXT_GACHA':{'id':'ZJz5QwAy','key':'Ab2Kb6yJ'},'F_TEXT_GAME_TITLE_NAME':{'id':'3CzC5zn7','key':'SA6Bv7i1'},'F_TEXT_IMPORTANT_ITEM_EXPLAIN_LONG':{'id':'aJ4tvgSq','key':'iElLxksB'},'F_TEXT_IMPORTANT_ITEM_EXPLAIN_SHORT':{'id':'YBqAUJt1','key':'Fc6H1Udw'},'F_TEXT_IMPORTANT_ITEM_NAME':{'id':'TIKwbf3D','key':'lx4HCdrQ'},'F_TEXT_IMPORTANT_ITEM_SHOP':{'id':'JO7UqqJ6','key':'EzACmD0Y'},'F_TEXT_ITEM_EQUIP_LONG':{'id':'CD4giPVu','key':'jqe9yQm0'},'F_TEXT_ITEM_EQUIP_NAME':{'id':'E0NdslwL','key':'SGMI0nIq'},'F_TEXT_ITEM_EQUIP_SHORT':{'id':'Nao9HYWk','key':'I0l1uc2s'},'F_TEXT_ITEM_EXPLAIN_LONG':{'id':'9NCIDltW','key':'s3fVSywt'},'F_TEXT_ITEM_EXPLAIN_SHORT':{'id':'IAPS1jOu','key':'TZh30bbo'},'F_TEXT_ITEM_NAME':{'id':'VhkhtvDn','key':'xDkegMbe'},'F_TEXT_JOB_NAME':{'id':'yUkwbFyc','key':'R6mBb3T3'},'F_TEXT_LAND_NAME':{'id':'sKLZVYWQ','key':'yYnTSUtm'},'F_TEXT_LIMIT_BURST_DES':{'id':'EUsG7rlQ','key':'ZcXYp8BI'},'F_TEXT_LIMIT_BURST_NAME':{'id':'XBS8hLZD','key':'zswbSb5U'},'F_TEXT_MAGIC_EXPLAIN_LONG':{'id':'Jcavjyxo','key':'ZFHehCN4'},'F_TEXT_MAGIC_EXPLAIN_SHORT':{'id':'Hs9KVVnj','key':'raokY9Xl'},'F_TEXT_MAGIC_NAME':{'id':'1ZqISaBp','key':'9TAwFj0e'},'F_TEXT_MAP_OBJECT':{'id':'15KaBQci','key':'U56G5oiU'},'F_TEXT_MATERIA_EXPLAIN_LONG':{'id':'QEbXmDTD','key':'3ZaDmbq1'},'F_TEXT_MATERIA_EXPLAIN_SHORT':{'id':'8g18k8jD','key':'DvdwoXYQ'},'F_TEXT_MATERIA_NAME':{'id':'2Eg5s20D','key':'E5jbLGyb'},'F_TEXT_MISSION':{'id':'pa6vblsG','key':'GdAhtrNB'},'F_TEXT_MONSTER_DICTIONARY_NAME':{'id':'F1VQsGpG','key':'uEOGF11w'},'F_TEXT_MONSTER_DIC_EXPLAIN_LONG':{'id':'xe6RH45K','key':'p9l4ys4L'},'F_TEXT_MONSTER_DIC_EXPLAIN_SHORT':{'id':'zf7USTwU','key':'OJir9FR5'},'F_TEXT_MONSTER_NAME':{'id':'0xkPiwVI','key':'UOz3hI2k'},'F_TEXT_MONSTER_PART_DIC_NAME':{'id':'P4c5fq2t','key':'XhCacZZv'},'F_TEXT_MONSTER_SKILL_NAME':{'id':'F1z92dkt','key':'B41kLp2C'},'F_TEXT_MONSTER_SKILL_SET_NAME':{'id':'76oKZdNU','key':'mOz786Zr'},'F_TEXT_NPC_NAME':{'id':'A55coosK','key':'xQj2cuc8'},'F_TEXT_PICTURE_STORY_NAME':{'id':'j525zYCH','key':'Pe21ACFe'},'F_TEXT_PLAYBACK':{'id':'cvz0lj48','key':'svmqgt6n'},'F_TEXT_QUEST':{'id':'NMwfx1lf','key':'KVBowHC2'},'F_TEXT_QUEST_SUB_DETAIL':{'id':'vb5Nom5d','key':'sCFyRxng'},'F_TEXT_QUEST_SUB_NAME':{'id':'uuU68I2u','key':'cnW2w71S'},'F_TEXT_QUEST_SUB_STORY':{'id':'fULaqIeB','key':'CueuZNTN'},'F_TEXT_QUEST_SUB_TARGET_PARAM':{'id':'Cw3B65ql','key':'W4rz5Sas'},'F_TEXT_RB_ABILITY_GROUP_DESCRIPTION':{'id':'3sxyv1w9','key':'v30p83B2'},'F_TEXT_RB_ABILITY_GROUP_NAME':{'id':'69zUY4Zb','key':'qEAmEfJU'},'F_TEXT_RB_BONUS_RULE_DESCRIPTION':{'id':'10Ew2Rth','key':'AGItS6CC'},'F_TEXT_RB_BONUS_RULE_NAME':{'id':'6YYynT87','key':'YC0psthA'},'F_TEXT_RB_FORBIDDEN_INFO_DESCRIPTION':{'id':'M6bRb5Eg','key':'ScqX2kIE'},'F_TEXT_RB_FORBIDDEN_INFO_NAME':{'id':'DaNvFWp7','key':'wxea5c0t'},'F_TEXT_RECIPE_BOOK_NAME':{'id':'tFnHkR8G','key':'lEWsm9iI'},'F_TEXT_RECIPE_EXPLAIN_LONG':{'id':'DS21iNC5','key':'9uTG75o7'},'F_TEXT_RULE_DESCRIPTION':{'id':'a6kiwI22','key':'EahlebAb'},'F_TEXT_SCENARIO_BATTLE':{'id':'TGxop4tW','key':'ZCIcuxf3'},'F_TEXT_SEASON_EVENT_ABILITY_NAME':{'id':'q81b55dv','key':'E6Jrump4'},'F_TEXT_SEASON_EVENT_ABILITY_TYPE_DESCRI':{'id':'q81b55dv','key':'E6Jrump4'},'F_TEXT_SEASON_EVENT_ABILITY_TYPE_DESCRIPTION':{'id':'q81b55dv','key':'E6Jrump4'},'F_TEXT_SEASON_EVENT_ABILITY_TYPE_NAME':{'id':'xT67VZAS','key':'jFgn6bIU'},'F_TEXT_SEASON_EVENT_DESCRIPTION':{'id':'mKbhB8ai','key':'Kt30PvJg'},'F_TEXT_SEASON_EVENT_NAME':{'id':'FxaCYmHE','key':'NwKi0CpP'},'F_TEXT_SHOP':{'id':'NYz5Oxm4','key':'yBd5wOHp'},'F_TEXT_SPCHALLENGE':{'id':'hge62ssc','key':'lklesd2w'},'F_TEXT_STORY_NAME':{'id':'fKGHnuPm','key':'nJswCIXz'},'F_TEXT_STORY_SUB':{'id':'hiiVWxXJ','key':'ucOQs1YO'},'F_TEXT_SUBLIMATION_EXPLAIN':{'id':'JF89DHPE','key':'SkUNQP6F'},'F_TEXT_TELEPO_NAME':{'id':'ca5XNnWD','key':'WfvQbAKG'},'F_TEXT_TEXT_EN':{'id':'0ThfQQWd','key':'s9E34w78'},'F_TEXT_TICKER':{'id':'RUPcXt7J','key':'tHaAyyqI'},'F_TEXT_TOWN_EXPLAIN':{'id':'KLoYS0Tj','key':'0BZOtiRB'},'F_TEXT_TOWN_NAME':{'id':'N12vEZpN','key':'11yq2cUt'},'F_TEXT_TOWN_STORE':{'id':'h23JuUGF','key':'Jovaw62m'},'F_TEXT_TOWN_STORE_COMMENT':{'id':'SZXTrTgq','key':'oVpBUtX2'},'F_TEXT_TOWN_STORE_OWNER_NAME':{'id':'KFL34pbm','key':'Q9HMWNZG'},'F_TEXT_TRIBE':{'id':'Z6OfsPv9','key':'FAfGhIMo'},'F_TEXT_TROPHY_EXPLAIN':{'id':'pNeHXqpJ','key':'OJV9Jpm8'},'F_TEXT_TROPHY_METER_SERIF':{'id':'7BfBBf9E','key':'S410iF8y'},'F_TEXT_UNITS_NAME':{'id':'sZE3Lhgj','key':'3IfWAnJ3'},'F_TEXT_UNIT_AFFINITY':{'id':'Zfw0jmyn','key':'xCppLKwD'},'F_TEXT_UNIT_DESCRIPTION':{'id':'w6U2ntyZ','key':'VNh3r92R'},'F_TEXT_UNIT_EVO':{'id':'7tfppWVS','key':'OYQn68Hu'},'F_TEXT_UNIT_EXPLAIN_SHOP':{'id':'3uEWl5CV','key':'QrOn67A8'},'F_TEXT_UNIT_FUSION':{'id':'TpbDECdR','key':'v47OlIK4'},'F_TEXT_UNIT_SUMMON':{'id':'hWE8dJMC','key':'GInxSlTN'},'F_TEXT_WORLD_NAME':{'id':'GPNXLUJP','key':'uDFuhlR6'},'F_TICKER_DEFINE_MESSAGE_MST':{'id':'tUQ2Lkc1','key':'6TQR0hSX'},'F_TICKER_LOG_CATEGORY_MST':{'id':'QmnZ48Fs','key':'hJ91Gkz5'},'F_TICKER_MST':{'id':'5WJ9MQ3n','key':'h92Fk0Qw'},'F_TICKET_MST':{'id':'95KFiNTM','key':'0sDdWku8'},'F_TOWN_MST':{'id':'6P9XZ7ts','key':'IavY38oB'},'F_TOWN_STORE_COMMENT_MST':{'id':'ASh8IH0b','key':'1L7oneM4'},'F_TOWN_STORE_MST':{'id':'v34C8PdG','key':'Si9bxe86'},'F_TRIBE_MST':{'id':'3Lc1DWQV','key':'adj41LQC'},'F_TROPHY_METER_SERIF_MST':{'id':'4Qz7qK51','key':'SGjk89Tr'},'F_TROPHY_MST':{'id':'9ZN4Eo1m','key':'5qRZs6Kz'},'F_TROPHY_REWARD_MST':{'id':'GN1bMQm3','key':'KyAC0q3D'},'F_UNIT_CLASS_UP_MST':{'id':'60FtuAhp','key':'pjW5TI0K'},'F_UNIT_EXPLAIN_MST':{'id':'Da62x85q','key':'zU6L4Gng'},'F_UNIT_EXP_PATTERN_MST':{'id':'kMnY10ry','key':'B38YWDtF'},'F_UNIT_GROW_MST':{'id':'i3YrEM1t','key':'6cUguh10'},'F_UNIT_MST':{'id':'SsidX62G','key':'UW0D8ouL'},'F_UNIT_SERIES_LV_ACQUIRE_MST':{'id':'Eb5ewi87','key':'t8QV2WvE'},'F_URL_MST':{'id':'9wmd4iua','key':'UREmi85S'},'F_WORLD_MST':{'id':'JLxQW68j','key':'t8bWUq9Z'},'F_TOWN_EXPLAIN_MST':{'id':'QJF37LcR','key':'1ThX6WNZ'},'F_TROPHY_EXPLAIN_MST':{'id':'yhnT19Z4','key':'JPTK6q4V'},'F_MONSTER_SKILL_SET_MST':{'id':'B9K8ULHc','key':'p6iXmLh4'},'F_AWARD_EXPLAIN_MST':{'id':'B2mKN0M4','key':'0FfIgG67'},'F_MEDAL_EXCHANGE_MST':{'id':'2qDEnLF9','key':'7FmTj0hp'},'F_STORE_ITEM_MST':{'id':'03cY9vXe','key':'d60DCUMp'},'F_TELEPO_MST':{'id':'zw0kb3To','key':'KENf4db1'},'F_RESOURCE_MAP_MST':{'id':'B7LnP2TH','key':'U0Vd7AfQ'},'F_RESOURCE_MST':{'id':'ZQqB38Ns','key':'u6q3F02d'},'F_TEXT_ANALYTICS_LOCALIZE':{'id':'3sI39BAT','key':'6zAQarn1'},'F_TEXT_ANALYTICS_ITEMS':{'id':'8e6PGb3p','key':'7nyO4pC9'},'F_TEXT_BATTLE_SCRIPT':{'id':'dhR7sSxt','key':'QuxKHQQT'}}
		
	def fillKeyNoBase(self,key):
		return key+((16-len(key))*'\00')

	def fillKeyWithBase(self,key):
		return base64.b64encode(key+((16-len(key))*'\00'))

	def findFileName(self,id):
		try:
			return self.names[id]['id']
		except:
			return None

	def findFileKey(self,id):
		try:
			return self.names[id]['key']
		except:
			print 'key not found %s'%id
			return None

	def cleanName(self,n):
		return re.sub('.dat.*','',n)

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

class Updater(object):
	def __init__(self,region=1):
		self.region=region
		if self.region==1:
			self.base_txt='http://lapis-dlc.gumi.sg/dlc_assets_prod/localized_texts/%s'
			self.base_mst='http://lapis-dlc.gumi.sg/dlc_assets_prod/mst/%s'
		else:
			self.base_txt='http://cdn.resource.exvius.com/dlc_assets_prod/localized_texts/%s'
			self.base_mst='http://cdn.resource.exvius.com/lapis/resource/mst/%s'
		self.tools=Tools()

	def log(self,msg):
		print('[%s]:%s'%(time.strftime('%H:%M:%S'),msg))

	def setTT(self,data):
		self.updateData=data
		self.findMST()
		self.doUpdate()
		self.unpackAll()
		try:
			self.updateAll()
		except:
			pass

	def updateAll(self):
		self.parseMissionTypes()
		self.parseItemNames()
		self.parseMissionNames()
		self.parseLevels()
		self.parseUnit()
		self.parseChallenges()

	def doUpdate(self):
		if hasattr(self,'updateData'):
			self.makeFolder(self.mst)
			for ufile in  self.updateData:
				ufilename=self.tools.findFileName(ufile['a4hXTIm0'])
				if ufilename:
					self.downloadFile(ufile['a4hXTIm0'],ufile['wM9AfX6I'],ufilename)
				else:
					self.log('missing:%s %s'%(ufile['a4hXTIm0'],ufile['wM9AfX6I']))

	def makeFolder(self,name):
		if not os.path.exists(name):
			os.makedirs(name)

	def isFolder(self,file):
		return os.path.exists(file)
			
	def ensure_unicode(self,v):
		if isinstance(v, str):
			v = v.decode('utf8')
		return unicode(v)

	def save(self,data,file):
		with io.open(file, 'w', encoding='utf8') as the_file:
			if '_MST' in file:
				the_file.write('%s'%(unicode(json.dumps(json.loads(data), indent=4, sort_keys=True,ensure_ascii=False))))
			else:
				the_file.write('%s'%(unicode(self.ensure_unicode(data))))

	def downloadFile(self,file,version,filename):
		download_name='Ver%s_%s.dat'%(version,filename)
		local_name='%s.dat'%(file)
		if not os.path.isfile('%s/%s'%(self.mst,local_name)):
			os.system('wget -q --header="User-Agent: FF%%20EXVIUS/2.1.1 CFNetwork/808.2.16 Darwin/16.3.0" -O %s/%s %s'%(self.mst,local_name,self.base_mst%(download_name) if '_MST' in file else self.base_txt%(download_name)))

	def getFileContent(self,file,MST=False):
		clean_filename= self.tools.cleanName(file)
		file_key=self.tools.findFileKey(clean_filename)
		with open('%s/%s'%(self.mst,file)) as data_file:    
			data = data_file.readlines()
			rr=[]
			if MST:
				rr.append('[')
			for l in data:
				if MST:
					rr.append(self.tools.decrypt(l,file_key)+',' if l <> data[-1] else self.tools.decrypt(l,file_key))
				else:
					rr.append(self.tools.decrypt(l,file_key))
			if MST:
				rr.append(']')
			self.save(rp(''.join(rr)),'%s/%s.json'%(self.mst,clean_filename))

	def parseMissionTypes(self):
		target='%s/F_MISSION_MST.json'%(self.mst)
		if self.isFolder(target):
			_t={}
			with open(target) as data_file:    
				data = json.load(data_file)
				for m in data:
					B6kyCQ9M=int(m['B6kyCQ9M'])#energy use
					qo3PECw6=int(m['qo3PECw6'])#mission id
					Y4VoF8yu=int(m['Y4VoF8yu'])
					v8xi6Xvyk=int(m['8xi6Xvyk'])
					_t[qo3PECw6]={}
					_t[qo3PECw6]['type']=Y4VoF8yu
					_t[qo3PECw6]['energy']=B6kyCQ9M
					_t[qo3PECw6]['rounds']=v8xi6Xvyk
				self.save('# -*- coding: utf-8 -*-\nmission_types=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'mission_types_%s.py'%('gl' if self.region == 1 else 'jp'))
				
	def parseItemNames(self):
		fin={}
		if self.region==1:
			target='%s/F_TEXT_ITEM_NAME.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:    
					data = data_file.readlines()
					for l in data:
						l=l.rstrip().split('^')
						if len(l[0]) >=1:
							try:
								cn= self.cleanMissionName(l[0])
								fin[cn]={}
								fin[cn]['name']=l[1]
							except:
								pass
					self.save('# -*- coding: utf-8 -*-\nitems=%s'%fin,'item_names_%s.py'%('gl' if self.region == 1 else 'jp'))
		else:
			target='%s/F_ITEM_MST.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:
					data = json.load(data_file)
					for m in data:
						G4L0YIB2=m['G4L0YIB2']#name
						tL6G9egd=str(m['tL6G9egd'])#id
						fin[tL6G9egd]={}
						fin[tL6G9egd]['name']=G4L0YIB2
					self.save('# -*- coding: utf-8 -*-\nitems=%s'%fin,'item_names_%s.py'%('gl' if self.region == 1 else 'jp'))

	def parseMissionNames(self):
		fin={}
		if self.region==1:
			target='%s/F_TEXT_MISSION.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:
					data = data_file.readlines()
					for l in data:
						l=l.rstrip().split('^')
						if len(l[0]) >=1:
							try:
								cn= self.cleanMissionName(l[0])
								fin[cn]={}
								fin[cn]['name']=l[1].decode('utf-8')
							except:
								pass
					self.save('# -*- coding: utf-8 -*-\nmissions=%s'%self.ensure_unicode(unicode(json.dumps(fin, ensure_ascii=False))),'mission_names_%s.py'%('gl' if self.region == 1 else 'jp'))
		else:
			target='%s/F_MISSION_MST.json'%(self.mst)
			if self.isFolder(target):
				with open(target) as data_file:    
					data = json.load(data_file)
					for m in data:
						G4L0YIB2=m['G4L0YIB2']#name
						qo3PECw6=str(m['qo3PECw6'])#id
						fin[qo3PECw6]={}
						fin[qo3PECw6]['name']=G4L0YIB2
					self.save('# -*- coding: utf-8 -*-\nmissions=%s'%unicode(json.dumps(fin, ensure_ascii=False)),'mission_names_%s.py'%('gl' if self.region == 1 else 'jp'))

	def parseLevels(self):
		_t={}
		target='%s/F_TEAM_LV_MST.json'%(self.mst)
		if self.isFolder(target):
			with open(target) as data_file:
				data = json.load(data_file)
				for m in data:
					qo3PECw6=int(m['7wV3QZ80'])#energy use
					Z0EN6jSh=int(m['B6H34Mea'])#energy use
					if qo3PECw6 in _t:
						_t[qo3PECw6]=Z0EN6jSh
					else:
						_t[qo3PECw6]={}
						_t[qo3PECw6]=Z0EN6jSh
				self.save('# -*- coding: utf-8 -*-\nlevels=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'levels_%s.py'%('gl' if self.region == 1 else 'jp'))
				
	def parseUnit(self):
		_t={}
		target='%s/F_UNIT_MST.json'%(self.mst)
		if self.isFolder(target):
			with open(target) as data_file:
				data = json.load(data_file)
				for m in data:
					u18nfD7p=int(m['u18nfD7p'])#price
					woghJa61=str(m['3HriTp6B'])#unit id
					_t[woghJa61]={}
					_t[woghJa61]['price']=u18nfD7p
				self.save('# -*- coding: utf-8 -*-\nunits=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'units_%s.py'%('gl' if self.region == 1 else 'jp'))

	def parseChallenges(self):
		_t={}
		target='%s/F_CHALLENGE_MST.json'%(self.mst)
		if self.isFolder(target):
			with open(target) as data_file:
				data = json.load(data_file)
				for m in data:
					qo3PECw6=int(m['qo3PECw6'])
					Pzn5h0Ga=str(m['Pzn5h0Ga'])
					Z0EN6jSh=int(m['Z0EN6jSh'])
					if qo3PECw6 in _t:
						_t[qo3PECw6][Z0EN6jSh]=Pzn5h0Ga
					else:
						_t[qo3PECw6]={}
						_t[qo3PECw6][Z0EN6jSh]=Pzn5h0Ga
				self.save('# -*- coding: utf-8 -*-\nchallenges=%s'%unicode(json.dumps(_t, ensure_ascii=False)),'challenges_%s.py'%('gl' if self.region == 1 else 'jp'))

	def cleanMissionName(self,n):
		return re.sub('.*NAME_','',n)

	def unpackAll(self):
		for file in os.listdir(self.mst):
			if '.dat' in file and ('_MST' in file or 'F_TEXT_' in file):
				self.getFileContent(file,'_MST' in file)

	def findMST(self):
		for i in self.updateData:
			if i['a4hXTIm0']=='F_MST_VERSION':
				self.log('found MST:%s'%(i['wM9AfX6I']))
				self.mst=i['wM9AfX6I']

if __name__ == "__main__":
	u=Updater(2)
	u.setTT([{"a4hXTIm0":"F_MST_VERSION","wM9AfX6I":"4412","dT2gJ1vH":"","D0f6Cn7Q":""},{"a4hXTIm0":"F_ABILITY_EXPLAIN_MST","wM9AfX6I":"640","dT2gJ1vH":"3537938","D0f6Cn7Q":"183b712f6f481e7b19e29811541e5847"},{"a4hXTIm0":"F_ABILITY_MST","wM9AfX6I":"1035","dT2gJ1vH":"10578431","D0f6Cn7Q":"ac0fda97d34c49e01a868cebd6d105a9"},{"a4hXTIm0":"F_AI_MST","wM9AfX6I":"411","dT2gJ1vH":"10600654","D0f6Cn7Q":"3bac88c5137c27efbbfb3994e2eed761"},{"a4hXTIm0":"F_ARCHIVE_MST","wM9AfX6I":"34","dT2gJ1vH":"30332","D0f6Cn7Q":"25b020c835b885e4ed940c7e1fcc3869"},{"a4hXTIm0":"F_AREA_MST","wM9AfX6I":"418","dT2gJ1vH":"146294","D0f6Cn7Q":"16ad9ef4794a49260ffb055b71a350ac"},{"a4hXTIm0":"F_AWARD_EXPLAIN_MST","wM9AfX6I":"27","dT2gJ1vH":"7851","D0f6Cn7Q":"35304f3a33eee8643574a91ea69a587e"},{"a4hXTIm0":"F_AWARD_MST","wM9AfX6I":"26","dT2gJ1vH":"6215","D0f6Cn7Q":"70290e05dd3da5eda97951aa71a83f29"},{"a4hXTIm0":"F_AWARD_TYPE_MST","wM9AfX6I":"26","dT2gJ1vH":"654","D0f6Cn7Q":"48d8f097b31d4c9a98441fdca678d36f"},{"a4hXTIm0":"F_BANNER_MST","wM9AfX6I":"599","dT2gJ1vH":"126755","D0f6Cn7Q":"07e1ba9bf385d3265669481438accb70"},{"a4hXTIm0":"F_BATTLE_BG_MST","wM9AfX6I":"203","dT2gJ1vH":"127344","D0f6Cn7Q":"08632fa12eb2ed58c0af083b042c8b61"},{"a4hXTIm0":"F_BATTLE_SCRIPT_MST","wM9AfX6I":"312","dT2gJ1vH":"1550594","D0f6Cn7Q":"2bb75fa21e62132fac1654dd8c01e5fd"},{"a4hXTIm0":"F_BEAST_BOARD_PIECE_EXT_MST","wM9AfX6I":"19","dT2gJ1vH":"109","D0f6Cn7Q":"0771dc2a9ee8612f5dbdf6daa63f4b70"},{"a4hXTIm0":"F_BEAST_BOARD_PIECE_MST","wM9AfX6I":"71","dT2gJ1vH":"276839","D0f6Cn7Q":"a956414e99c9f7ab8770c81f17be9645"},{"a4hXTIm0":"F_BEAST_CLASS_UP_MST","wM9AfX6I":"53","dT2gJ1vH":"7224","D0f6Cn7Q":"2914b05fb25afb5bfd8e47289412206a"},{"a4hXTIm0":"F_BEAST_CP_MST","wM9AfX6I":"64","dT2gJ1vH":"16780","D0f6Cn7Q":"9de56ce7de8b90ad96ebc85fe91a21fc"},{"a4hXTIm0":"F_BEAST_EXPLAIN_MST","wM9AfX6I":"54","dT2gJ1vH":"9688","D0f6Cn7Q":"e7fa2f19ef2491b0faaed509f747c2b3"},{"a4hXTIm0":"F_BEAST_EXP_PATTERN_MST","wM9AfX6I":"30","dT2gJ1vH":"57530","D0f6Cn7Q":"535cfeec96cce0b896b6831c2989a060"},{"a4hXTIm0":"F_BEAST_GROW_MST","wM9AfX6I":"24","dT2gJ1vH":"33550","D0f6Cn7Q":"8cfe30208919afeb3be7ca7561d6d5c8"},{"a4hXTIm0":"F_BEAST_MST","wM9AfX6I":"49","dT2gJ1vH":"4403","D0f6Cn7Q":"ffa2d242e666f7bd7c48f20a15dd65fd"},{"a4hXTIm0":"F_BEAST_SKILL_MST","wM9AfX6I":"69","dT2gJ1vH":"38332","D0f6Cn7Q":"cb35d39993610908ea660d4102a2304c"},{"a4hXTIm0":"F_BEAST_STATUS_MST","wM9AfX6I":"67","dT2gJ1vH":"37280","D0f6Cn7Q":"f13207d606e453fda96cde3de93277f9"},{"a4hXTIm0":"F_CAPTURE_MST","wM9AfX6I":"492","dT2gJ1vH":"1255512","D0f6Cn7Q":"dc0785e36d8d42746e4b3909e9faca80"},{"a4hXTIm0":"F_CHALLENGE_COMPLETE_REWARD_MST","wM9AfX6I":"22","dT2gJ1vH":"0","D0f6Cn7Q":"d41d8cd98f00b204e9800998ecf8427e"},{"a4hXTIm0":"F_CHALLENGE_MST","wM9AfX6I":"407","dT2gJ1vH":"6170386","D0f6Cn7Q":"5cadf60c8d705851eb167bcc27624277"},{"a4hXTIm0":"F_CHARACTER_MST","wM9AfX6I":"34","dT2gJ1vH":"4292","D0f6Cn7Q":"e9783747cbfaebb8dc1046dcded83716"},{"a4hXTIm0":"F_CLSM_GRADE_MST","wM9AfX6I":"21","dT2gJ1vH":"218","D0f6Cn7Q":"89ea7f7b3e3849016e258c3acd983541"},{"a4hXTIm0":"F_CLSM_PROGRESS_MST","wM9AfX6I":"20","dT2gJ1vH":"7650","D0f6Cn7Q":"487b48c3c8f6111fad8d5f4019066d1a"},{"a4hXTIm0":"F_CLSM_RANK_MST","wM9AfX6I":"20","dT2gJ1vH":"865","D0f6Cn7Q":"02b5a752ed37c083fb349b1fd127274d"},{"a4hXTIm0":"F_CLSM_ROUND_MST","wM9AfX6I":"21","dT2gJ1vH":"13810","D0f6Cn7Q":"16b5772f9ec700d8630cd39d03173569"},{"a4hXTIm0":"F_CRAFT_EXT_MST","wM9AfX6I":"21","dT2gJ1vH":"1248","D0f6Cn7Q":"357b10d0a4984597ed1d94a26a4678a4"},{"a4hXTIm0":"F_CREST_SWITCH_MST","wM9AfX6I":"20","dT2gJ1vH":"981","D0f6Cn7Q":"2d9563b00367b55a411cfbc310591006"},{"a4hXTIm0":"F_DEFINE_MST","wM9AfX6I":"131","dT2gJ1vH":"29076","D0f6Cn7Q":"c598785093fc744f7ebfdf7e32964c75"},{"a4hXTIm0":"F_DESCRIPTION_FORMAT_MST","wM9AfX6I":"486","dT2gJ1vH":"2773996","D0f6Cn7Q":"98186ee7bd1a2ceda4822422e403dfd1"},{"a4hXTIm0":"F_DIAMOND_MST","wM9AfX6I":"24","dT2gJ1vH":"11638","D0f6Cn7Q":"ead361938e9a1edbc92d8b0e092f5d03"},{"a4hXTIm0":"F_DIAMOND_REWARD_MST","wM9AfX6I":"4","dT2gJ1vH":"3600","D0f6Cn7Q":"db04cef49a79a7f15f2235ca34311e88"},{"a4hXTIm0":"F_DUNGEON_MST","wM9AfX6I":"518","dT2gJ1vH":"599811","D0f6Cn7Q":"104f7ed4d4e721b02573d3bcd6fdcf54"},{"a4hXTIm0":"F_EFFECT_GROUP_MST","wM9AfX6I":"366","dT2gJ1vH":"2456249","D0f6Cn7Q":"7966ec6466ca133ee56d6cba8bfb38ef"},{"a4hXTIm0":"F_EFFECT_MST","wM9AfX6I":"294","dT2gJ1vH":"1325965","D0f6Cn7Q":"f6257d5642d922fcbcf9a324fe58adf8"},{"a4hXTIm0":"F_EMBLEM_ITEM_MST","wM9AfX6I":"20","dT2gJ1vH":"9518","D0f6Cn7Q":"08ea7310f7ed9125f5bfa1a16022e387"},{"a4hXTIm0":"F_ENCOUNT_FIELD_MST","wM9AfX6I":"23","dT2gJ1vH":"6420","D0f6Cn7Q":"b678bdfa30d5a5d7126d55ea5ed69bf8"},{"a4hXTIm0":"F_ENCOUNT_MONSTER_EXT_MST","wM9AfX6I":"20","dT2gJ1vH":"4389","D0f6Cn7Q":"9138f841ebd9159736fbd13732819099"},{"a4hXTIm0":"F_ENCOUNT_MST","wM9AfX6I":"92","dT2gJ1vH":"937122","D0f6Cn7Q":"4f853f184696e863be5820a699526bd5"},{"a4hXTIm0":"F_EQUIP_ITEM_CONDITION_MST","wM9AfX6I":"5","dT2gJ1vH":"173","D0f6Cn7Q":"f29808b589750b2138b314246821dd6e"},{"a4hXTIm0":"F_EQUIP_ITEM_EXPLAIN_MST","wM9AfX6I":"292","dT2gJ1vH":"875942","D0f6Cn7Q":"f04e0e9dabd0770407c3555bbef31876"},{"a4hXTIm0":"F_EQUIP_ITEM_MST","wM9AfX6I":"367","dT2gJ1vH":"1257834","D0f6Cn7Q":"02695a9eed2138dfd6d53d4d79ba1026"},{"a4hXTIm0":"F_EXCHANGE_SHOP_ITEM_MST","wM9AfX6I":"20","dT2gJ1vH":"1085","D0f6Cn7Q":"b65696c7fde136f555eb4991922d4076"},{"a4hXTIm0":"F_EXCHANGE_SHOP_MST","wM9AfX6I":"19","dT2gJ1vH":"198","D0f6Cn7Q":"95236051edfe684dc99d2506642a78ee"},{"a4hXTIm0":"F_EXPLORE_AREA_MST","wM9AfX6I":"16","dT2gJ1vH":"7346","D0f6Cn7Q":"9a9a4f16a3ccad9a80d10778933309f0"},{"a4hXTIm0":"F_EXPLORE_TIME_MST","wM9AfX6I":"19","dT2gJ1vH":"516","D0f6Cn7Q":"56579592512103903f0d7dc1a9ab9c19"},{"a4hXTIm0":"F_EXVIUS_POINT_REWARD_MST","wM9AfX6I":"24","dT2gJ1vH":"3311","D0f6Cn7Q":"b554f7dbdebd901558579258168ddf09"},{"a4hXTIm0":"F_FIELD_TREASURE_MST","wM9AfX6I":"102","dT2gJ1vH":"321666","D0f6Cn7Q":"890f0e16a7ddf5bb2e7ee9a6ab79b240"},{"a4hXTIm0":"F_FOOTPRINT_MST","wM9AfX6I":"30","dT2gJ1vH":"2561","D0f6Cn7Q":"d7f3ea6a188c76b818d96c27e54432b1"},{"a4hXTIm0":"F_FUNCTION_MST","wM9AfX6I":"30","dT2gJ1vH":"1548","D0f6Cn7Q":"039073605d038eca586e5df772d09adf"},{"a4hXTIm0":"F_GACHA_EFFECT_BLOCK_MST","wM9AfX6I":"23","dT2gJ1vH":"4511","D0f6Cn7Q":"ec432e3eaae35d1ecfb0090cc3a1b789"},{"a4hXTIm0":"F_GACHA_EFFECT_PATTERN_MST","wM9AfX6I":"299","dT2gJ1vH":"110389","D0f6Cn7Q":"d14210781b5d425085d676bca3df9f4a"},{"a4hXTIm0":"F_GACHA_SELECT_UNIT_MST","wM9AfX6I":"164","dT2gJ1vH":"22317","D0f6Cn7Q":"da837d424beed1e365270cbc2ed066f9"},{"a4hXTIm0":"F_GALLERY_MST","wM9AfX6I":"5","dT2gJ1vH":"1110","D0f6Cn7Q":"4852d74c8311797a6164991cfff538f7"},{"a4hXTIm0":"F_GAME_TITLE_MST","wM9AfX6I":"56","dT2gJ1vH":"7094","D0f6Cn7Q":"cef6fd1faf79dfc2de97d6aae893a67c"},{"a4hXTIm0":"F_GUEST_UNIT_MST","wM9AfX6I":"51","dT2gJ1vH":"71407","D0f6Cn7Q":"d083051dda0afe3cea2aa2aa26ec3871"},{"a4hXTIm0":"F_HERO_MST","wM9AfX6I":"77","dT2gJ1vH":"26010","D0f6Cn7Q":"0ca9b349148a7749f9cd76cffe4796ef"},{"a4hXTIm0":"F_ICON_MST","wM9AfX6I":"425","dT2gJ1vH":"536036","D0f6Cn7Q":"911d309118aadc51ac678d18d9c613c9"},{"a4hXTIm0":"F_IMAGE_SWITCHING_MST","wM9AfX6I":"42","dT2gJ1vH":"4645","D0f6Cn7Q":"47b3a291cb3bbdcd3222801076c1fe98"},{"a4hXTIm0":"F_IMPORTANT_ITEM_EXPLAIN_MST","wM9AfX6I":"52","dT2gJ1vH":"10750","D0f6Cn7Q":"ecb36618c6805b21238149fc36ad4c4a"},{"a4hXTIm0":"F_IMPORTANT_ITEM_MST","wM9AfX6I":"54","dT2gJ1vH":"7230","D0f6Cn7Q":"cb512621d78f5051ed098ecb41430c4a"},{"a4hXTIm0":"F_ITEM_EXPLAIN_MST","wM9AfX6I":"269","dT2gJ1vH":"565888","D0f6Cn7Q":"d4c15dfc5eba63aeb5c98bab6921a19e"},{"a4hXTIm0":"F_ITEM_EXT_BEAST_MST","wM9AfX6I":"45","dT2gJ1vH":"486954","D0f6Cn7Q":"9380c5050b83ddfde58cf2f8362a79cb"},{"a4hXTIm0":"F_ITEM_MST","wM9AfX6I":"286","dT2gJ1vH":"577424","D0f6Cn7Q":"16a7d685ce699a6fc6f5541cc7094f8c"},{"a4hXTIm0":"F_JOB_MST","wM9AfX6I":"188","dT2gJ1vH":"23272","D0f6Cn7Q":"487570cc56edd8e7b8addf496754f701"},{"a4hXTIm0":"F_LAND_EXPLAIN_MST","wM9AfX6I":"19","dT2gJ1vH":"89","D0f6Cn7Q":"febef74407dc0709874f3a91fe0bf92b"},{"a4hXTIm0":"F_LAND_MST","wM9AfX6I":"58","dT2gJ1vH":"9675","D0f6Cn7Q":"1e338049c4df91e0106d9c8908493936"},{"a4hXTIm0":"F_LEARNING_MST","wM9AfX6I":"20","dT2gJ1vH":"5418","D0f6Cn7Q":"dc7312c04ae8325ba64e89d6f5f92838"},{"a4hXTIm0":"F_LIMITBURST_LV_MST","wM9AfX6I":"301","dT2gJ1vH":"6659630","D0f6Cn7Q":"fe14a78c91b7f9abdf3d5933e204b24c"},{"a4hXTIm0":"F_LIMITBURST_MST","wM9AfX6I":"380","dT2gJ1vH":"1441002","D0f6Cn7Q":"7978530ddb2a05cdb21ecf4dfbe112c5"},{"a4hXTIm0":"F_LOCATION_GOAL_MST","wM9AfX6I":"21","dT2gJ1vH":"129","D0f6Cn7Q":"bbf1dacb6d88628e489cc908a9d75637"},{"a4hXTIm0":"F_LOGIN_BONUS_MST","wM9AfX6I":"50","dT2gJ1vH":"155870","D0f6Cn7Q":"353660daaa83f1cead6705d2d741e3ef"},{"a4hXTIm0":"F_LOGIN_BONUS_SP_MST","wM9AfX6I":"97","dT2gJ1vH":"9371","D0f6Cn7Q":"bedb68c76d42852aef4a2c4c9e6dbcb2"},{"a4hXTIm0":"F_LOGIN_BONUS_SP_REWARD_MST","wM9AfX6I":"70","dT2gJ1vH":"223080","D0f6Cn7Q":"e2c2b072840528cbf9fc8458c2a10110"},{"a4hXTIm0":"F_LOGIN_BONUS_TOTAL_REWARD_MST","wM9AfX6I":"29","dT2gJ1vH":"16748","D0f6Cn7Q":"667164bfd7432240ab979cfe70d83498"},{"a4hXTIm0":"F_MAGIC_EXPLAIN_MST","wM9AfX6I":"112","dT2gJ1vH":"57581","D0f6Cn7Q":"605a8b48bf1a37ac397befb8c45f68d0"},{"a4hXTIm0":"F_MAGIC_MST","wM9AfX6I":"125","dT2gJ1vH":"210025","D0f6Cn7Q":"448540192d9619b30c291f97e4423cfd"},{"a4hXTIm0":"F_MAP_EVENT_MST","wM9AfX6I":"137","dT2gJ1vH":"189439","D0f6Cn7Q":"c4b7a9222a8e4f9d2ad5914370e91cee"},{"a4hXTIm0":"F_MAP_EXT_RESOURCE_MST","wM9AfX6I":"140","dT2gJ1vH":"93792","D0f6Cn7Q":"437407a1cb31fd1e9e28fe4b3190f7b2"},{"a4hXTIm0":"F_MAP_OBJECT_MST","wM9AfX6I":"22","dT2gJ1vH":"4803","D0f6Cn7Q":"3716eb0a721c08d812dbe377fcee4357"},{"a4hXTIm0":"F_MAP_ROUTE_MST","wM9AfX6I":"99","dT2gJ1vH":"70706","D0f6Cn7Q":"dbf8dcf01a260c201ab95422a6b3432c"},{"a4hXTIm0":"F_MATERIA_EXPLAIN_MST","wM9AfX6I":"302","dT2gJ1vH":"173103","D0f6Cn7Q":"503e776826f325494eec0a4d0bfbd3b0"},{"a4hXTIm0":"F_MATERIA_MST","wM9AfX6I":"327","dT2gJ1vH":"313175","D0f6Cn7Q":"15ab78161a719a5f58f6288c09734aad"},{"a4hXTIm0":"F_MEDAL_EXCHANGE_MST","wM9AfX6I":"179","dT2gJ1vH":"831044","D0f6Cn7Q":"56f6a839df4bce4633e34e02d9f8e5d4"},{"a4hXTIm0":"F_MISSION_MST","wM9AfX6I":"632","dT2gJ1vH":"6483581","D0f6Cn7Q":"893210f285971cf122c803d0586d58e6"},{"a4hXTIm0":"F_MISSION_NOTICE_MST","wM9AfX6I":"13","dT2gJ1vH":"14062","D0f6Cn7Q":"e7839e3872cbb6c9450f8f08eb7f64ba"},{"a4hXTIm0":"F_MONSTER_DICTIONARY_EXPLAIN_MST","wM9AfX6I":"352","dT2gJ1vH":"1360323","D0f6Cn7Q":"4c352292973f4e28c38b25138676a254"},{"a4hXTIm0":"F_MONSTER_DICTIONARY_MST","wM9AfX6I":"366","dT2gJ1vH":"500744","D0f6Cn7Q":"37ecd662e2af17ca224a4e1c0e09645c"},{"a4hXTIm0":"F_MONSTER_PASSIVE_SKILL_MST","wM9AfX6I":"94","dT2gJ1vH":"26263","D0f6Cn7Q":"ecedb665912c8b9fd3f7f330bf73e8ce"},{"a4hXTIm0":"F_MONSTER_PASSIVE_SKILL_SET_MST","wM9AfX6I":"98","dT2gJ1vH":"14263","D0f6Cn7Q":"b5c208a93f854dbdcc25d47fc901b0f1"},{"a4hXTIm0":"F_MONSTER_SKILL_MST","wM9AfX6I":"567","dT2gJ1vH":"6199806","D0f6Cn7Q":"97ec2488a32f2138fa3955c95d7eac7f"},{"a4hXTIm0":"F_MONSTER_SKILL_SET_MST","wM9AfX6I":"341","dT2gJ1vH":"638780","D0f6Cn7Q":"5f01236e24e2e8ff1bc05edda32acf9b"},{"a4hXTIm0":"F_MONSTER_UNIQUE_ANIME_MST","wM9AfX6I":"19","dT2gJ1vH":"474","D0f6Cn7Q":"01e1e94e1707a76adc363461b992f62b"},{"a4hXTIm0":"F_NPC_MST","wM9AfX6I":"198","dT2gJ1vH":"180265","D0f6Cn7Q":"fa56d388b089a4df040b36229e0b9112"},{"a4hXTIm0":"F_PICTURE_STORY_MST","wM9AfX6I":"112","dT2gJ1vH":"21898","D0f6Cn7Q":"7698c6794edea64d4a2665149a48c374"},{"a4hXTIm0":"F_PLAYBACK_CHAPTER_MST","wM9AfX6I":"38","dT2gJ1vH":"7282","D0f6Cn7Q":"06680daf3c96658342fa98fe95201bb9"},{"a4hXTIm0":"F_PLAYBACK_EVENT_MST","wM9AfX6I":"57","dT2gJ1vH":"418146","D0f6Cn7Q":"86647f508dbca3c5f205e2df1bd8aa91"},{"a4hXTIm0":"F_PLAYBACK_MAP_MST","wM9AfX6I":"34","dT2gJ1vH":"90267","D0f6Cn7Q":"e3268c5e55b55924e0b79430f955bf2d"},{"a4hXTIm0":"F_PLAYBACK_SEASON_MST","wM9AfX6I":"21","dT2gJ1vH":"346","D0f6Cn7Q":"85c6fb6cb39df37d4b5d05a1d9249f42"},{"a4hXTIm0":"F_PURCHASE_AGE_LIMIT_MST","wM9AfX6I":"19","dT2gJ1vH":"307","D0f6Cn7Q":"6803e28cf47bfafe820713d5afbf3fb6"},{"a4hXTIm0":"F_QUEST_MST","wM9AfX6I":"112","dT2gJ1vH":"111777","D0f6Cn7Q":"515b1cb293ba757bfce83ddfa1022c13"},{"a4hXTIm0":"F_QUEST_SUB_MST","wM9AfX6I":"120","dT2gJ1vH":"268063","D0f6Cn7Q":"bce8e234371f942304c582a8ff8171f2"},{"a4hXTIm0":"F_RANKUP_REWARD_MST","wM9AfX6I":"12","dT2gJ1vH":"3174","D0f6Cn7Q":"7076c5b425ba180718083767fd2e4086"},{"a4hXTIm0":"F_RB_ABILITY_GROUP_MST","wM9AfX6I":"179","dT2gJ1vH":"28402","D0f6Cn7Q":"46a41f8792bd6ec7b325a778700e3c26"},{"a4hXTIm0":"F_RB_AI_PATTERN_MST","wM9AfX6I":"22","dT2gJ1vH":"796","D0f6Cn7Q":"6f3fc0d9bfc2d7823752b5553779e52e"},{"a4hXTIm0":"F_RB_BONUS_RULE_MST","wM9AfX6I":"21","dT2gJ1vH":"237","D0f6Cn7Q":"7b3d3b584de0920b1a60d2c4158b1f49"},{"a4hXTIm0":"F_RB_DEFINE_MST","wM9AfX6I":"22","dT2gJ1vH":"281","D0f6Cn7Q":"7d83d9c10ebab728795da9cb1827f469"},{"a4hXTIm0":"F_RB_FORBIDDEN_INFO_MST","wM9AfX6I":"24","dT2gJ1vH":"2712","D0f6Cn7Q":"424e26e2d7c218374ff82129f2acb8fa"},{"a4hXTIm0":"F_RB_LS_MST","wM9AfX6I":"82","dT2gJ1vH":"5881","D0f6Cn7Q":"c7b8bc59090b6adbdf8e0dcdfb14542d"},{"a4hXTIm0":"F_RB_LS_REWARD_MST","wM9AfX6I":"65","dT2gJ1vH":"61755","D0f6Cn7Q":"cdf6ed681da430cb91a0e86613675978"},{"a4hXTIm0":"F_RB_SS_MST","wM9AfX6I":"168","dT2gJ1vH":"135541","D0f6Cn7Q":"e93974fbcd67d04b332d9d37073f6a9e"},{"a4hXTIm0":"F_RB_SS_REWARD_MST","wM9AfX6I":"156","dT2gJ1vH":"486828","D0f6Cn7Q":"73b54959e9cfd76edf39585a2bc8c956"},{"a4hXTIm0":"F_RB_TRADE_BOARD_MST","wM9AfX6I":"23","dT2gJ1vH":"763","D0f6Cn7Q":"42dc1b343dc0a463c2931b808258adad"},{"a4hXTIm0":"F_RB_TRADE_BOARD_PIECE_MST","wM9AfX6I":"25","dT2gJ1vH":"75953","D0f6Cn7Q":"d1940923d46341e2138b28f12d63c925"},{"a4hXTIm0":"F_RECIPE_BOOK_MST","wM9AfX6I":"184","dT2gJ1vH":"134838","D0f6Cn7Q":"41d0537f42df3562df647569f3bb594f"},{"a4hXTIm0":"F_RECIPE_MST","wM9AfX6I":"213","dT2gJ1vH":"250402","D0f6Cn7Q":"8ead13c445b2f30b41d123b2dd970e30"},{"a4hXTIm0":"F_RESOURCE_MAP_MST","wM9AfX6I":"383","dT2gJ1vH":"413450","D0f6Cn7Q":"8ffeaeb6c4c3e744adb3fae9821f9d88"},{"a4hXTIm0":"F_RESOURCE_MST","wM9AfX6I":"208","dT2gJ1vH":"45621","D0f6Cn7Q":"42419a2acad3794eb2b3c07f992c8433"},{"a4hXTIm0":"F_RULE_MST","wM9AfX6I":"78","dT2gJ1vH":"25431","D0f6Cn7Q":"88c86ea668941cd47b51b1a6271e811f"},{"a4hXTIm0":"F_SACRIFICE_MST","wM9AfX6I":"112","dT2gJ1vH":"19511","D0f6Cn7Q":"c0f9c7ea478221eaf0d12b4c2273a48f"},{"a4hXTIm0":"F_SCENARIO_BATTLE_GROUP_MST","wM9AfX6I":"184","dT2gJ1vH":"144016","D0f6Cn7Q":"4d47a731e584adaff34ca91761ee7c1c"},{"a4hXTIm0":"F_SCENARIO_BATTLE_MST","wM9AfX6I":"172","dT2gJ1vH":"97476","D0f6Cn7Q":"cc9bbc917149ffb914579ecb617b0a38"},{"a4hXTIm0":"F_SEASON_EVENT_ABILITY_MST","wM9AfX6I":"206","dT2gJ1vH":"49554","D0f6Cn7Q":"329be10e8254704569d874bfe29d2081"},{"a4hXTIm0":"F_SEASON_EVENT_ABILITY_TYPE_MST","wM9AfX6I":"202","dT2gJ1vH":"29565","D0f6Cn7Q":"6fbcc9c03d57e50943467df3efaff3a7"},{"a4hXTIm0":"F_SEASON_EVENT_GROUP_FRIEND_LV_MST","wM9AfX6I":"33","dT2gJ1vH":"8190","D0f6Cn7Q":"527d44f766011bb4a17b577f46a75810"},{"a4hXTIm0":"F_SHOP_MST","wM9AfX6I":"30","dT2gJ1vH":"2808","D0f6Cn7Q":"e0a269a644d84f7392fefe5393ba387f"},{"a4hXTIm0":"F_SKILL_SUBLIMATION_BOARD_MST","wM9AfX6I":"19","dT2gJ1vH":"0","D0f6Cn7Q":"d41d8cd98f00b204e9800998ecf8427e"},{"a4hXTIm0":"F_SKILL_SUBLIMATION_PIECE_MST","wM9AfX6I":"16","dT2gJ1vH":"0","D0f6Cn7Q":"d41d8cd98f00b204e9800998ecf8427e"},{"a4hXTIm0":"F_SOUND_MST","wM9AfX6I":"19","dT2gJ1vH":"1290","D0f6Cn7Q":"e0f2185d767b4e943587ee59e54dd6e8"},{"a4hXTIm0":"F_SP_CHALLENGE_MST","wM9AfX6I":"91","dT2gJ1vH":"420731","D0f6Cn7Q":"6864103158679f3df5723cc86ced65a4"},{"a4hXTIm0":"F_STORE_ITEM_MST","wM9AfX6I":"177","dT2gJ1vH":"448920","D0f6Cn7Q":"2878d88f3e80c044d847ea519333baf7"},{"a4hXTIm0":"F_STORY_EVENT_MST","wM9AfX6I":"155","dT2gJ1vH":"321666","D0f6Cn7Q":"9b939807680eb9e8dabf6b9e2b494bf0"},{"a4hXTIm0":"F_STORY_FLOW_MST","wM9AfX6I":"19","dT2gJ1vH":"410","D0f6Cn7Q":"765d7cd740c06aa2e47399ce8f8e56cf"},{"a4hXTIm0":"F_STORY_MST","wM9AfX6I":"53","dT2gJ1vH":"2160","D0f6Cn7Q":"bec87e4fe52b2a869f55fa004c436ca3"},{"a4hXTIm0":"F_STORY_SUB_MST","wM9AfX6I":"92","dT2gJ1vH":"105641","D0f6Cn7Q":"27b23c875779d7cccf2ddb7db46fed7b"},{"a4hXTIm0":"F_STRONGBOX_MST","wM9AfX6I":"46","dT2gJ1vH":"17563","D0f6Cn7Q":"d964337d3b4dca03b99438a4dd48cc44"},{"a4hXTIm0":"F_SUBLIMATION_RECIPE_MST","wM9AfX6I":"124","dT2gJ1vH":"841808","D0f6Cn7Q":"0158f54e88beff3d860313c3e4978ab7"},{"a4hXTIm0":"F_SWITCH_MST","wM9AfX6I":"465","dT2gJ1vH":"1176655","D0f6Cn7Q":"e9c7290eca7829ab83df4c4d04cf8cae"},{"a4hXTIm0":"F_SWITCH_TYPE_MST","wM9AfX6I":"21","dT2gJ1vH":"4115","D0f6Cn7Q":"9ead115fc4292d260c761f7a99d0c83b"},{"a4hXTIm0":"F_TEAM_LV_MST","wM9AfX6I":"49","dT2gJ1vH":"116834","D0f6Cn7Q":"4545b9a5cca8892844e2058dea436996"},{"a4hXTIm0":"F_TELEPO_MST","wM9AfX6I":"88","dT2gJ1vH":"47422","D0f6Cn7Q":"e7917da7a1a590c336b14c20326c8ba4"},{"a4hXTIm0":"F_TICKER_DEFINE_MESSAGE_MST","wM9AfX6I":"15","dT2gJ1vH":"109","D0f6Cn7Q":"0998ce78d526570fcd15e27cd4bd0b8d"},{"a4hXTIm0":"F_TICKER_LOG_CATEGORY_MST","wM9AfX6I":"19","dT2gJ1vH":"1791","D0f6Cn7Q":"e327a85ffcf59374f8a8dafcafb1c2e6"},{"a4hXTIm0":"F_TICKER_MST","wM9AfX6I":"41","dT2gJ1vH":"18755","D0f6Cn7Q":"f777152f3b3c6864ef17a11e93ff9bc5"},{"a4hXTIm0":"F_TICKET_MST","wM9AfX6I":"51","dT2gJ1vH":"7017","D0f6Cn7Q":"178b85985a8556d1f83c6086edb6d2e4"},{"a4hXTIm0":"F_TITLE_MST","wM9AfX6I":"19","dT2gJ1vH":"445","D0f6Cn7Q":"90c79942ed5288dbc761e63909a6cd47"},{"a4hXTIm0":"F_TOWN_EXPLAIN_MST","wM9AfX6I":"84","dT2gJ1vH":"25213","D0f6Cn7Q":"5586ec5eeb7426dc9b5983865fa2eb2d"},{"a4hXTIm0":"F_TOWN_MST","wM9AfX6I":"127","dT2gJ1vH":"23614","D0f6Cn7Q":"8622238df280109bd20b59e94b5ada77"},{"a4hXTIm0":"F_TOWN_STORE_COMMENT_MST","wM9AfX6I":"170","dT2gJ1vH":"77252","D0f6Cn7Q":"0efedd95e171daa3ea752b3f6cb0d3aa"},{"a4hXTIm0":"F_TOWN_STORE_MST","wM9AfX6I":"174","dT2gJ1vH":"65738","D0f6Cn7Q":"308bc5a760c6afb3c67db2cd6f5e8658"},{"a4hXTIm0":"F_TRIBE_MST","wM9AfX6I":"19","dT2gJ1vH":"1068","D0f6Cn7Q":"3260403319574176da7f3b5013bd8fb1"},{"a4hXTIm0":"F_TROPHY_EXPLAIN_MST","wM9AfX6I":"20","dT2gJ1vH":"8175","D0f6Cn7Q":"c8bf47ccaa287d8f6ea29a8ece71ab67"},{"a4hXTIm0":"F_TROPHY_METER_SERIF_MST","wM9AfX6I":"19","dT2gJ1vH":"2256","D0f6Cn7Q":"9d14dbc110fda5496e1737e9635754b3"},{"a4hXTIm0":"F_TROPHY_MST","wM9AfX6I":"30","dT2gJ1vH":"26829","D0f6Cn7Q":"432b3309abb33773e01c44c52066d544"},{"a4hXTIm0":"F_TROPHY_REWARD_MST","wM9AfX6I":"26","dT2gJ1vH":"1377","D0f6Cn7Q":"fc1e109f72149abc2585e80b1f01ca90"},{"a4hXTIm0":"F_UNIT_CLASS_UP_MST","wM9AfX6I":"252","dT2gJ1vH":"231983","D0f6Cn7Q":"d89fec830e68f0c94aec283d7d878aa1"},{"a4hXTIm0":"F_UNIT_EXPLAIN_MST","wM9AfX6I":"308","dT2gJ1vH":"1989057","D0f6Cn7Q":"c800d7b01d5eceb486348913b2879ea4"},{"a4hXTIm0":"F_UNIT_EXP_PATTERN_MST","wM9AfX6I":"28","dT2gJ1vH":"74554","D0f6Cn7Q":"1cf2af68c3c65f11fdffbca63420429d"},{"a4hXTIm0":"F_UNIT_GROW_MST","wM9AfX6I":"27","dT2gJ1vH":"74704","D0f6Cn7Q":"7f6dbf3e2685670726abcdcaf27d2e23"},{"a4hXTIm0":"F_UNIT_LV_ACQUIRE_MST","wM9AfX6I":"44","dT2gJ1vH":"84404","D0f6Cn7Q":"fec0b6c0c8d50bbbcae2c5c632cefe52"},{"a4hXTIm0":"F_UNIT_MST","wM9AfX6I":"378","dT2gJ1vH":"2562567","D0f6Cn7Q":"2fd32513fa09212ebf5f2d7e9c766ea4"},{"a4hXTIm0":"F_UNIT_ROLE_MST","wM9AfX6I":"8","dT2gJ1vH":"1677","D0f6Cn7Q":"e37a3f158449b1b41a25e19e57d3df46"},{"a4hXTIm0":"F_UNIT_SERIES_LV_ACQUIRE_MST","wM9AfX6I":"306","dT2gJ1vH":"1412955","D0f6Cn7Q":"8c38a16be6773bd46f5fd7515630ce8b"},{"a4hXTIm0":"F_UNIT_SERIES_SWITCH_SKILL_MST","wM9AfX6I":"9","dT2gJ1vH":"1038","D0f6Cn7Q":"8f7c8581efade853441471d895db9adf"},{"a4hXTIm0":"F_UNIT_TRANSLATE_RATE_MST","wM9AfX6I":"5","dT2gJ1vH":"579","D0f6Cn7Q":"76d79689ffcfd48d58ee2e6dc03e0605"},{"a4hXTIm0":"F_UNIT_UNIQUE_ANIME_MST","wM9AfX6I":"254","dT2gJ1vH":"414541","D0f6Cn7Q":"c0f52583f70d0d983803ae847347640d"},{"a4hXTIm0":"F_URL_MST","wM9AfX6I":"86","dT2gJ1vH":"22721","D0f6Cn7Q":"e9839565295fc801fb0f58ce7c7698b9"},{"a4hXTIm0":"F_WORLD_MST","wM9AfX6I":"23","dT2gJ1vH":"732","D0f6Cn7Q":"b4a95284dcabe8863a2af24a58b3a801"}])