#function: i_love_gambling
#what this AI does is that it check your hand and returns True(hit), stay(False), then bust(BUST) if you hit and you go over 21
#input/output: value of each card and total value of cards/hit or stay, or bust if hit previous turn

def i_love_gambling (card1, card2): 
	total = card1 + card2
	hit = 0
	
	if total > 13:
		return False
	if total == 13 or total < 13:
		hit += 1
		return True

	if card1 < 1 or card2 < 1:
		return False 

	else:
		return False
		


assert i_love_gambling (9, 10) == False
assert i_love_gambling (9, 2) == True
assert i_love_gambling (0, 9) == False


