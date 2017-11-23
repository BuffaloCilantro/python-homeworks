#function: im_picky
#takes in the input (which should be Empire, Gala, Rome or York), and identifies if they are ones I like. Then it prints answers depending on whether I like them or not
#input is an apple type (Empire, Gala, Rome, York or an apple I haven't heard of yet), and returns if I like it(true) or not(false)

def im_picky (apples):
	if str(apples) == "Empire":
		return "true"

	if str(apples) == "Gala":
		return "true"

	if str(apples) == "Rome":
		return "false"

	if str(apples) == "York":
		return "false"	

	else:
		return "false"


assert im_picky("Empire") == "true"
assert im_picky("Gala") == "true"
assert im_picky("Rome") == "false"
assert im_picky("York") == "false"
assert im_picky("STAB") == "false"















#function: im_picky_and_full
#takes in an apple type and quantity of apple, and returns answered based off whether I like them or not, and if I can finish all of them or not, my limit being 5 apples
#input/output: appletype and quantity/false or true, depending on the inputs and my preferences

def im_picky_and_full (applez, quantity):
	if str(applez) == "Empire":
		if quantity > 5 or quantity < 0:
			return "false"
		if quantity == 5 or quantity < 5 or quantity == 0: 
			return "true"

	if str(applez) == "Gala":
		if quantity > 5 or quantity < 0:
			return "false"
		if quantity == 5 or quantity < 5 or quantity == 0: 
			return "true"

	if str(applez) == "Rome":
		if quantity == 0:
			return "true"
		else:
			return "false"

	if str(applez) == "York":
		if quantity == 0:
			return "true"
		else:
			return "false"

	else:
		return "false"


assert im_picky_and_full ("Gala", -5) == "false"
assert im_picky_and_full ("", 3) == "false"
assert im_picky_and_full ("Empire", 5) == "true"
assert im_picky_and_full ("York", 0) == "true"
assert im_picky_and_full ("Gala", 3) == "true"
assert im_picky_and_full ("Empire", 3) == "true"
assert im_picky_and_full ("Rome", 3) == "false"

