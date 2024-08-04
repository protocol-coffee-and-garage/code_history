from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
order_list = [read().strip() for _ in range(n)]

deq = deque()
for order in order_list:
		if order.startswith('push_front'):
				_, num = order.split()
				deq.appendleft(num)
		elif order.startswith('push_back'):
				_, num = order.split()
				deq.append(num)	
		elif order == 'pop_front':
				print(deq.popleft() if deq else -1)
		elif order == 'pop_back':
				print(deq.pop() if deq else -1)
		elif order == 'size':
				print(len(deq))
		elif order == 'empty':
				print(1 if not deq else 0)
		elif order == 'front':
				print(deq[0] if deq else -1)
		elif order == 'back':
				print(deq[-1] if deq else -1)
