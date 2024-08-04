from collections import deque
import sys
read = sys.stdin.readline

n = int(read())
n_deque = deque([*range(1, n + 1)])

while n_deque and len(n_deque) > 1:
		n_deque.popleft()
		card = n_deque.popleft()
		n_deque.append(card)

print(n_deque.pop())