from queue import Queue
q=Queue(maxsize=3)
print(q.qsize())
q.put('m')
q.put('n')
q.put('o')
print("\nfull:",q.full())
print("\n element dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nempty",q.empty())
q.put(1)
print("\nempty",q.empty())
print("full",q.full())