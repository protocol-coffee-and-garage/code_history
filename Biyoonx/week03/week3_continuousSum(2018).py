import sys
read = sys.stdin.readline

n = int(read())
num_list = range(1, n + 1)
sum_list = [0] * n

# 부분합 구간의 시작점을 1에서 이동시킬 수 없는 문제
# 
sub_list = [0] * n
for num in num_list:
		sum_list[num - 1] = (num + (sum_list[num - 2] if num > 1 else 0))
		sub_list[num - 1] = sum_list[num - 1] - n
		print(sum_list)
		print(sub_list)

result_cnt = 0
for num in sub_list:
		if num < 0 or num >= n:
				continue
		result_cnt += 1
print(result_cnt)