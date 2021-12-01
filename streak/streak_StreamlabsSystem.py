ScriptName = "Streak" # name of script
Website = "" # no website
Description = "DBD Streak command. Too much stuff to put in this little thing" # command of description
Creator = "TheKingWalnut" # Me :D
Version = "1.7.0" # Version number
Command = "!streak" # Command
Params = ['add', 'set', 'view'] #parameters list I didn't use yet, but might use later

killers = {'trapper': 0, 'wraith': 0, 'hillbilly': 0, 'nurse': 0, 'shape': 0, 'hag': 0, 'doctor': 0, 'huntress': 0, 'cannibal': 0, 'nightmare': 0, 'pig': 0, 'clown': 0, 'spirit': 0, 'legion': 0, 'plague': 0, 'ghostface': 0, 'demogorgon': 0, 'oni': 0, 'deathslinger': 0, 'executioner': 0, 'blight': 0, 'twins': 0, 'trickster': 0, 'nemesis': 0, 'cenobite': 0, 'artist': 0}
pb = [0]
maxkillers = {'trapper': 0, 'wraith': 0, 'hillbilly': 0, 'nurse': 0, 'shape': 0, 'hag': 0, 'doctor': 0, 'huntress': 0, 'cannibal': 0, 'nightmare': 0, 'pig': 0, 'clown': 0, 'spirit': 0, 'legion': 0, 'plague': 0, 'ghostface': 0, 'demogorgon': 0, 'oni': 0, 'deathslinger': 0, 'executioner': 0, 'blight': 0, 'twins': 0, 'trickster': 0, 'nemesis': 0, 'cenobite': 0, 'artist': 0}
# These arrays are extremely ugly but it's easier than doing a separate values file, for now.

currStreak = 0 # global streak
bestKiller = ""

def Init(): # initialize func
	log("entered init") #logs entering
	i = 0
	try:
		f = open("test.txt", "r") #open a text file
		log("File opened")
		lenk = len(killers)
		lenmk = lenk + len(maxkillers)
		log("len of killers is " + str(lenk))
		log("len of killers + maxkillers is " + str(lenmk))
		for line in f: # for every line in the txt file
			i += 1 #increment
			log("val of i is " + str(i))
			if i > lenmk: #if i is over len of killers + max killers
				log("pb is " + line)
				pb[0] = int(line) #set pb[0] to the pb[0] value stored
				break # leave
			elif i > lenk: # if i is over len of killers
				key, value = line.split(",") # split the line into a key value pair
				if(key in maxkillers): # make sure the killer is valid
					maxkillers[key] = int(value) # set maxkillers key to the value
				else:
					i -= 1
			else: # if i is less than len of killers and len of killers + max killers
				key, value = line.split(",") # split the line into a key value pair
				if(key in killers): # make sure the killer is valid
					killers[key] = int(value) # set killers key to the value
				else:
					i -= 1
		f.close()
	except:
		log("Error on line " + str(i) + " when reading file.")
		send_message("Unexpected value when reading file, this is a big deal! Let Jack know ASAP!!!")
		f.close()
	log("exited init") #logs leaving
	return

