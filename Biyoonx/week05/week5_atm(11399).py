import sys
read = sys.stdin.readline

n = int(read())
p_list = [*map(int, read().split())]

p_list.sort()

sum = 0
for idx in range(n):
		sum += p_list[idx] * (n - idx)

print(sum)