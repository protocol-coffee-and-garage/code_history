import sys
read = sys.stdin.readline

n, m = map(int, read().split())
n_list = list(map(int, read().split()))

idx1 = 0
idx2 = 0
sub_sum = n_list[0]
result = 0
while idx1 < n and idx2 < n:
		if (sub_sum <= m):
				if (sub_sum == m):
						result += 1
				idx2 += 1
				if (idx2 < n):
						sub_sum += n_list[idx2]
		else: # sub_sum > m
				sub_sum -= n_list[idx1]
				idx1 += 1

print(result)