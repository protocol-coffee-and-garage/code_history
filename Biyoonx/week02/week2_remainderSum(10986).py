import sys
read = sys.stdin.readline

num_cnt, submultiple = map(int, read().split())
num_list = [*map(int, read().split())]

# 시간 초과
'''
sum_list = []
for start in range(0, num_cnt):
		for end in range(start + 1, num_cnt + 1):
				sum_list.append(sum(num_list[start:end]) % submultiple)
print(sum_list.count(0))
'''
