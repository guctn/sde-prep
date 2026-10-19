# QUEUES - FIRST IN FIRST OUT (FIFO)
from collections import deque 
# this implements a double-ended queue - doubly linked list
# we can add and delete values from the end and start - O(1)

q = deque()

print(q)
# out: deque([])


# Enqueue - Add element in the queue's end - O(1)
q.append(5)
q.append(6)
q.append(8)
q.append(7)


print(q)
# out: deque([5, 6, 8, 7])

# Dequeue - remove element from the start - O(1)
q.popleft()
# out: 5


# Peek from the start - O(1)
q[0]
# out: 6

# Peek from the end - O(1)
q[-1]
# out: 7

