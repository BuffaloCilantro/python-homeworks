
#NOTE: Because I am using global variables, you have to run each assert seperately.

#function: good_day
#takes in multiple strings 	which contain the apples i have collected today, and returns good or bad, depending on how many good(apples i like) and bad(apples i dislike) i collected
#input/output: x+1 good apples and x bad apples/true, x good apples and x+1 bad apples/false, x good apples and x bad apples/false, not an apple and not an apple/false, no apples/false

I_like_dem_apples = 0
I_dont_like_dem_apples = 0

def how_do_you_like_them_applez(steve_jobs):
	
	if steve_jobs == "Empire" or steve_jobs == "Gala":
		global I_like_dem_apples
		I_like_dem_apples += 1

	elif steve_jobs == "Rome" or steve_jobs == "York":
		global I_dont_like_dem_apples
		I_dont_like_dem_apples += 1

	else:
		I_dont_like_dem_apples += 1
	

def good_day (the_good_stuff):

	if len(the_good_stuff) == 0:
		return False

	for apple in the_good_stuff:
		how_do_you_like_them_applez(apple)

	if I_dont_like_dem_apples > I_like_dem_apples or I_dont_like_dem_apples == I_like_dem_apples:
		#return False
		print False

	if I_like_dem_apples > I_dont_like_dem_apples:
		#return True
		print True

assert good_day (["Gala", "Gala", "Rome", "York", "Empire"]) == True
assert good_day ([]) == False
assert good_day (["York", "Gala", "Rome"]) == False
assert good_day (["STAB", "FakeAppleType", "Gala"]) == False
assert good_day (["STAB", "FakeAppleType", "Gala", "Gala"]) == False
assert good_day (["STAB", "FakeAppleType", "Gala", "Gala", "Gala"]) == True
assert good_day (["STAB", "FakeAppleType", "Gala", "Gala", "Empire"]) == True
assert good_day ("") == False



