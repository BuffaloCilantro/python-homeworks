#function: plaindrome
#take in a word, checks if it is a palindrome(a word that stays keeps the same characters in order when written in reverse order) by checking each letter and seeing if it has the same character in the reverse position of said string (formula: index_# + (total_number_of_indexes - (2 * index_#))). if the word is indeed a palindrome, the function will True. if not, it will return False
#input/output: racecar/True, Racecar/true, toy/false
def check_word(word):
	if word == "" or word == " ":
		return True
	if word[0] == " ":
		check_word(word[1:len(word)])
		return True
	elif word[len(word) - 1] == " ":
		check_word(word[0:len(word) - 1])
		return True
	elif word[0] ==  word[len(word) - 1]:
		return True
	else:
		return False
	

def palindrome(string):	
	return check_word(string)

	


assert palindrome("racecar") == True
assert palindrome("   racecar") == True
assert palindrome("toy") == False
assert palindrome("123") == False
assert palindrome(" ") ==  True
assert palindrome("") ==  True


