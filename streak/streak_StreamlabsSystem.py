ScriptName = "Streak" # name of script
Website = "" # no website
Description = "DBD Streak command. Too much stuff to put in this little thing" # command of description
Creator = "TheKingWalnut" # Me :D
Version = "1.2.2" # Version number
Command = "!streak" # Command
Params = ['add', 'set', 'view'] #parameters list I didn't use yet, but might use later
Mods = ["adamantlyme", "merrycrimi", "cheddar_fetter", "ravenclawseekergirl", "terrinx8", "deltac", "thekingwalnut", "mario7354"] # Shitty list of Mods lmao

from values import killers # List of all killers and their active streaks
from values import maxkillers # List of all killers and their best streaks
from values import pb # Contains the best streaks Adam has had.
currStreak = 0 # global streak
bestKiller = ""

def Init(): # initialize func
	log("entered init") #logs entering
	try:
		f = open("test.txt", "r") #open a text file
		i = 0
		for line in f: # for every line in the txt file
			i += 1 #increment
			if i > 44: #if i is over 44 (len of killers + max killers) 
				pb[0] = int(line) #set pb[0] to the pb[0] value stored
				break # leave
			elif i > 22: # if i is over 22 (len of killers)
				key, value = line.split(",") # split the line into a key value pair
				maxkillers[key] = int(value) # set maxkillers key to the value
			else: # if i is less than 22 and 44
				key, value = line.split(",") # split the line into a key value pair
				killers[key] = int(value) # set killers key to the value
		f.close()
	except:
		log("file no exist :(")
	log("exited init") #logs leaving
	return

def Execute(data): # function when command is called
	log("entered execute") #logged
	if(data.GetParam(0) != Command or Parent.IsOnUserCooldown(ScriptName, Command, data.User)): # if the first thing isn't the command
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
		#Parent.AddUserCooldown(ScriptName, Command, data.User, 30) # sets a user cooldown for 30s
		try:
			view(data.GetParam(2)) # tries to enter the reset function with the user who called it and a killer
		except:
			view() # if that fails, just go in with the user 
		return
	if(data.GetParam(1) == 'reset'): # if the first thing after the command is reset
		log("entered reset") # log
		try:
			reset(user, data.GetParam(2)) # tries to enter the reset function with the user who called it and a killer
		except:
			reset(user) # if that fails, just go in with the user 
		return
	log("goodbye")
	send_message("Sorry, that's not a valid use.")
	return

def Tick():
	global bestKiller
	for key in maxkillers: # goes thru dict by key
		if maxkillers[key] == int(pb[0]): # if they value for any given killer is the current best
			bestKiller = str(key).capitalize() # set best killer equal to that killer's name
	return

