from collections import deque
q=deque()
q.append('g')
q.append('f')
q.append('g')
print("initial queue")
print(q)
print("\nelements dequeued from the queue ")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nqueue after removing element")
print(q)

