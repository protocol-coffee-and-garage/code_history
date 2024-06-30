import sys
read = sys.stdin.readline

n = int(read())
num_list = [*map(int, read().split())]
num_list.sort()

for idx in range(2, n):
		num = num_list[idx]
		