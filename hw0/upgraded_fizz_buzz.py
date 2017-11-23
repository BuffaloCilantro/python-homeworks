#function: mul_sum
#takes in number "n" and returns the sum of all multiples of 3 and 5 between "n" and 0
#input/output: 10/23, etc.


def mul_sum(number):
	final_sum = 0
	
	for i in range(0, number):

		if i % 3 == 0:
			final_sum += i
			

		if i % 5 == 0:
			final_sum += i
	
	return final_sum	

	
	




assert mul_sum (10) == 23
assert mul_sum (11) == 33
assert mul_sum (0) == 0
assert mul_sum (88) == 2070

