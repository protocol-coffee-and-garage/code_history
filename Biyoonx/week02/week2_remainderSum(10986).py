import sys
read = sys.stdin.readline

num_cnt, submultiple = map(int, read().split())

# 시간 초과1
'''
sum_list = []
for start in range(0, num_cnt):
		for end in range(start + 1, num_cnt + 1):
				sum_list.append(sum(num_list[start:end]) % submultiple)
print(sum_list.count(0))
'''

# 시간 초과2
'''
num_list = [0] * num_cnt
for idx, num in enumerate(map(int, read().split())):
		num_list[idx] = (num + (num_list[idx - 1] if idx != 0 else 0)) % submultiple

submultiple_cnt = num_list.count(0)
for num in range(submultiple):
		cnt = num_list.count(num)
		submultiple_cnt += (cnt * (cnt - 1)) // 2

print(submultiple_cnt)
'''

num_list = [0] * num_cnt
num_cnt_dict = dict(zip(range(submultiple), [0] * submultiple))
for idx, num in enumerate(map(int, read().split())):
		num_list[idx] = (num + (num_list[idx - 1] if idx != 0 else 0)) % submultiple
		num_cnt_dict[num_list[idx]] += 1

submultiple_cnt = num_cnt_dict.get(0)
for num in range(submultiple):
		cnt = num_cnt_dict.get(num)
		submultiple_cnt += (cnt * (cnt - 1)) // 2

print(submultiple_cnt)