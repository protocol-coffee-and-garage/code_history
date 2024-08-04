from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
order_list = [read().strip() for _ in range(n)]

queue = deque()
for order in order_list:
		if order.startswith('push'):
				_, num = order.split()
				queue.append(num)
		elif order == 'pop':
				print(queue.popleft() if queue else '-1')
		elif order == 'size':
				print(len(queue))
		elif order == 'empty':
				print(1 if not queue else 0)
		elif order == 'front':
				print(queue[0] if queue else '-1')
		elif order == 'back':
				print(queue[-1] if queue else '-1')