def Execute(data): # function when command is called
	log("entered execute") #logged
	if(data.GetParam(0) != Command or Parent.IsOnUserCooldown(ScriptName, Command, data.User)): # if the first thing isn't the command
		return # leave
	userName = data.UserName # create a variable "user" that's the username of the user
	userID = data.User
	if(data.GetParamCount() > 4): # if there are more than 4 paramters
		send_message("Error: Too many parameters.") # too many parameters for the command
		return #leave
	if(data.GetParam(1) == 'add'): # if the first thing after the command is add
		log("entered add") #log
		add(data.GetParam(2), userID, userName) # go to add, passing in the killer and the user who called it
		return
	if(data.GetParam(1) == 'set'): # if the first thing after the command is set
		log("entered set") # log
		set(data.GetParam(2), data.GetParam(3), data.User, userName) # go to set, passing in the killer, the val, and the user who called it
		return
	if(data.GetParam(1) == 'view'): # if the first thing after the command is view
		log("entered view") # log
		if not (Parent.HasPermission(userID, "moderator", userName)): # If the user isn't a mod, give them a 15s cooldown.
			Parent.AddUserCooldown(ScriptName, Command, data.User, 15) # sets a user cooldown for 15s
			log("User %s is not a mod"%userName)
		if(Parent.IsOnCooldown(ScriptName, Command)):
			log("CD")
			return
		Parent.AddCooldown(ScriptName, Command, 5); # Sets a global cooldown for 5 seconds, to avoid a weirdchamp one
		try:
			view(userID, userName, data.GetParam(2)) # tries to enter the view function with the user who called it and a killer
		except:
			view(userID, userName) # if that fails, just go in with the user 
		return
	if(data.GetParam(1) == 'reset'): # if the first thing after the command is reset
		log("entered reset") # log
		try:
			reset(userID, userName, data.GetParam(2)) # tries to enter the reset function with the user who called it and a killer
		except:
			reset(userID, userName) # if that fails, just go in with the user 
		return
	if(data.GetParam(1) == 'dec'): # if the first thing after the command is dec
		log("entered dec")
		dec(data.GetParam(2), userID, userName) # enters the dec function with the user and the killer
		return
	if(data.GetParam(1) == 'ver'): # if the first thing after the command is ver
		log("entered ver")
		ver(userID, userName) # enters the ver function with the user
		return
	log("goodbye")
	send_message("The official uses are '!streak view' or '!streak view <killer>', so try those!")
	return

def Tick():
	global bestKiller
	for key in maxkillers: # goes thru dict by key
		if maxkillers[key] >= int(pb[0]): # if they value for any given killer is the current best
			bestKiller = str(key).capitalize() # set best killer equal to that killer's name
			pb[0] = int(maxkillers[key])
#	log("best killer is " + str(bestKiller) + " with streak " + str(pb[0]))
	return

def add(name, userID, userName): # add function
	global currStreak # get the global currStreak value
	log('in add')
	if not (Parent.HasPermission(userID, "moderator", userName)): # if the passed user is not a mod
		log("add: not a mod") # log it
		send_message("Sorry, this is for mods only!")
		return # gtfo
	if(name.lower() in killers): # if the passed name is in the list of killers
		log('add: name in killers')
		killers[name.lower()] += 1 # add 1 to that killer's associated value
		ans = ("Streak for " + normalize(name) + " has been updated. ") # add the string to ans
		if(killers[name.lower()] > maxkillers[name.lower()]): # if the current streak is better than that killers old best streak
			maxkillers[name.lower()] = killers[name.lower()] # set maxkillers to killers best
			ans += ("New best streak for " + normalize(name) + "! ") # dumb message letting you know it happened
		log('add: entering the name > maxStreak')
		if killers[name.lower()] > pb[0]: # if the currStreak is greater than the best streak
			log('add: currStreak > pb[0]')
			pb[0] = killers[name.lower()] # make the best streak equal to currStreak
			ans += ("New overall best streak achieved! ") # add this on to the ans
			log('exiting currStreak > pb[0]')
		ans += ("Current streak is " + str(killers[name.lower()]) + ".") # prints the current streak at the end of the line.
		writeToFile()
		send_message(ans) # return ans
		return
	log('add: did not work')
	send_message("Killer name not found. Make sure it's the official name!") # if there name wasn't found, then send an error message
	return

def set(name, val, userID, userName): # set function
	log('in set')
	if not (Parent.HasPermission(userID, "moderator", userName)): # if the passed user is not a mod
		log("set: not a mod") # log
		send_message("Sorry, this is for mods only!")
		return # gtfo
	if(name.lower() in killers): # if the passed name is in the killer list
		killers[name.lower()] = int(val) # set that killer's value to the appropriate value on the killer list
		if killers[name.lower()] > maxkillers[name.lower()]: # if that is better than the old best
			maxkillers[name.lower()] = int(killers[name.lower()]) # set the best to the current one
		if killers[name.lower()] > pb[0]:
			pb[0] = int(killers[name.lower()])
		ans = ("Streak for " + normalize(name) + " has been set to " + str(val) + ".") # ans setting
		send_message(ans) # return ans
		writeToFile()
		return
	send_message("Killer name not found. Make sure it's the official name!") # if the killer isn't found, here's an error
	return

