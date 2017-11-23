#function: num_ways
#take in input(hours: how much time you have to do homework in hours), and returns the total amount of ways you divide your homework up. HDS Hw = 1hr, Snapchat = 2, Math Hw = 1.5, Study Spanish 
#input/output: 0/None, 1/1, 2/2, etc.
HDS = 1 #2
Math = 1.5 #3
Snapchat = 2 #4
Spanish = 2.5 #5
Code = 3 #6

assignments =[1, 1.5, 2, 2.5, 3]
def num_ways(n):
	#base cases
	if n == 0:
		return 1
	if n < 0:
		return 0

	#main recursive body
	ways = 0
	for i in range(len(assignments)):
		ways += num_ways(n - assignments[i])

	return ways
'''



def num_ways(n):
	
	hours = 0
	diff_ways = 0
	
	while True:
		print "Hey, the time you have is", n*2, "hours"
		print ""
		for i in range(2 , 7, 1):
			print "i am looking at", i, "hours"
			print ""
			
			out_key = 0
			hours = n*2
			
			if hours - i < 0:
				#checks if the hours is too long for the given time
				out_key += 1
				print "this", i, "takes too much time."
				print ""
				
			while out_key == 0:
				hours -= i
				
				if hours < 0:
					diff_ways += 1
					out_key += 1
					print "I found another unique pattern to do your hw, which you'll never actually start on or bother to look at."
					print ""

		print diff_ways
		return diff_ways
'''
	
'''
	global counter
	global hw_time
	if hw_time < 0.5:
		return counter
	if hours_I_have > hw_time:
		hours_I_have =- hw_time
		counter =+ 1
		num_ways(hours_I_have)
	else:
		hw_time =- 0.5
		num_ways(hours_I_have)
'''






'''
	while loopbreaker == 0:
		if hours_spent < hours_I_have && hours_spent > hours_I_have:
			if counter == 0:
				return None
			else:
				return counter
'''
assert num_ways(2) == 2
assert num_ways(1) == 1
print(num_ways(8))
#num_ways(2)
