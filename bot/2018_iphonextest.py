from main import API,Tools

_player='9DCB10ED-B4D9-47E4-9CC3-47235029CCE3'
_device=1

a=API()
a.setPlayerID(_player,_device)

a.InitializeRequest()
a.GetUserInfoRequest()
a.setSolve()

a.setLoot()
a.setELoot()
a.setFriends()

print a.startMission(1110301)[1]
print a.startMission(1110302)[1]
print a.startMission(1110303)[1]