def view(userID, userName, *args, **kwargs): # view function
	log('in view')
	ans = ""
	try: # this try block will look to see if the user passed in a killer to look at, and if they didn't, it'll just send the best overall streak.
		log("Passed in value:" + str(args[0].lower()))
		if ((args[0].lower() == "all") and (Parent.HasPermission(userID, "moderator", userName))): # if the user typed in all and is a mod
			ans += "Active: " # ans = active
			for i in killers: # goes through killers and puts killer=value
				ans += (i + "=")
				ans += (str(killers[i]) + " ")
			send_message(ans) #sends that
			ans = "Max: " #resets ans to Max:
			for i in maxkillers: #goes through max killers and puts maxkiller=value
				ans += (i + "=") 
				ans += (str(maxkillers[i]) + " ")
			send_message(ans) #sends that
			return
		streak = killers[args[0].lower()] # set streak to the given killer's streak
		beststreak = maxkillers[args[0].lower()] # get the best streak for the given killer
		ans = "Adam's current streak on " + str(normalize(args[0])) + " is " + str(streak) + ". " #adam's current streak
		ans += "Adam's best streak on " + str(normalize(args[0])) + " is " + str(beststreak) + ". " #adam's best streak
	except:
		log("view: no arg passed")
	localbest = 0
	localkiller = ""
	for killer in killers:
#		log(str(killers[killer]))
		if killers[killer] > localbest:
			log("Entered on " + killer)
			localbest = int(killers[killer])
			localkiller = str(killer)
	if(localbest != 0):
		ans += "The best active streak is " + str(localbest) + " on " + normalize(localkiller)
	else:
		ans += "There is no best active streak right now"
	ans += ". The best streak over all is " + str(int(pb[0])) + " on " + bestKiller + "."
	#ans = "Current streak is " + str(currStreak) + " and the max streak is " + str(int(pb[0])) # gets the currStreak and the best streak and puts them in a string
	send_message(ans) # returns the string
	return

def reset(userID, userName, *args, **kwargs): # reset function
	global currStreak # get the global currStreak
	if not (Parent.HasPermission(userID, "moderator", userName)): # if the passed user isn't a mod
		log("reset: not a mod") # log
		send_message("Sorry, this is for mods only!")
		return # gtfo
	currStreak = 0 # set the global currStreak to 0
	if(args[0] != "" and args[0].lower() in killers):
		killers[args[0].lower()] = 0 # set the killer's thing to 0
		ans = " Streak for " + normalize(args[0]) + " has been set to 0." # adds that you did that on to ans
		writeToFile()
	else:
		ans = "Killer name not found. Make sure it's the official name!"
	send_message(ans) # returns ans

def dec(name, userID, userName): # decrements the current score.
	if not (Parent.HasPermission(userID, "moderator", userName)):
		log("dec: not a mod")
		send_message("Sorry, this is for mods only!")
		return
	if (name.lower() in killers):
		killers[name.lower()] -= 1
		maxkillers[name.lower()] -= 1
		ans = ("Max streak for " + normalize(name) + " has been decreased by one. ")
		if(maxkillers[name.lower()] + 1 >= pb[0]):
			pb[0] -= 1
			ans += ("Best overall was decreased by 1, because the value for " + normalize(name) + " tied it. ")
		ans += ("Active streak for " + normalize(name) + " was decreased by one as well, so if that's an issue, remember to !streak add!")
		send_message(ans)
		writeToFile()
		return
	log("dec: name not in killers")
	send_message("Killer name not found. Make sure it's the official name!")
	return

def ver(userID, userName):
	if not (Parent.HasPermission(userID, "moderator", userName)):
		log("ver: not a mod")
		send_message("Sorry, this is a mod only command!")
		return
	ans = ("Version is " + Version)
	send_message(ans)
	return

def Unload():
	log("Wrote to file in Unload")
	writeToFile()
	return

def writeToFile():
	try:
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
	except:
		log("error occured when writing to file in writeToFile")
	return

def log(message): # log function for me :)
	Parent.Log(Command, message)

def send_message(message): # send message for me :)
	Parent.SendStreamMessage(message)
	return

def normalize(msg): #makes the code look nicer (no more .lower.capitalize)

	return msg.lower().capitalize()
