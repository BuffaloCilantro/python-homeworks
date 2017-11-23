import bst_helper

def bst_search (node, key):

	if node == None:
		return None

	elif key == node.key:
		return node.payload

	elif key < node.key:
		return bst_search(node.leftChild, key)

	elif key > node.key:
		return bst_search(node.rightChild, key)

print bst_helper.test_bst(bst_search)