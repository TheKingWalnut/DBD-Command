ScriptName = "Streak" # name of script
Website = "" # no website
Description = "DBD Streak command. Too much stuff to put in this little thing" # command of description
Creator = "TheKingWalnut" # Me :D
Version = "0.0.1" # Version number
Command = "!streak" # Command
Params = ['add', 'set', 'view'] #parameters list I didn't use yet, but might use later
Mods = ["adamantlyme", "merrycrimi", "cheddar_fetter", "ravenclawseekergirl", "terrinx8", "deltac", "thekingwalnut", "mario7354"] # Shitty list of Mods lmao

from values import killers # import from external file
from values import pb # import from external file
currStreak = 0 # global streak

def Init(): # initialize func
	log("entered init") #logs entering
	log("exited init") #logs leaving
	return

def Execute(data): # function when command is called
	log("entered execute") #logged
	if(data.GetParam(0) != Command): # if the first thing isn't the command
		return # leave
	user = data.UserName # create a variable "user" that's the username of the user
	if(data.GetParamCount() > 4): # if there are more than 4 paramters
		send_message("Error: Too many parameters.") # too many parameters for the command
		return #leave
	if(data.GetParam(1) == 'add'): # if the first thing after the command is add
		log("entered add") #log
		add(data.GetParam(2), user) # go to add, passing in the killer and the user who called it
		return
	if(data.GetParam(1) == 'set'): # if the first thing after the command is set
		log("entered set") # log
		set(data.GetParam(2), data.GetParam(3), user) # go to set, passing in the killer, the val, and the user who called it
		return
	if(data.GetParam(1) == 'view'): # if the first thing after the command is view
		log("entered view") # log
		view() # go to view
		return
	if(data.GetParam(1) == 'reset'): # if the first thing after the command is reset
		log("entered reset") # log
		try:
			reset(user, data.GetParam(2)) # tries to enter the reset function with the user who called it and a killer
		except:
			reset(user) # if that fails, just go in with the user 
		return
	return

def Tick():
	return

def add(name, user): # add function
	global currStreak # get the global currStreak value
	log('in add')
	if not (user.lower() in Mods): # if the passed user is not in the mods list
		log("not a mod") # log it
		return # gtfo
	if(name in killers): # if the passed name is in the list of killers
		log('name in killers')
		killers[name] += 1 # add 1 to that killer's associated value
		ans = ("Streak for " + name + " has been updated.") # add the string to ans
		currStreak += 1 # add 1 to currStreak
		log('entering the name > maxStreak')
		if currStreak > pb[0]: # if the currStreak is greater than the best streak
			log('we in')
			pb[0] = currStreak # make the best streak equal to currStreak
			ans += (" New max streak achieved! Streak of " + str(pb[0])) # add this on to the ans
			log('we leaving')
		log('we out')
		send_message(ans) # return ans
		return
	log('did not work')
	send_message("name not found") # if there name wasn't found, then send an error message
	return

def set(name, val, user): # set function
	log('in set')
	if not (user.lower() in Mods): # if the passed user is not in the mods list
		log("not a mod") # log
		return # grfo
	if(name in killers): # if the passed name is in the killer list
		killers[name] = val # set that killer's value to the appropriate value on the killer list
		ans = ("Streak has been set to " + str(val)) # ans setting
		send_message(ans) # return ans
		return
	send_message("Oops, that killer was not found.") # if the killer isn't found, here's an error
	return

def view(): # view function
	global currStreak # get the global currStreak
	log('in view')
	ans = "Current streak is " + str(currStreak) + " and the max streak is " + str(int(pb[0])) # gets the currStreak and the best streak and puts them in a string
	send_message(ans) # returns the string
	return

def reset(user, *args, **kwargs): # reset function
	global currStreak # get the global currStreak
	if not (user.lower() in Mods): # if the passed user isn't a mod
		log("not a mod") # log
		return # gtfo
	currStreak = 0 # set the global currStreak to 0
	ans = "Current Streak has been set to 0." # adds that it set the streak to 0 to ans
	if(args[0] != ""): # if a killer was passed in, reset that too
		killers[args[0]] = 0 # set the killer's thing to 0
		ans += " Streak for " + args[0] + " has been set to 0." # adds that you did that on to ans
	send_message(ans) # returns ans

def log(message): # log function for me :)
	Parent.Log(Command, message)

def send_message(message): # send message for me :)
	Parent.SendStreamMessage(message)
	return