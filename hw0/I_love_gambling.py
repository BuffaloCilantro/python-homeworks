#function: I_love_gambling
#what this AI does is it reads your hand (which consists of two cards), finds out the value of them and which card they are, then does the same for the dealer's one card facing up. Once it does this, it eliminates these numbers off a list containing all of the card values (A being identified as 1/11)
#input/output: each card face-up and its value/false or true depending on the percentage of drawing a card that'll make you go over 21

def EXTERMINATE (the_card):
	for i in the_deck:
		if i == the_card:
			cannot_draw[] = cannot_draw[] + the_deck[i]
			the_deck[i] = the_deck[i] - the_deck[i]
			return



def play (my_card1, my_card2, dealer_card, hits):
	ace1 = 1
	ace2 = 1
	ace3 = 1
	ace4 = 1

	global the_deck
	the_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, ace1, ace2, ace3, ace4]

	global cannot_draw
	cannot_draw = []
	
	your_hand = my_card1 + my_card2
	EXTERMINATE (my_card1)
	


	print your_hand

play(10, 9, 9, 0)