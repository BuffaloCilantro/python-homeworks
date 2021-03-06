# Hi Eugene
###############################
# CSAI HOMEWORK 3
# STENCIL CODE
# Author: zminster
# Date: January 21, 2015
###############################

import Queue

class Node(object):
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

###############################
# TODO: TASK 1
###############################
Q = Queue.PriorityQueue()
Q.put((26617, Node(" ")))
Q.put((10249, Node("a")))
Q.put((1816, Node("b")))
Q.put((2840, Node("c")))
Q.put((5376, Node("d")))
Q.put((15846, Node("e")))
Q.put((2712, Node("f")))
Q.put((2493, Node("g")))
Q.put((8639, Node("h")))
Q.put((8905, Node("i")))
Q.put((110, Node("j")))
Q.put((1257, Node("k")))
Q.put((6489, Node("l")))
Q.put((4238, Node("m")))
Q.put((8578, Node("n")))
Q.put((11450, Node("o")))
Q.put((2006, Node("p")))
Q.put((218, Node("q")))
Q.put((8100, Node("r")))
Q.put((8668, Node("s")))
Q.put((12450, Node("t")))
Q.put((4739, Node("u")))
Q.put((1219, Node("v")))
Q.put((3110, Node("w")))
Q.put((177, Node("x")))
Q.put((3198, Node("y")))
Q.put((120, Node("z")))

###############################
# TODO: TASK 2
###############################
def huffman_encode(Q):

	while Q.qsize() != 1:
		A = Q.get()
		B = Q.get()
		N = Node()
		N.left = B[1]
		#print "left is", N.left
		N.right = A[1]
		#print "right is", N.right
		#print ""
		Q.put((A[0] + B[0], N))
	return Q.get()[1]





















	'''
	node = Q.get()
	larger_than_node_node = Q.get()
	N = Node()
		
	N.left = larger_than_node_node
		#print "left is,", N.left

	N.right = node
		#print "right is,", N.right
		
		#print ""
		
	Q.put(N.left[0] + N.right[0])
	
	while Q.qsize() != 1:
		node1 = Q.get()
		node2 = Q.get()
		Nide = Node()
	
		Nide.left = node2
		print "left is", Nide.left

		Nide.right = node1
		print "right is", Nide.right
		print ""
	
		Q.put(Nide.left[0] + Nide.right)
	print Q.get()
'''

'''
		Q.put((60, Node("lol")))

		for i in range(5):
			print Q.get()[0]
		print ""
		#testing
		'''
'''
		lol1 = Q.get()
		lol2 = Q.get()

		Q.put((lol1[0] + lol2[0], Node("lul")))
		for i in range(4):
			print Q.get()[0]
			#testing
		'''

'''
		node1 = Q.get()
		node2 = Q.get()
		Nide = Node()
	
		Nide.left = node2

		Nide.right = node1
	
		Q.put(Nide.left[0] + Nide.right, Nide)
	return Q.get()[1]
	'''


###############################
# TESTING CODE
# if any of the assertions fail (you get an AssertionError), something is wrong!
###############################

# generic simple test
Q_simple = Queue.PriorityQueue()
Q_simple.put((35, Node('b')))
Q_simple.put((40, Node('a')))
Q_simple.put((20, Node('c')))
Q_simple.put((5, Node('d')))

huff_simple = huffman_encode(Q_simple)
assert huff_simple.left.data == None
assert huff_simple.left.left.data == 'b'
assert huff_simple.left.right.data == None
assert huff_simple.left.right.left.data == 'c'
assert huff_simple.left.right.right.data == 'd'
assert huff_simple.right.data == 'a'
assert huff_simple.right.left == None
assert huff_simple.right.right == None

print "Simple (homework example) tests passed."

# generic complex test

Q_complex = Queue.PriorityQueue()
Q_complex.put((24, Node('a')))
Q_complex.put((97, Node('b')))
Q_complex.put((70, Node('c')))
Q_complex.put((6, Node('d')))
Q_complex.put((96, Node('e')))
Q_complex.put((96, Node('f')))
Q_complex.put((52, Node('g')))
Q_complex.put((89, Node('h')))
Q_complex.put((17, Node('i')))
Q_complex.put((42, Node('j')))

huff_complex = huffman_encode(Q_complex)
assert huff_complex.left.data == None
assert huff_complex.right.data == None
assert huff_complex.left.left.data == None
assert huff_complex.right.left.data == None
assert huff_complex.right.right.data == 'b'
assert huff_complex.left.left.left.data == 'f' or huff_complex.left.left.right.data == 'f'
assert huff_complex.left.right.right.data == 'h' or huff_complex.left.right.left.data == 'h'

print "Complex (10 initial nodes) tests passed."

# basic sanity checks on correct homework response

huff_homework = huffman_encode(Q)
assert huff_homework.left.data == None
assert huff_homework.right.data == None
assert huff_homework.left.left.data == None
assert huff_homework.left.right.data == None
assert huff_homework.right.left.data == None
assert huff_homework.right.right.data == None
assert huff_homework.left.left.left.data == ' '
assert huff_homework.left.left.right.data == None
assert huff_homework.left.left.right.right.data == 't'

print "Hamlet tests passed."

print "All tests passed!"

