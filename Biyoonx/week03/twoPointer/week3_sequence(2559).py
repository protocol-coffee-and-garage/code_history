import sys
read = sys.stdin.readline

n, k = map(int, read().split())
t_list = list(map(int, read().split()))

idx1 = 0
idx2 = 0
sub_sum = t_list[0]
result = 0

while idx1 < n and idx2 < n:
		result = max(result, sub_sum)