from collections import deque

stack = []
stack.append('first')
stack.append('second')
stack.append('last')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

queue = deque()
queue.append('1')
queue.append('2')
queue.append('3')
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

queue.appendleft('2')
queue.appendleft('1')
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)
queue = deque([1, 2, 3, 4, 5, 6, 1, 2, 1, 3, 3, 3, 4, 4, 5, 6])
print(queue.count(1))
print(queue.count(3))