def add(name, user): # add function
	global currStreak # get the global currStreak value
	log('in add')
	if not (user.lower() in Mods): # if the passed user is not in the mods list
		log("not a mod") # log it
		return # gtfo
	if(name.lower() in killers): # if the passed name is in the list of killers
		log('name in killers')
		killers[name.lower()] += 1 # add 1 to that killer's associated value
		ans = ("Streak for " + normalize(name) + " has been updated. ") # add the string to ans
		if(killers[name.lower()] > maxkillers[name.lower()]): # if the current streak is better than that killers old best streak
			maxkillers[name.lower()] = killers[name.lower()] # set maxkillers to killers best
			ans += ("New best streak for " + normalize(name) + "! ") # dumb message letting you know it happened
		log('entering the name > maxStreak')
		if killers[name.lower()] > pb[0]: # if the currStreak is greater than the best streak
			log('we in')
			pb[0] = killers[name.lower()] # make the best streak equal to currStreak
			ans += ("New overall best streak achieved! Streak of " + str(pb[0]) + ".") # add this on to the ans
			log('we leaving')
		log('we out')
		f = open("test.txt", "w") # this bit just writes killers, maxkillers, and pb to a file so it can save between uses
		for i in killers:
			f.write(i)
			f.write(", ")
			f.write(str(killers.get(i)))
			f.write("\n")
		for i in maxkillers:
			f.write(i)
			f.write(", ")
			f.write(str(maxkillers.get(i)))
			f.write("\n")
		f.write(str(pb[0]))
		f.close()
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
	if(name.lower() in killers): # if the passed name is in the killer list
		killers[name.lower()] = int(val) # set that killer's value to the appropriate value on the killer list
		if killers[name.lower()] > maxkillers[name.lower()]: # if that is better than the old best
			maxkillers[name.lower()] = int(killers[name.lower()]) # set the best to the current one
		ans = ("Streak has been set to " + str(val)) # ans setting
		send_message(ans) # return ans
		f = open("test.txt", "w") # this bit just writes killers, maxkillers, and pb to a file so it can save between uses
		for i in killers:
			f.write(i)
			f.write(", ")
			f.write(str(killers.get(i)))
			f.write("\n")
		for i in maxkillers:
			f.write(i)
			f.write(", ")
			f.write(str(maxkillers.get(i)))
			f.write("\n")
		f.write(str(pb[0]))
		f.close()	
		return
	send_message("Oops, that killer was not found.") # if the killer isn't found, here's an error
	return

def view(*args, **kwargs): # view function
	log('in view')
	ans = ""
	try: # this try block will look to see if the user passed in a killer to look at, and if they didn't, it'll just send the best overall streak.
		streak = killers[args[0].lower()] # set streak to the given killer's streak
		beststreak = maxkillers[args[0].lower()] # get the best streak for the given killer
		ans = "Adam's current streak on " + str(normalize(args[0])) + " is " + str(streak) + ". " #adam's current streak
		ans += "Adam's best streak on " + str(normalize(args[0])) + " is " + str(beststreak) + ". " #adam's best streak
	except:
		log("no arg passed")
	localbest = 0
	localkiller = ""
	for killer in killers:
		log(str(killers[killer]))
		if killers[killer] > localbest:
			log("Entered on " + killer)
			localbest = killers[killer]
			localkiller = str(killer)
	if(localbest != 0):
		ans += "The best active streak is " + str(localbest) + " on " + normalize(localkiller)
	else:
		ans += "There is no best active streak right now"
	ans += ". The best streak over all is " + str(int(pb[0])) + " on " + bestKiller + "."
	#ans = "Current streak is " + str(currStreak) + " and the max streak is " + str(int(pb[0])) # gets the currStreak and the best streak and puts them in a string
	send_message(ans) # returns the string
	return

def reset(user, *args, **kwargs): # reset function
	global currStreak # get the global currStreak
	if not (user.lower() in Mods): # if the passed user isn't a mod
		log("not a mod") # log
		return # gtfo
	currStreak = 0 # set the global currStreak to 0
	#ans = "Current Streak has been set to 0." # adds that it set the streak to 0 to ans
	if args[0] != "": # if a killer was passed in, reset that too
		killers[args[0].lower()] = 0 # set the killer's thing to 0
		ans = " Streak for " + normalize(args[0]) + " has been set to 0." # adds that you did that on to ans
		f = open("test.txt", "w") # this bit just writes killers, maxkillers, and pb to a file so it can save between uses
		for i in killers:
			f.write(i)
			f.write(", ")
			f.write(str(killers.get(i)))
			f.write("\n")
		for i in maxkillers:
			f.write(i)
			f.write(", ")
			f.write(str(maxkillers.get(i)))
			f.write("\n")
		f.write(str(pb[0]))
		f.close()
	else:
		ans = "Sorry, please specify a killer!"
	send_message(ans) # returns ans

def log(message): # log function for me :)
	Parent.Log(Command, message)

def send_message(message): # send message for me :)
	Parent.SendStreamMessage(message)
	return

def normalize(msg): #makes the code look nicer (no more .lower.capitalize)

	return msg.lower().capitalize()
