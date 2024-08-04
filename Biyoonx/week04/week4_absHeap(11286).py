from queue import PriorityQueue
import sys
read = sys.stdin.readline

n = int(read())
n_list = [int(read()) for _ in range(n)]

pq = PriorityQueue()
for num in n_list:
		if num == 0:
				if pq.empty():
						print(0)
						continue
				print(pq.get()[1])
		else: # num != 0
				pq.put((abs(num), num))