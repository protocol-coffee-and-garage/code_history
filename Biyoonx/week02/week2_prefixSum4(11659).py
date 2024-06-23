import sys
read = sys.stdin.readline

num_cnt, sum_cnt = map(int, read().split())

# 시간 초과
'''
num_list = [*map(int, read().split())]

for _ in range(sum_cnt):
		start, end = map(int, read().split())
		print(sum(num_list[start - 1:end]))
'''

# 부분합 활용
sum_list = [0]
for idx, num in enumerate([*map(int, read().split())]):
		sum_list.append(num + sum_list[idx])

for _ in range(sum_cnt):
		a, b = map(int, read().split())
		print(sum_list[max(a, b)] - sum_list[min(a, b) - 1])