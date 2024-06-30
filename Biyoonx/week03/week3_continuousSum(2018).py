import sys
read = sys.stdin.readline

n = int(read())
num_list = range(1, n + 1)

# 부분합 구간의 시작점을 1에서 이동시킬 수 없는 문제
'''
sum_list = [0] * n
sub_list = [0] * n
for num in num_list:
		sum_list[num - 1] = (num + (sum_list[num - 2] if num > 1 else 0))
		sub_list[num - 1] = sum_list[num - 1] % n

result_cnt = 0
for num in sub_list:
		if num < 0 or num >= n:
				continue
		result_cnt += 1
print(result_cnt)
'''

# 시간 초과
'''
idx1 = 0
idx2 = 1
result = 0
while idx2 <= n:
		sub_sum = sum(num_list[idx1:idx2])
		if sub_sum == n:
				result += 1
				idx2 += 1
		elif sub_sum > n:
				idx1 += 1
		else: # sub_sum < n
				idx2 += 1
print(result)
'''

idx1 = 0
idx2 = 1
sub_sum = num_list[idx1]
result = 0
while True:
		if sub_sum == n:
				result += 1
				if idx2 == n:
						break;
				sub_sum += num_list[idx2]
				idx2 += 1
		elif sub_sum > n:
				sub_sum -= num_list[idx1]
				idx1 += 1
		else: # sub_sum < n
				sub_sum += num_list[idx2]
				idx2 += 1
print(result)