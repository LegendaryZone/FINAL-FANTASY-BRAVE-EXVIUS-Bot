from main import API,Tools
from mission_names_gl import *

_player='3D2A21DB-D06A-459C-B723-78EBE14CF3F9'
_device=1

todo=[]

a=API()
a.setPlayerID(_player,_device)
#a.setFacebook('EAARmB9evD0cBAOaZCGqbT5kYu9Db8HPpVnZAvQZCTCmZCX3JOa86qzZCIZAS9RQMr0QLxCwkMw9apeup0mcDoyrn7r1CajGoJ9lDvqFywX0Tkony7H3NWorImFdR6p8nnVQtlg3x2X5gkhmZAzQP7cis9Q9RGDtojw920GjWidkU8YszifNDdaOYjrGJQXxj9pgErAWYuBsiml18xHWlFYIxmAuuraM02uXN3IqoatNwQZDZD','1580352528642492')

a.InitializeRequest()
a.GetUserInfoRequest()
#a.setSolve()

a.setRefill()
a.setLoot()
a.setELoot()
#a.setFriends()

print a.startMission(1110100)[1]
exit(1)

while(1):
	print a.startMission(2000201)[1]
exit(1)

for m in missions:
	m=int(m)
	if m >= 1110100:# and m <= 1620705:
		todo.append(m)
todo.sort()
for m in todo:
	print a.startMission(m)[1]
exit(1)

def findM(i):
	res=[]
	for m in missions:
		m=int(m)
		_mn=Tools().findMissionName(m)
		if i in _mn:
			res.append(m)
	return res
	


if False:
	print a.startMission(7970104)[1]
	print a.startMission(7970104)[1]
	print a.startMission(7970104)[1]
	print a.startMission(7970104)[1]
	print a.startMission(7970104)[1]
	
#for i in findM('Timber Track'): a.startMission(i)[1]
for m in missions:
	m=int(m)
	if m >= 11421501:# and m <= 1620705:
		todo.append(m)
todo.sort()
for m in todo:
	print a.startMission(m)[1]