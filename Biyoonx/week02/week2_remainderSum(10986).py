import sys
read = sys.stdin.readline

num_cnt, submultiple = map(int, read().split())
num_list = [0] * sum(range(1, num_cnt + 1))
for idx, num in enumerate(map(int, read().split())):
		num_list[idx] = (num + (num_list[idx - 1] if idx != 0 else 0)) % submultiple

print(num_list)

# 시간 초과
'''
sum_list = []
for start in range(0, num_cnt):
		for end in range(start + 1, num_cnt + 1):
				sum_list.append(sum(num_list[start:end]) % submultiple)
print(sum_list.count(0))
'''

