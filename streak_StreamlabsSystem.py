ScriptName = "Streak"
Website = ""
Description = "For any user to look at the streak stats."
Creator = "TheKingWalnut"
Version = "0.0.1"
Command = "!streak"
Params = ['add', 'set', 'view']
Mods = ["adamantlyme", "merrycrimi", "cheddar_fetter", "ravenclawseekergirl", "terrinx8", "deltac", "thekingwalnut", "mario7354"]

from values import killers
from values import pb

def Init():
	log("entered init")
	return

def Execute(data):
	log("entered execute")
	if(data.GetParam(0) != Command):
		return
	user = data.UserName
	if(data.GetParamCount() > 4):
		send_message("Error: Too many parameters.")
		return
	if(data.GetParam(1) == 'add'):
		log("entered add")
		add(data.GetParam(2), user)
		return
	if(data.GetParam(1) == 'set'):
		log("entered set")
		set(data.GetParam(2), data.GetParam(3), user)
		return
	if(data.GetParam(1) == 'view'):
		log("entered view")
		view()
		return
	return

def Tick():
	return

def add(name, user):
	log('in add')
	if not (user.lower() in Mods):
		log("not a mod")
		return
	if(name in killers):
		log('name in killers')
		killers[name] += 1
		ans = ("Streak for " + name + " has been updated.")
		log('entering the name > maxStreak')
		if killers[name] > pb[0]:
			log('we in')
			pb[0] = killers[name]
			ans += (" New max streak achieved! Streak of " + str(pb[0]))
			log('we leaving')
		log('we out')
		send_message(ans)
		return
	log('did not work')
	send_message("name not found")
	return

def set(name, val):
	log('in set')
	if not (user.lower() in Mods):
		log("not a mod")
		return
	if(name in killers):
		killers[name] = val
		ans = ("Streak has been set to " + str(val))
		send_message(ans)
	return

def view():
	log('in view')
	ans = (str(killers) + str(pb))
	send_message(ans)
	return

def log(message):
	Parent.Log(Command, message)

def send_message(message):
	Parent.SendStreamMessage(message)
	return
