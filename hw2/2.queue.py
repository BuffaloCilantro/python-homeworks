import Queue

def hot_potato_sim (n):

	q = Queue.Queue()
	q.put("Nia") #1
	q.put("Alex") #2
	q.put("Brehanu") #3
	q.put("Artie") #4
	q.put("Charlie") #5
	q.put("Jake") #6

	for i in range(5):
		for j in range(n):
			q.put(q.get())
		winner = q.get()
		print winner, "came to class 1 millisecond too late and faced the wrath of the crisply baked potato."
		print ""
	print q.get(), "has survived the purge."

hot_potato_sim(1)